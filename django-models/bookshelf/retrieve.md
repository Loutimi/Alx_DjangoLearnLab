# Retrieve a single record that matches certain criteria
specific_book = Book.objects.get(title='1984') print(specific_book)