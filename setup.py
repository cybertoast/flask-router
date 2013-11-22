'''
    Flask-Router
    -------------

    Centralized routes management for Flask

'''
import os

from setuptools import setup

module_path = os.path.join(os.path.dirname(__file__), 'flask_router.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version_info__')][0]

__version__ = '.'.join(eval(version_line.split('__version_info__ = ')[-1]))

setup(
    name='Flask-Router',
    version=__version__,
    url='https://github.com/cybertoast/flask-router/',
    license='BSD',
    author='Sundar Raman',
    author_email='cybertoast@gmail.com',
    description='Centralized routes management for Flask.',
    long_description=__doc__,
    py_modules=['flask_router'],
    test_suite='test_router',
    zip_safe=False,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
