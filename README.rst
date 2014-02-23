################
RevSquare Sphinx
################

Install Sphinx documentation to a project using RevSquare themed template and settings.

*******
Install
*******

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

Add this line to your requirements.txt file:

.. code-block::  shell-session

    -e git+https://github.com/RevSquare/revsquare-sphinx#egg=revsquare-sphinx

And run:

.. code-block::  shell-session

    pip install -r requirements.txt

**************************
Setup sphinx documentation
**************************

It is recommanded to install the documentation folder in the current projet so anyone in the team can access it:

.. code-block::  shell-session

    mkdir doc
    cd doc
    sphinx-quickstart
    
You can check all the default settings.

***************
Setup the theme
***************

In your Sphinx documentation directory, update your conf.py file with the following settings:

.. code-block::  python

    pip install -r requirements.txt
