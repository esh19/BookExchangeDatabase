# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re


class scraper:
    """ boksala.is scraper

    This class scrapes stuff from boksala.is <- need a better docstring :)
    """

    # default starting page - faculty list
    facultyList = 'http://www.boksala.is/kennslubokalistar/' \
        'haskoli-islands.html'

    # various selectors for scraper...
    # 1 - links in faculty list
    facultySelector = 'div .block-content dd ol li a'
    # 2 - links in programme list
    programmeSelector = 'div .block-content dd ol li a'
    # 3 - main div for booklists
    booklistSelector = 'div .col-main'
    # 4 - booklist - selector for programme name
    programeName = booklistSelector + " .sub_cat_title"
    # 5 - booklist - selector for book particulates
    bookCard = booklistSelector + " .category-products .item"

    # other stuff...
    # 6 - regex for freeing price from isk format
    isk = re.compile(r'(\d+)(?:\.)(\d+)')

    # a mapping object for mapping IS to EN
    # ***NOTE (kh):
    #   This needs better testing, or we at least need to handle the case
    #   if translation does not exists in the translation object, now we
    #   will just get an exception and the scraper will stop and loose all
    #   of it's work...
    book = {
        u'Höfundur': 'author',
        u'Útgefandi': 'publisher',
        u'Útgáfuár': 'publishing_year',
        u'Útgáfunúmer': 'edition',
        u'ISBN': 'isbn',
        u'ISBN13': 'isbn'
    }

    # -------------------------------------------------------------------------
    def getFaculties(self, url=False):
        """ Get all faculties

        @url (string): url to scrape, leave blank to use the
                       default facultyList

        Returns a list of dicts containing names and urls of faculties
        """
        if not url:
            url = self.facultyList

        q = []   # set up a placeholder

        soup = self._getBS(url)
        links = soup.select(self.facultySelector)

        for link in links:
            q.append({'name': link.string, 'url': link['href']})

        return q

    # -------------------------------------------------------------------------
    def getProgramme(self, url, faculty=None):
        """ Get all programmes from a given faculty

        @url (string): the faculty url

        Returns a list of dicts containing name and url of programmes
        """

        if not url:
            return False

        q = []   # set up a placeholder

        soup = self._getBS(url)
        links = soup.select(self.programmeSelector)

        for link in links:
            booklist = {
                'programme': link.string,
                # 'url': link['href'],
                'booklist': self.getProgrammeUrl(link['href']),
            }
            if faculty:
                booklist['faculty'] = faculty
            q.append(booklist)

        return q

    # -------------------------------------------------------------------------
    def getAllProgramme(self):
        """ Get all programmes from all faculties

        returns a list of dicts containing programme name, faculty name,
        faculty url and booklist url
        """

        q = []
        faculties = self.getFaculties(False)

        if faculties:
            for x in faculties:
                y = self.getProgramme(x['url'], x['name'])
                q = q + y

        return q

    # -------------------------------------------------------------------------
    def scrape(self, limit=None):
        return self.getAllBooks(None, limit)

    # -------------------------------------------------------------------------
    def getAllBooks(self, booklists=None, limit=None):
        """ Get all books from all booklists

        @boolists = list of booklist items to scrape (optional)

        Note:
        If booklist parameter is None we will scrape all booklists

        returns a list of dicts containing particulates of a book, for each
        book in each booklist
        """

        if not booklists:
            booklists = self.getAllProgramme()

        books = []
        count = 0
        total = len(booklists)
        #
        # NOTE:
        # remove the if and print statements before
        # deployment.... and this comment!
        #
        for booklist in booklists:
            if limit:
                if len(books) > limit:
                    print('We have more than {0} books, bail out...'.format(
                        limit)
                    )
                    break

            books = books + self.getBooks(booklist)
            count = count + 1
            print('Fetched {0} lists of {1} - books are now {2}'.format(
                count, total, len(books)
            ))

        return books

    # -------------------------------------------------------------------------
    def getBooks(self, booklist):
        """ Get all books of a booklist

        @booklist (dict): a dict containing faculty name, programme name
                          and booklist url

        returns a list of dicts, each containing particulates of a book
        """
        bl = self._getBS(booklist['booklist'])
        cards = bl.select('.products-list .item')

        books = []
        for card in cards:
            book = {}

            # easy stuff...
            heading = card.parent.parent.find_previous_sibling('h3')
            book['course'] = heading.string.strip()
            book['faculty'] = booklist['faculty']
            book['programme'] = booklist['programme']
            book['cover'] = card.select('img')[0]['src']
            book['title'] = card.select('h2')[0].string
            # deal with isk
            price = card.select('.price')[0].string.strip()
            try:
                price = (''.join(self.isk.search(price).groups()))
            except:
                price = "0"

            book['price'] = price
            # other stuff...
            info = card.select('.new_info li')
            for items in info:
                item = items.text.strip().split(":")
                book[self.book[item[0].strip()]] = item[1].strip()
            # collect and move on...
            books.append(book)

        return books

    # -------------------------------------------------------------------------
    def getCurrentSemester(self):
        """ Get the name of the current semester

        Returns a text string containing the name of the current semester
        as used by boksala.is
        """
        month = datetime.now().month
        year = datetime.now().year

        if month < 8:
            month = "vor"
        else:
            month = "haust"

        return month + "-" + str(year)

    # -------------------------------------------------------------------------
    def getProgrammeUrl(self, facultyUrl):
        """ Generate a valid URL
        """
        url = facultyUrl[:facultyUrl.find('.', -7)]
        url = "%s/%s.html" % (url, self.getCurrentSemester())
        return url

    # -------------------------------------------------------------------------
    def _getBS(self, url):
        """ Initalize BeautifulSoup
        """
        r = requests.get(url)

        data = r.content
        # NOTE
        # We have to use html5lib parser for bs4 since the page we are
        # scraping has malformed tag structure, html5lib is more
        # lenient than lxml and python's built in parser
        return BeautifulSoup(data, 'html5lib')
