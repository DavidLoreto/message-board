from django.test import TestCase
from django.urls import reverse

from .models import Message

class PostModelTest(TestCase):

    def setUp(self):
        Message.objects.create(text='Just a test')

    def test_text_content(self):
        post = Message.objects.get(id=1)
        expected_object_name = f'{post.text}'
        
        self.assertEqual(expected_object_name, 'Just a test')


class HomePageTest(TestCase):

    def setUp(self):
        Message.objects.create(text='Just another test')

    def test_home_page_by_url(self):
        request = self.client.get('/')
        response_code = 200

        self.assertEqual(request.status_code, response_code)

    def test_home_page_by_name(self):
        request = self.client.get(reverse('home'))
        response_code = 200

        self.assertEqual(request.status_code, response_code)

    def test_home_page_template(self):
        request = self.client.get('/')
        response_code = 200

        self.assertEqual(request.status_code, response_code)
        self.assertTemplateUsed(request, 'home.html')

