from bookshelf.models import Book

Retrieve the record that you want to delete
book = Book.objects.get(title='1984') print(book)

Delete the record
book.delete()