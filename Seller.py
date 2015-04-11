import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookExchange.settings")
from db.models import Prototype, UsedBooks, Seller


def createSeller( sellerName, phoneNumber, email):
	return Seller.objects.create(sellerName=sellerName, phoneNumber=phoneNumber, email=email)

def getEmail(seller):
	return seller.email

def getSellerName(seller):
	return seller.sellerName

def getNumber(seller):
	return seller.phoneNUmber

# def getBooks(seller): 
# 	return Seller.objects.filter(seller=seller).values('UsedBooks.bookName')	

def modifyNumber(seller,phoneNumber):
	return seller.phoneNumber = phoneNumber

def modifyEmail(seller,email):
	return seller.email = email