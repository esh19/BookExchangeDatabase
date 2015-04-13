import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Seller
import django
django.setup()

def createSeller(sellerName, phoneNumber, email):
	return Seller.objects.create(sellerName=sellerName, phoneNumber=phoneNumber, email=email)

def getSellerById(identity):
	return Seller.objects.filter(id=identity)

def getAll():
	return Seller.objects.all()
def searchByName(name):
	return Seller.objects.filter(sellerName__icontains = name)

def getId(Seller):
	return Seller.id

def getEmail(Seller):
	return Seller.email

def getSellerName(seller):
	return seller.sellerName

def getNumber(seller):
	return seller.phoneNumber

def getBooks(seller): 
  	return UsedBooks.objects.filter(seller=seller)

def setNumber(seller,phoneNumber):
 	seller.phoneNumber = phoneNumber
 	seller.save()

def setEmail(seller,email):
 	seller.email = email
 	seller.save()
