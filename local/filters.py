from django_filters import rest_framework as filters

from .models import Book


class BookFilter(filters.FilterSet):
    date = filters.NumberFilter(field_name='release_date', lookup_expr='year')

    class Meta:
        model = Book
        fields = ('name', 'country', 'publisher', 'date')
