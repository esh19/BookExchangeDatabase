import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Prototype, UsedBooks, Seller
import django
django.setup()

def createSeller(sellerName, phoneNumber, email):
	return Seller.objects.create(sellerName=sellerName, phoneNumber=phoneNumber, email=email)

def getEmail(Seller):
	return Seller.email

def getSellerName(seller):
	return seller.sellerName

def getNumber(seller):
	return seller.phoneNumber

def getBooks(seller): 
  	return UsedBooks.objects.filter(seller=seller)

def modifyNumber(seller,phoneNumber):
 	seller.phoneNumber = phoneNumber
 	seller.save()

def modifyEmail(seller,email):
 	seller.email = email
 	seller.save()