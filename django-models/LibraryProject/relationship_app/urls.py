from django.urls import path
from .views import list_books  # ✅ Needed for check
from .views import LibraryDetailView  # Also needed if you're linking class-based view

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
