new_book =  Book.objects.create(title="1984", author="George Orwell", year=1949)
# Save the instance to the database
new_book.save()