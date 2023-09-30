from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('authors/', views.AuthorCreate.as_view(), name='author-create'),
    path('authors/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),
    path('genres/', views.GenreCreate.as_view(), name='genre-create'),
    path('genres/<int:pk>/', views.GenreDelete.as_view(), name='genre-delete'),
    path('books/<int:book_id>/express-interest/', views.BookInterestView.as_view(), name='express-interest'),
    path('books/<int:book_id>/transfer/', views.BookTransferView.as_view(), name='transfer-book'),
    # Add more URLs for other API views as needed
]
