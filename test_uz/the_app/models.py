from pydoc import pager
from pyexpat import model
from statistics import mode
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    page_count = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"

    
class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    book_id = models.IntegerField()