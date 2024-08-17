# Retrieve the record that you want to delete
specific_book = Book.objects.get(title='1984') print(specific_book)

# Delete the record
specific_book.delete()