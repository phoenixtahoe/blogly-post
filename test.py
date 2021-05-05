from unittest import TestCase
from app import app

class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_user_form(self):
        with self.client:
            response = self.client.get('/users/new')
            self.assertIn(b'First Name', response.data)
            self.assertIn(b'Last Name', response.data)
            self.assertIn(b'Image URL', response.data)
    
    def test_post_form(self):
        with self.client:
            response = self.client.get('/users/3/posts/new')
            self.assertIn(b'Title', response.data)
            self.assertIn(b'Post Content', response.data)