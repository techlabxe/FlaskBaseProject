import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = False
    TESTING = False

class TestingConfig(BaseConfig):
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

app_configs = {
    'develop' : 'configs.DevelopmentConfig',
    'testing' : 'configs.TestingConfig',
    'production' : 'configs.ProductionConfig',
}
