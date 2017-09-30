import unittest
from project import create_app_unittest

class AppAPIUnittests(unittest.TestCase):
    def setUp(self):
        self.app = create_app_unittest()
        self.test_client = self.app.test_client()
        return super().setUp()

    def test_getAPIindex(self):
        self.assertIsNotNone( self.app )
        response = self.test_client.get('/api/')
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.data, b'WebAPIindex' )

if __name__ == '__main__':
    unittest.main()
