import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Prototype

def create(isbn, bookName, newPrice, publisher, bookAuthor, edition, year):
	return Prototype.objects.create(isbn=isbn, bookName=bookName, newPrice=newPrice, publisher=publisher, bookAuthor=bookAuthor, edition=edition, year=year)

def delete(prototype):
	prototype.delete()
	prototype.save()


def bookExists(isbn):
	if Prototype.objects.filter(isbn=isbn).exists():
		return Prototype.objects.filter(isbn=isbn).values('bookName')
	else: return ('Book does not exist')

def getNewPrice(prototype):
	return prototype.newPrice

def getEdition(prototype):
	return prototype.edition;

def getYear(prototype):
	return prototype.year

def getCourse(prototype):
	return prototype.course


def getAuthor(prototype):
	return prototype.authorName
		

def modifyNewPrice(prototype,newPrice):
	prototype.newPrice = newPrice
	prototype.save()

def modifyCourse(prototype,course):
	prototype.course = course
	prototype.save()
