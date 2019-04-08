import requests

from rest_framework import viewsets
from rest_framework.response import Response

from django.conf import settings

from .services import format_external_data

class BooksViewSet(viewsets.ViewSet):
    """
    ViewSet for listing or retrieving books.
    """

    def list(self, request):
        params = {}
        response = requests.get(
            url=settings.EXTERNAL_API_URL,
            params=request.GET.dict()
        )

        formated_data = format_external_data(response.json())
        data = {
            'status_code': response.status_code,
            'status': 'success',
            'data': formated_data
        }

        return Response(data)
