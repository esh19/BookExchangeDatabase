from django.db import models
import datetime

class Prototype(models.Model):
    isbn = models.CharField(primary_key=True, max_length=100)
    bookName = models.CharField(max_length=100,default="",null=True)
    newPrice = models.IntegerField(null=True)
    publisher = models.CharField(max_length=100,default="",null=True)
    bookAuthor = models.CharField(max_length=100,default="",null=True)
    edition = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    course = models.CharField(max_length=100,default="",null=True)
    faculty = models.CharField(max_length=100,default="",null=True)
    programme = models.CharField(max_length=100,default="",null=True)
    cover = models.CharField(max_length=100,default="",null=True)


class Seller(models.Model):
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)

    sellerName = models.CharField(max_length=100,default="")
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=100,default="")

class UsedBooks(models.Model):
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)

    
    prototype = models.ForeignKey(Prototype)
    seller = models.ForeignKey(Seller)
    price = models.IntegerField()
    condition = models.CharField(max_length=100,default="")
    date = models.DateField(default=datetime.date.today, null=True)
