import unittest
from project import create_app_unittest

class AppUnittests(unittest.TestCase):
    def setUp(self):
        self.app = create_app_unittest()
        self.test_client = self.app.test_client()
        return super().setUp()

    def test_getIndex(self):
        self.assertIsNotNone( self.app )
        response = self.test_client.get('/')
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.data, b'Hello Flask Base application' )

if __name__ == '__main__':
    unittest.main()
