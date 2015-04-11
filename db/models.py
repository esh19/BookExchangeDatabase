from django.db import models

# Create your models here.

class Prototype(models.Model):
    isbn = models.IntegerField(primary_key=True)
    bookName = models.CharField(max_length=100)
    newPrice = models.IntegerField()
    publisher = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=100)
    edition = models.IntegerField()
    year = models.IntegerField()
    course
    faculty
    programme
    cover


class Seller(models.Model):
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)

    sellerName = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=100)

class UsedBooks(models.Model):
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
    
    prototype = models.ForeignKey(Prototype)
    seller = models.ForeignKey(Seller)
    price = models.IntegerField()
    condition = models.CharField(max_length=100)

