from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
  author = Author.objects.get(name=author_name)
  return Book.objects.filter(author=author)

# List all books in a library
def get_books_in_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.librarian

# # Example Usage (uncomment to test)
# author_books = get_books_by_author("J.R.R. Tolkien")
# library_books = get_books_in_library("Central Library")
# library_librarian = get_librarian_for_library("Central Library")

# # Print results (uncomment to test)
# for book in author_books:
#   print(book)
# for book in library_books:
#   print(book)
# print(library_librarian)