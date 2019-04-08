from django.urls import reverse

from rest_framework.test import APIClient, APITestCase

from .models import Book


class LocalAPITests(APITestCase):

    def setUp(self):
        books = [
            {
                'name': 'A Game of Thrones',
                'isbn': '978-0553103540',
                'authors': [
                    'George R. R. Martin'
                ],
                'number_of_pages': 694,
                'publisher': 'Bantam Books',
                'country': 'United States',
                'release_date': '1996-08-01'
            }, {
                'name': 'A Clash of Kings',
                'isbn': '978-0553108033',
                'authors': [
                    'George R. R. Martin'
                ],
                'number_of_pages': 768,
                'publisher': 'Bantam Books',
                'country': 'United States',
                'release_date': '1999-02-02'
            }
        ]
        Book.objects.bulk_create([Book(**book) for book in books])

        self.client = APIClient()

    def test__api__list(self):
        """
        List all books from local API
        """

        url = reverse('api:local:books-list')
        response = self.client.get(url)

        self.assertListEqual(
            sorted(['status', 'status_code', 'data']),
            sorted(list(response.json().keys()))
        )

        self.assertEqual(response.data['status_code'], 200)
        self.assertEqual(response.data['status'], 'success')

        if len(response.data['data']) > 0:
            keys = sorted(list(response.data['data'][0].keys()))
            expected_keys = sorted([
                'id',
                'name',
                'isbn',
                'authors',
                'number_of_pages',
                'publisher',
                'country',
                'release_date'
            ])
            self.assertListEqual(keys, expected_keys)

            for book in response.data['data']:
                b = Book.objects.get(pk=book['id'])
                self.assertEqual(b.name, book['name'])

    def test__api__create(self):
        """
        POST request to local API
        """

        new_book_name = 'A Third Book'
        data = {
            'name': new_book_name,
            'isbn': '978-0553103540',
            'authors': [
                'George R. R. Martin'
            ],
            'number_of_pages': 694,
            'publisher': 'Bantam Books',
            'country': 'United States',
            'release_date': '1996-08-01'
        }
        url = reverse('api:local:books-list')
        response = self.client.post(url, data=data)

        self.assertListEqual(
            sorted(['status', 'status_code', 'data']),
            sorted(list(response.json().keys()))
        )

        self.assertEqual(response.data['status_code'], 201)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['book']['name'], new_book_name)
        self.assertTrue(Book.objects.filter(name=new_book_name).exists())

    def test__api__update(self):
        """
        PUT request to local API
        """

        book = Book.objects.first()

        new_book_name = 'A Third Book'
        new_book_isbn = '123456'
        data = {
            'name': new_book_name,
            'isbn': new_book_isbn,
            'authors': [
                'George R. R. Martin'
            ],
            'number_of_pages': 694,
            'publisher': 'Bantam Books',
            'country': 'United States',
            'release_date': '1996-08-01'
        }
        url = reverse('api:local:books-detail', kwargs={'pk': book.pk})
        response = self.client.put(url, data=data)

        self.assertListEqual(
            sorted(['status', 'status_code', 'message', 'data']),
            sorted(list(response.json().keys()))
        )

        self.assertEqual(response.data['status_code'], 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(
            response.data['message'],
            'The book %s was updated successfully' % response.data['data']['name']
        )
        self.assertEqual(response.data['data']['name'], new_book_name)
        self.assertEqual(response.data['data']['isbn'], new_book_isbn)

        book = Book.objects.get(name=new_book_name)
        self.assertEqual(book.name, new_book_name)
        self.assertEqual(book.isbn, new_book_isbn)

    def test__api__detail(self):
        """
        Detail GET request with pk to local API
        """

        book = Book.objects.first()

        url = reverse('api:local:books-detail', kwargs={'pk': book.pk})
        response = self.client.get(url)

        self.assertListEqual(
            sorted(['status', 'status_code', 'data']),
            sorted(list(response.json().keys()))
        )

        self.assertEqual(response.data['status_code'], 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['data']['name'], book.name)

    def test__api__delete(self):
        """
        DELETE request with pk to local API
        """

        book = Book.objects.first()

        url = reverse('api:local:books-detail', kwargs={'pk': book.pk})
        response = self.client.delete(url)

        self.assertListEqual(
            sorted(['status', 'status_code', 'message', 'data']),
            sorted(list(response.json().keys()))
        )

        self.assertEqual(response.data['status_code'], 204)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(
            response.data['message'],
            'The book %s was deleted successfully' % book.name
        )
        self.assertEqual(len(response.data['data']), 0)
        self.assertFalse(Book.objects.filter(name=book.name).exists())
