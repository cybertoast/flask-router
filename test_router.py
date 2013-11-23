from __future__ import with_statement

import sys
import unittest

from flask import Flask
from flask_router import Router

if sys.version_info[0] < 3:
    b = lambda s: s
else:
    b = lambda s: s.encode('utf-8')

# The main functions have to be defined outside 
#   the RouterTestCase class, since their context
#   would not be visible otherwise
def show(id=None):
    if not id:
        return 'show'
    else:
        return 'show %s' % id

def create():
    return 'create'

def update():
    return 'update'

def regex(action=None):
    return 'regex %s' % action


class RouterTestCase(unittest.TestCase):

    def setUp(self):

        routes = [ 
            # u'route', 'controller.method', {options:value})
            ('/', 'show', {'methods':['GET']}),
            ('/<id>', 'show', {'methods':['GET']}),
            ('/new', 'create', {'methods':['POST']}),
            ('/update', 'update', {'methods':['PUT']}),
            ('/regex/<regex("load|get"):action>', 'regex', {'methods': ['GET']})

            # We'll define the DELETE method in the view function decorator
            # ('/', 'delete', {'methods':['DELETE']})
        ]

        app = Flask(__name__)
        app.debug = True
        app.secret_key = '1234'
        self.app = app

        Router(app, routes)

        @app.route('/delete', methods=['DELETE'])
        def delete():
            return 'delete'

    def test_retrieve(self):
        with self.app.test_client() as client:
            rv  = client.get('/')
            self.assertEqual(rv.status_code, 200)
            self.assertEqual(rv.data, 'show')

    def test_create(self):
        with self.app.test_client() as client:
            rv  = client.post('/new')
            self.assertEqual(rv.status_code, 200)
            self.assertEqual(rv.data, 'create')

    def test_update(self):
        with self.app.test_client() as client:
            rv  = client.put('/update')
            self.assertEqual(rv.status_code, 200)
            self.assertEqual(rv.data, 'update')

    def test_update(self):
        with self.app.test_client() as client:
            rv  = client.delete('/delete')
            self.assertEqual(rv.status_code, 200)
            self.assertEqual(rv.data, 'delete')

    def test_regex_routes(self):
        with self.app.test_client() as client:
            rv = client.get('/regex/load')
            self.assertEqual(rv.data, 'regex load')

    def test_param_routes(self):
        with self.app.test_client() as client:
            rv = client.get('/some-id')
            self.assertEqual(rv.data, 'show some-id')

    def test_failures(self):
        with self.app.test_client() as client:
            rv = client.get('/regex/nothing')
            self.assertEqual(rv.status_code, 404)
            rv = client.put('/')
            self.assertEqual(rv.status_code, 405)
            rv = client.post('/update')
            self.assertEqual(rv.status_code, 405)
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RouterTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
