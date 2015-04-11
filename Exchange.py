import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Prototype, UsedBooks, Seller

#UsedBook

def createSale(prototype, seller, condition, price, date):
	return UsedBooks.objects.create(prototype=prototype, seller=seller, condition=condition, price=price, date=date)

def modifyPrice(UsedBooks,price):
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