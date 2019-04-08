from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter


class BooksViewSet(ModelViewSet):
    """
    ViewSet for CRUD operations for books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_class = BookFilter

    def response_format(self, response, name=None):
        r = {
            'status_code': response.status_code,
            'status': 'success',
            'data': response.data
        }
        if self.action in ['update', 'partial_update']:
            r['message'] = 'The book %s was updated successfully' % response.data['name']
        elif self.action == 'destroy':
            r['message'] = 'The book %s was deleted successfully' % name
            r['data'] = []
        elif self.action == 'create':
            r['data'] = {
                'book': response.data
            }

        return r

    def list(self, request, *args, **kwargs):
        r = super(BooksViewSet, self).list(request, *args, **kwargs)
        return Response(self.response_format(r))

    def create(self, request, *args, **kwargs):
        r = super(BooksViewSet, self).create(request, *args, **kwargs)
        return Response(self.response_format(r))

    def retrieve(self, request, *args, **kwargs):
        r = super(BooksViewSet, self).retrieve(request, *args, **kwargs)
        return Response(self.response_format(r))

    def update(self, request, *args, **kwargs):
        r = super(BooksViewSet, self).update(request, *args, **kwargs)
        return Response(self.response_format(r))

    def update(self, request, *args, **kwargs):
        r = super(BooksViewSet, self).update(request, *args, **kwargs)
        return Response(self.response_format(r))

    def destroy(self, request, *args, **kwargs):
        name = self.get_object().name
        r = super(BooksViewSet, self).destroy(request, *args, **kwargs)
        return Response(self.response_format(r, name))
