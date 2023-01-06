from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)#fields we want in table
    pages = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}, {self.pages} pages long"
