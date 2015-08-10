""" Run test by checking the status code or if texts appear"""

from project import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure the login page loads correctly via 200
    def test_index(self):
        # creates the test client
        tester = app.test_client(self)
        # calls the login route
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure the text appears on the page
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'*login is case sensitive' in response.data)

# Ensure login behaves correctly given the correct credentials

if __name__ == '__main__':
    unittest.main()
