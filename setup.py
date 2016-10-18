#! /usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
import sys

# python2 and python3 support
try:
    reload
except NameError:
    # py3k has unicode by default
    pass
else:
    reload(sys).setdefaultencoding('utf-8')


setup(
    name='revsquare-sphinx',
    version='0.0.2',
    author='Guillaume Pousseo',
    author_email='guillaumepousseo@revsquare.com',
    description='Install RevSquare themed template and settings to a project.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=['revsquare_sphinx', 'revsquare_theme'],
    include_package_data = True,
    classifiers=[
        'Development Status :: 0.0.1 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
    ],
    install_requires=[
        'Django>=1.4',
        'Sphinx==1.2.1',
    ],
)
