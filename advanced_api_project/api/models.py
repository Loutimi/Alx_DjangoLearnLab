from django.db import models

# Author model to keep records of all authors
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Book model to keep records of all books
class Book(models.Model):
    title = models.CharField(max_length=300)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
