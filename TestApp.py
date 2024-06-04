import unittest
from WebApp import app

class HelloWorldTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World, im here!', response.data)

if __name__ == '__main__':
    unittest.main()
