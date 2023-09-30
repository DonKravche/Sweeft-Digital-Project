from django_filters import rest_framework as filters

from book_management.models import Book


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    genre = filters.CharFilter(field_name='genre__name', lookup_expr='icontains')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author', 'genre']