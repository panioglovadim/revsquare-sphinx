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

Update your conf.py file in your Sphinx documentation directory with the following settings:

On top of the document add:


.. code-block::  python

    import revsquare_theme

Make sure you have at least the following extensions installed:

.. code-block::  python
   
    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode']
    
Now add the theme by setting the *html_theme* and *revsquare_theme* parameters:

.. code-block::  python
   
    html_theme = 'revsquare'
    html_theme_path = revsquare_theme.get_html_theme_path()



************
Setup django
************

In order to simply link the templates wihin your website urls, simply add the following:

1. In your settings.py add to the *INSTALLED_APPS*

.. code-block::  python
   
    INSTALLED_APPS = (
        ...
        'revsquare_sphinx',
        ...
    )
    
2. In your root urls.py module, add to the urlpatterns (of course you can use any wildcard that you want 'doc' is just an exemple):

.. code-block::  python
    urlpatterns = patterns('',
        ...

        url(r'^doc/', include('revsquare_sphinx.urls')),
        ...
    )  
