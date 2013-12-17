Flask-Router
=============

.. module:: flask_router

Router is a Flask extention to manage all routes in a single file, 
rather than define them on each view.


.. _Router: http://github.com/cybertoast/flask-router
.. _Flask: http://flask.pocoo.org/


Installation
------------
Install the extension with one of the following commands::

    $ easy_install flask-router

or alternatively if you have pip installed::

    $ pip install flask-router


Usage
-----

<put in usage text>

.. code-block:: python
    
    import Flask
    from flask.ext.router import Router
    # Import the file that contains all the routes
    #   This is simply a python file
    from urls import urls
    router = Router(app, urls)

The routes file (urls, in the example above) contains all your routes
in any format you like. It's just a python file, so you can separate
concerns as you want, and the only requirement is that you return a 
list of tuples in the following format:

    [ ( route, view_function, methods ), (), () ...]

The example below attempts to be complete.

    urls = [
        #-----------------------------------
        ('/', 'views.index', {'methods':['GET']}),
        ('/api', 'views.api.index', {'methods':['GET']}),
        ('/api/help', 'views.api.help', {'methods': ['GET']}),

        # RESTful resources
        ('/bs/messages', 'views.api.beamsign.show', {'methods': ['GET']}),
        ('/bs/messages/new', 'views.api.beamsign.create', {'methods': ['PUT']}),
        # You can also alias resources, so that different names 
        # go to the same function
        ('/bs/messages/add', 'views.api.beamsign.create', {'methods': ['PUT']}),

        ('/bs/messages/update', 'views.api.beamsign.update', {'methods': ['POST', 'PUT']}),

        ('/bs/messages/delete', 'views.api.beamsign.delete', {'methods': ['POST']}),
        ('/bs/messages', 'views.api.beamsign.delete', {'methods': ['DELETE']})
    ]
     
Note that you can still continue to define your routes in your view
function using the standard Flask pattern, and this will still be recognized.

