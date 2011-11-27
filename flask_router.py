# -*- coding: utf-8 -*-

from __future__ import absolute_import
from flask import _request_ctx_stack

from werkzeug import import_string, cached_property
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

class LazyView(object):
    """
    Load the controllers/route-handlers lazily so that we can 
    have centralized routing
    """

    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)

class Router(object):
    # Move all the routes to Urls.py, but ensure it's after the LazyView

    def __init__(self, app=None, routes=None):
        if routes is not None:
            self.routes = routes
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None
            
    def init_app(self, app, routes=None):
        self.app = app
        if routes is not None:
            self.routes = routes
        # self.app.teardown_request(self.teardown_request)
        # self.app.before_request(self.before_request)

        # Set up the Regex Converter
        self.app.url_map.converters['regex'] = RegexConverter
        # Finally load the routes
        self._load_routes()
        
    def _load_routes(self):
        '''
        Load the routes, but with a default of GET and POST for evry call,
        and with the endpoint being the full controller so that the name is unique
        The resaon for the endpoint is that all controllers might use the same
        function name (eg. controller.index)
        '''
        for item in self.routes:
            route = item[0]
            controller = item[1]
            opts = {}
            if len(item) == 3:
                opts = item[2]
            if opts.get('endpoint') is None:
                # mitsuhiko
                # i would not use a dot since that separates blueprint from endpoit
                # but feel free to use ":" or "/"
                # eg: controller_name:callback
                opts['endpoint'] = controller.replace('.',':')
            if opts.get('methods') is None:
                opts['methods'] = ['GET', 'POST']
            if opts.get('strict_slashes') is None:
                opts['strict_slashes'] = False
                    
            self.url(route, controller, **opts)
        
    def url(self, url_rule, import_name, **options):
        # view = LazyView('yourapplication.' + import_name)
        view = LazyView(self.app.name + '.' + import_name)
        self.app.add_url_rule(url_rule, view_func=view, **options)

    def teardown_request(self):
        pass
    
    def before_request(self):
        pass
