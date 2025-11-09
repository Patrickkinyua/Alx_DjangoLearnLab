# File: retrieve.md

from bookshelf.models import Book
Book.objects.all()  # Expected Output:

Book.objects.get(title="1984")


 <QuerySet [<Book: 1984>]>
