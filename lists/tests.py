from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_home_page_return_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf-8')
        self.assertTemplateUsed(response, 'home.html')
