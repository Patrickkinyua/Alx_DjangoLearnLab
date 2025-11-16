from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book


# View list of books (requires can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Create book (requires can_create)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published = request.POST.get('published')

        Book.objects.create(title=title, author=author, published=published)
        return render(request, 'bookshelf/success.html', {'msg': 'Book created successfully!'})

    return render(request, 'bookshelf/create_book.html')


# Edit book (requires can_edit)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published = request.POST.get("published")
        book.save()
        return render(request, 'bookshelf/success.html', {'msg': 'Book updated successfully!'})

    return render(request, 'bookshelf/edit_book.html', {'book': book})


# Delete book (requires can_delete)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return render(request, 'bookshelf/success.html', {'msg': 'Book deleted successfully!'})
