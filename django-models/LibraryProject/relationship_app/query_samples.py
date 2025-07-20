from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# List all books in a library
library = Library.objects.get(name="Central Library")
print(library.books.all())

# Retrieve the librarian for a library
print(Librarian.objects.get(library=library))
