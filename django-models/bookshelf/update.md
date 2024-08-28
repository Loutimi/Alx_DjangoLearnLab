from bookshelf.models import Book

Retrieve book
book = Book.objects.get(id=1)

Update the title of the retrieved book
book.title = "Nineteen Eighty-Four" book.save() print(book)

Output
<Book: Nineteen Eighty-Four>