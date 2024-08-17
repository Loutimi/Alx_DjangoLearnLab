# Retrieve the record that you want to update
specific_book = Book.objects.get(title='1984') print(specific_book)

# Update fields
specific_book.title = "Nineteen Eighty-Four" 
specific_book.year = 1949

# Save changes to the database
specific_book.save()   