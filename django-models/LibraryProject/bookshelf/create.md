from bookshelf.models import Book
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) print(new_book)

Save The Instance to The
new_book.save()

Output
<Book: 1984>