import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Prototype

def create(isbn, bookName, newPrice, publisher, bookAuthor, edition, year, course, faculty, programme, cover):
	return Prototype.objects.create(isbn=isbn, bookName=bookName, newPrice=newPrice, publisher=publisher, bookAuthor=bookAuthor, edition=edition, year=year, course=course, faculty=faculty, programme=programme, cover=cover)

def createFromList(lst):
	for i in range(len(lst)):
		create(lst[i]['isbn'], lst[i]['title'], lst[i]['price'], lst[i]['publisher'], lst[i]['author'], lst[i]['edition'], lst[i]['publishing_year'], lst[i]['course'], lst[i]['faculty'], lst[i]['programme'], lst[i]['cover'])

def delete(prototype):
	prototype.delete()
	prototype.save()


def bookExists(isbn):
	if Prototype.objects.filter(isbn=isbn).exists():
		return Prototype.objects.filter(isbn=isbn).values('bookName')
	else: return ('Book does not exist')

def getIsbn(prototype):
	return prototype.isbn

def getTitle(prototype):
	return prototype.bookName

def getPublisher(prototype):
	return prototype.publisher

def getAuthor(prototype):
	return prototype.bookAuthor

def getPrice(prototype):
	return prototype.newPrice

def getEdition(prototype):
	return prototype.edition

def getYear(prototype):
	return prototype.year

def getCourse(prototype):
	return prototype.course


def getFaculty(prototype):
	return prototype.faculty

def getProgramme(prototype):
	return prototype.programme

def getCover(prototype):
	return prototype.cover