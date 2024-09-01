from bookshelf.models import Book

Retrieve book
book = Book.objects.get(id=1) print(book)

Output
<Book: 1984>