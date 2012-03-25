"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

from models import Author


class LinkedModelChoiceFieldTest(TestCase):

    URL = '/'

    def test_html_output(self):
        client = Client()
        response = client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        choices = (
            '<option value="" class="static">---------</option>',
            '<option value="1" class="sub_1">La Fortune des Rougon</option>',
            '<option value="2" class="sub_1">La Curee</option>',
            '<option value="3" class="sub_1">Le Ventre de Paris</option>',
            '<option value="4" class="sub_2">Le Rouge et le Noir</option>',
            '<option value="5" class="sub_2">La Chartreuse de Parme</option>',
        )
        for choice in choices:
            self.assertContains(response, choice)

    def test_submit_valid_form(self):
        client = Client()
        AUTHOR_ID = 1
        BOOK_ID = 1

        # Sanity check, author and book should match
        author = Author.objects.get(id=AUTHOR_ID)
        self.assertTrue(author.books.filter(id=BOOK_ID).exists())

        # Now test the form submission
        response = client.post(self.URL, {
            'author': AUTHOR_ID,
            'book': BOOK_ID,
        })
        self.assertEqual(response.status_code, 302)

    def test_non_consistent_choices(self):
        client = Client()
        AUTHOR_ID = 1
        BOOK_ID = 4

        # Sanity check, author and book don't match
        author = Author.objects.get(id=AUTHOR_ID)
        self.assertFalse(author.books.filter(id=BOOK_ID).exists())

        # Now see if that works
        response = client.post(self.URL, {
            'author': AUTHOR_ID,
            'book': BOOK_ID,
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'book',
            'Value does not match author value.')


class LinkedModelMultipleChoiceFieldTest(TestCase):

    URL = '/2/'

    def test_html_output(self):
        client = Client()
        response = client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        choices = (
            '<option value="" class="static">---------</option>',
            '<option value="1" class="sub_1">La Fortune des Rougon</option>',
            '<option value="2" class="sub_1">La Curee</option>',
            '<option value="3" class="sub_1">Le Ventre de Paris</option>',
            '<option value="4" class="sub_2">Le Rouge et le Noir</option>',
            '<option value="5" class="sub_2">La Chartreuse de Parme</option>',
        )
        for choice in choices:
            self.assertContains(response, choice)

    def test_submit_valid_form(self):
        client = Client()
        AUTHOR_ID = 1
        BOOK_ID = 1

        # Sanity check, author and book should match
        author = Author.objects.get(id=AUTHOR_ID)
        self.assertTrue(author.books.filter(id=BOOK_ID).exists())

        # Now test the form submission
        response = client.post(self.URL, {
            'author': AUTHOR_ID,
            'book': BOOK_ID,
        })
        self.assertEqual(response.status_code, 302)

    def test_non_consistent_choices(self):
        client = Client()
        AUTHOR_ID = 1
        BOOK_ID = 4

        # Sanity check, author and book don't match
        author = Author.objects.get(id=AUTHOR_ID)
        self.assertFalse(author.books.filter(id=BOOK_ID).exists())

        # Now see if that works
        response = client.post(self.URL, {
            'author': AUTHOR_ID,
            'book': BOOK_ID,
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'book',
            'Select a valid choice. %i is not one of the available choices.' % BOOK_ID)
