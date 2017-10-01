import unittest
from pymongo import MongoClient
from project import create_app_unittest

class DBAcessTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app_unittest()
        self.test_client = self.app.test_client()
        mongo = self.app.mongo
        self.initDB()
        return super().setUp()

    def tearDown(self):
        self.exitDB()
        return super().tearDown()

    def initDB(self):
        self.DB_NAME = self.app.config['MONGO_DBNAME']
        client = MongoClient( host = self.app.config['MONGO_HOST'] )
        client.drop_database( self.DB_NAME )
        self.mongo_client = client

    def exitDB(self):
        client = self.mongo_client
        client.drop_database( self.DB_NAME )


    def testDatabase(self):
        with self.app.app_context():
            mongo = self.app.mongo
            self.assertIsNotNone( mongo )
            mongo.db.dummy.insert( 
                { '_id' : '0123', 'data' : 'hello,world'}
            )
            result = mongo.db.dummy.find_one( { '_id' : '0123' } )
            print(result)
            self.assertEqual( result['data'], 'hello,world' )


if __name__ == '__main__':
    unittest.main()
