from __future__ import with_statement

import sys
import unittest

from flask import Flask
from flask_router import Router

if sys.version_info[0] < 3:
    b = lambda s: s
else:
    b = lambda s: s.encode('utf-8')

# Define a few dummy routes
routes = [ 
     # u'route', 'controller.method', {options:value})
     ('/', 'show', {'methods':['GET']}),
     ('/new', 'create', {'methods':['POST']}),
     ('/update', 'update', {'methods':['PUT']})

     # We'll define the DELETE method in the view function decorator
     # ('/', 'delete', {'methods':['DELETE']})
]

class RouterTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.debug = True
        app.secret_key = '1234'
        self.app = app

        Router(app, routes)

        def show():
            return 'show'

        def create():
            return 'create'

        def update():
            return 'update'

        @app.route('/delete', methods=['DELETE'])
        def delete():
            return 'delete'

    def test_ensure_routes(self):
        pass

    def test_https_good_referer(self):
        with self.app.test_client() as client:
            rv  = client.get('/')
            self.assertEqual(rv.content, 'show')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RouterTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
