import unittest
from app import app


class Tests(unittest.TestCase):
    '''Basic tests for the application'''

    def setUp(self):
        '''Create a test client for the app'''
        self.app = app.test_client()

    def test_200(self):
        '''test_200: a request for / shall return 200 OK'''
        res = self.app.get('/')
        assert res.status == '200 OK'

    def test_404(self):
        '''test_404: a request for null shall return 404 NOT FOUND'''
        res = self.app.get('/null')
        assert res.status == '404 NOT FOUND'


if __name__ == "__main__":
    unittest.main()
