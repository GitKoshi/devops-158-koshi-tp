import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        print("Test 1 réussi : Code HTTP 200")

    def test_response_contains_hello(self):
        response = self.app.get('/')
        self.assertIn('Hello', response.data.decode('utf-8'))
        print("Test 2 réussi : La réponse contient 'Hello'")

    def test_response_not_empty(self):
        response = self.app.get('/')
        self.assertTrue(len(response.data) > 0)
        print("Test 3 réussi : La réponse n'est pas vide")

    def test_response_type_is_string(self):
        response = self.app.get('/')
        self.assertIsInstance(response.data.decode('utf-8'), str)
        print("Test 4 réussi : La réponse est une chaîne de caractères")

if __name__ == '__main__':
    unittest.main()
