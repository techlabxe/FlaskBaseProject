import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    MONGO_HOST = '192.168.243.148'
    MONGO_DBNAME = 'mymongo'

class DevelopmentConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    MONGO_DBNAME = 'develop'

class TestingConfig(BaseConfig):
    TESTING = True
    MONGO_DBNAME = 'tests'
    

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

app_configs = {
    'develop' : 'configs.DevelopmentConfig',
    'testing' : 'configs.TestingConfig',
    'production' : 'configs.ProductionConfig',
}
