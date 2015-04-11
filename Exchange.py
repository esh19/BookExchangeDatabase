import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Prototype, UsedBooks, Seller

#UsedBook

def createSale(prototype, seller, condition, price, date):
	return UsedBooks.objects.create(prototype=prototype, seller=seller, condition=condition, price=price, date=date)

def setPrice(UsedBooks,price):
	UsedBooks.price = price
	UsedBooks.save()

def getBookName(UsedBooks):
	return UsedBooks.bookName

def getCondition(UsedBooks):
	return UsedBooks.condition

def getPrice(UsedBooks):
	return UsedBooks.price

def getDate(UsedBooks):
	return UsedBooks.date

def getBooks(UsedBooks):
	return UsedBooks.bookName


#returns UsedBooks by the name (or substring name) of the book
#def searchByTitle(bookName):

#returns UsedBooks by the author (or substring athor) of the book
#def searchByAuthor(authorName):

#returns UsedBooks by the publisher (or substring publisher) of the book
#def searchByPublisher(publisherName):

#returns UsedBooks by a keyword (title, author or publisher)
#def searchByKeyword(keyword):
