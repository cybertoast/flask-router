"""
Flask-Router
-------------

Provides for centralized routing with lazy-loaded targets
"""
from setuptools import setup

setup(
    name='Flask-Router',
    version='0.5',
    # url='http://github.com/cybertoast/flask-router
    
    license='BSD',
    author='Sundar Raman',
    author_email='cybertoast@gmail.com',
    
    description='Centralized Routes',
    long_description=__doc__,
    keywords=['flask', 'route', 'url'],
    
    py_modules=['flask_router'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_router'],
    zip_safe=False,
    
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
