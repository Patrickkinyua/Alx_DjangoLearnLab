from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import ExampleForm, SearchForm
from .models import Book


# -----------------------------
# Example Form View (REQUIRED)
# -----------------------------
@csrf_protect
def example_form_view(request):
    """
    Displays and processes ExampleForm.
    Demonstrates CSRF protection and safe user input handling.
    """

    if request.method == "POST":
        form = ExampleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            return render(
                request,
                "bookshelf/form_example.html",
                {"form": form, "success": True, "title": title}
            )

    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})
    

# -----------------------------
# Secure Book List with Search
# -----------------------------
@csrf_protect
def book_list(request):
    """
    Shows a secure list of books.
    Uses Django ORM to prevent SQL injection.
    """

    books = Book.objects.all()  
    query = None

    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            query = form.cleaned_data["query"]

            # ORM prevents SQL injection
            books = books.filter(title__icontains=query)

    else:
        form = SearchForm()

    return render(
        request,
        "bookshelf/book_list.html",
        {"books": books, "form": form, "query": query}
    )
