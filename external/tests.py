from django.urls import reverse

from rest_framework.test import APIClient, APITestCase


class ExternalAPITests(APITestCase):

    def setUp(self):
        self.url = reverse('api:external:books-list')
        self.client = APIClient()

    def test__api__list(self):
        """
        List all books from external API
        """

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            sorted(['status', 'status_code', 'data']),
            sorted(list(response.json().keys()))
        )

        self.assertEqual(response.data['status_code'], 200)
        self.assertEqual(response.data['status'], 'success')

        if len(response.data['data']) > 0:
            keys = sorted(list(response.data['data'][0].keys()))
            expected_keys = sorted([
                'name',
                'isbn',
                'authors',
                'number_of_pages',
                'publisher',
                'country',
                'release_date'
            ])
            self.assertListEqual(keys, expected_keys)

    def test__api__list__with_filter(self):
        """
        List books with name `A Game of Thrones` from external API
        """
        search_text = 'A Game of Thrones'
        response = self.client.get(
            self.url, {'name': search_text})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['name'], search_text)

