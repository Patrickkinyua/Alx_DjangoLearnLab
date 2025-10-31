# File: CRUD_operations.md

## CREATE
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected Output: <Book: 1984>

## RETRIEVE
from bookshelf.models import Book
Book.objects.all()  # Expected Output: <QuerySet [<Book: 1984>]>

## UPDATE
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book  # Expected Output: <Book: Nineteen Eighty-Four>

## DELETE
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()  # Expected Output: (1, {'bookshelf.Book': 1})
Book.objects.all()  # Expected Output: <QuerySet []>
