import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_home_route(self):
        tester = app.test_client()  # Supprime `self`
        response = tester.get('/status')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
