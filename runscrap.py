import Prototype
import sys
sys.path.insert(0, './scrap')
import X2A


books = []


def postBooks(lst):
    global books
    books = lst
    Prototype.createFromList(lst)
    return True


def testScraper():
    scraper = X2A.X2A(postBooks)

    scraper.scrape()


testScraper()