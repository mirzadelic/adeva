import requests

from dateutil.parser import parse

from rest_framework import viewsets
from rest_framework.response import Response

from django.conf import settings


class BooksViewSet(viewsets.ViewSet):
    """
    ViewSet for listing or retrieving books.
    """
    @staticmethod
    def format_external_data(data):
        return [
            {
                'name': item['name'],
                'isbn': item['isbn'],
                'authors': item['authors'],
                'number_of_pages': item['numberOfPages'],
                'publisher': item['publisher'],
                'country': item['country'],
                'release_date': parse(item['released']).strftime("%Y-%m-%d"),

            } for item in data
        ]

    def list(self, request):
        try:
            response = requests.get(
                url=settings.EXTERNAL_API_URL,
                params=request.GET.dict()
            )
            formated_data = self.format_external_data(response.json())
            data = {
                'status_code': response.status_code,
                'status': 'success',
                'data': formated_data
            }
        except Exception as e:
            data = {
                'status': 'error',
                'message': 'Error from external server'
            }

        return Response(data)
