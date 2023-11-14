import unittest
from app import app


class TestQuadraticFunction(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_quadratic_function(self):
        data = {
            'a': '1',
            'b': '4',
            'c': '4'
        }
        response = self.app.post('/quadratic', data=data, follow_redirects=True)
        html = response.data.decode('utf-8')

        self.assertIn('Первый корень:', html)
        self.assertIn('Второй корень:', html)


if __name__ == '__main__':
    unittest.main()
