import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import UsedBooks
import Prototype, Seller
import django
django.setup()
from itertools import chain

def createSale(prototype, seller, condition, price, date):
	return UsedBooks.objects.create(prototype=prototype, seller=seller, condition=condition, price=price, date=date)

def getAll():
	return UsedBooks.objects.all()

def searchByTitle(title):
	return UsedBooks.objects.filter(prototype=Prototype.searchByTitle(title))

def searchBySeller(sellerName):
	return UsedBooks.objects.filter(seller=Seller.searchByName(sellerName))

def searchByAuthor(author):
	return UsedBooks.objects.filter(prototype=Prototype.searchByAuthor(author))

def searchByIsbn(isbn):
	return UsedBooks.objects.filter(prototype=Prototype.searchByIsbn(isbn))

def searchByField(fieldName):
	return UsedBooks.objects.filter(prototype=Prototype.searchByField(fieldName))

def searchByKeyword(keyword):
	return list(chain(searchByTitle(keyword), searchBySeller(keyword), searchByAuthor(keyword), searchByIsbn(keyword), searchByField(keyword)))

def getPrototype(UsedBooks):
	return UsedBooks.prototype

def getSeller(UsedBooks):
	return UsedBooks.seller

def setPrice(UsedBooks,price):
	UsedBooks.price = price
	UsedBooks.save()

def getCondition(UsedBooks):
	return UsedBooks.condition

def getPrice(UsedBooks):
	return UsedBooks.price

def getDate(UsedBooks):
	return UsedBooks.date

def getBooks(UsedBooks):
	return UsedBooks.bookName