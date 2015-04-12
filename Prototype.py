import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Prototype
import django
django.setup()

def create(isbn, bookName, newPrice, publisher, bookAuthor, edition, year, course, faculty, programme, cover):
	if bookExists(isbn): return False
	return Prototype.objects.create(isbn=isbn, bookName=bookName, newPrice=newPrice, publisher=publisher, bookAuthor=bookAuthor, edition=edition, year=year, course=course, faculty=faculty, programme=programme, cover=cover)

def createFromList(lst):
	attributes = ['isbn', 'title', 'price', 'publisher', 'author', 'edition', 'publishing_year', 'course', 'faculty', 'programme', 'cover']

	for i in range(len(lst)):

		for j in range(len(attributes)):
			if not(attributes[j] in lst[i].keys()): lst[i][attributes[j]] = None
		if (isinstance(attributes[2],str)): lst[i][attributes[2]] = None #price
		if (isinstance(attributes[5],str)): lst[i][attributes[5]] = None #edition
		if (isinstance(attributes[7],str)): lst[i][attributes[7]] = None #year
		create(lst[i]['isbn'], lst[i]['title'], lst[i]['price'], lst[i]['publisher'], lst[i]['author'], lst[i]['edition'], lst[i]['publishing_year'], lst[i]['course'], lst[i]['faculty'], lst[i]['programme'], lst[i]['cover'])

def delete(prototype):
	prototype.delete()
	prototype.save()

def bookExists(isbn):
	return Prototype.objects.filter(isbn=isbn).exists()

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