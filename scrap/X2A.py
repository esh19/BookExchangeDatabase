# -*- coding: utf-8 -*-

# imports
import connector
import scraper


class X2A():
    """ Boksala.is scraper application
    """
    database = None     # handle for the connector class
    scraper = None      # handle for the scraper class

    def __init__(self, booksCallback=None):
        self.database = connector.connector(booksCallback)
        self.scraper = scraper.scraper()

    def scrape(self, limit=None):
        books = self.scraper.scrape(limit)
        self.database.postBooks(books)
