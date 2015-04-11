

class connector():
    """ Database connector class

    Encapsulates callback functions for the database interface (team X2B)
    """

    _booksCallback = None
    # _booksCallback = None

    def __init__(self, books):
        """ Constructor

        @book = callback function to be called to post a single book object
                to the connector
        @books = same as above, now for posting a list of book objects

        """
        if hasattr(books, '__call__'):
            self._booksCallback = books

        # if hasattr(books, '__call__'):
        #     self._booksCallback = books

    # can be deleted - we will only offer the plural version
    def postBook(self, bookDict):
        """ Post a book to the connector

        @bookDict = a single dict object containing all attributes of a book

        Returns true if connector accepts, raises exception on fail
        """
        if not hasattr(self._bookCallback, '__call__'):
            raise Exception('No callback for posting a single book')

        try:
            if not self._bookCallback(bookDict):
                raise Exception('[postBook] Connector returned false')

            return True
        except Exception as error:
            raise Exception(
                '[postBook] Connector failed with {0}'.format(error)
                )

    def postBooks(self, bookList):
        """ Post a list of books to the connector

        @bookList = a list of book dicts each containing all
                    attributes of a book

        Returns true if connector accepts, raises exception on fail
        """
        if not hasattr(self._booksCallback, '__call__'):
            raise Exception('No callback for posting list of books')

        try:
            if not self._booksCallback(bookList):
                raise Exception('[postBooks] Connector returned false')

            return True
        except:
            raise Exception('[postBooks] Connector failed')
