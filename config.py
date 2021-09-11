# -*- coding: utf-8 -*-
# python 3.9.6

import os
import random, string
import sys

class Config(object):
    CSRF_ENABLED = True
    SECRET = 'asdfbashuivdvi!@#$%¨&*(v8sd48vv41vs!H'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEGUG = True
    IP_HOST = 'localhost'
    PORT = 8000
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:samara123@localhost:3306/livro_flask'

class TestingConfig(Config):
    TESTING = True
    DEGUG = True
    IP_HOST = 'localhost'
    PORT = 5000
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT)

class ProductionConfig(Config):
    TESTING = False
    DEGUG = False
    IP_HOST = 'localhost'
    PORT = 8080
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT)

app_config = {
    'development' : DevelopmentConfig(),
    'testing' : TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:ecal4321@localhost:3306/livro_flask'
























