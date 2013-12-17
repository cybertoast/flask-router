# Using flask-router

```
from flask.ext.router import Router
from urls import urls
```

A simple way of making this work, without relying on installing
the extension "officially" is to do something like:

```
cd path-to-project # eg. cd myproj
mkdir extensions
```

Put flask_router.py into the extensions folder so that your project structure looks like:

    main.py
    extensions
        flask_router.py
    myproj
        __init__.py

In your create_app() add ...

```
if os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extensions'))):
    # if settings.get('FLASK').get('local_extensions') is True:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extensions')))
```

# CAVEATS and Gotchas

Note that in order to avoid blueprint name confusion, the endpoint syntax in 
flask_router uses colon (:) instead of period (.). 
So the syntax for url_for() needs to replace the separator as follows:
eg. `url_for("views.api.index")` becomes `url_for("views:api:index")`
See notes in flask_router for more details

If you do NOT replace the colons you will get the following error:
    `BuildError: ('views.api.index', {}, None)`
since the endpoint is not found.

