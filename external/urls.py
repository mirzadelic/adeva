from django.urls import path, include
from rest_framework import routers

from .views import BooksViewSet


router = routers.SimpleRouter()
router.register('books', BooksViewSet, base_name='books')

app_name = 'external'
urlpatterns = [
    path('', include(router.urls)),
]
