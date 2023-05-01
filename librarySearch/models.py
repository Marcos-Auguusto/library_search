from django.db import models

class Book(models.Model):
    book_title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    book_cover = models.ImageField()
    about = models.TextField()
    isbn = models.IntegerField()
    number_copies = models.DecimalField()
    rented = models.BooleanField(default=True)
    