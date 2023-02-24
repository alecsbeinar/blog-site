from django.test import TestCase
from django.urls import reverse


class RedirectTest(TestCase):

    def test_python_redirect(self):
        url = reverse('python_redirect')
        response = self.client.get(url)
        self.assertRedirects(response, 'https://ru.wikipedia.org/wiki/Python', fetch_redirect_response=False)

    def test_setup_redirect(self):
        url = reverse('setup_redirect')
        response = self.client.get(url)
        self.assertRedirects(response, 'https://www.djangoproject.com/', fetch_redirect_response=False)

