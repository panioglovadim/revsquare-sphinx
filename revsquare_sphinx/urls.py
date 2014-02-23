from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required


def get_document_root():
    """Returns the default Sphinx document root. Tries to trigger it from
    settings. 

    :returns:  Sphinx document root. Tries to trigger from settings. 
    :rtype: string
    """
    return settings.SPHINX_ROOT
    
urlpatterns = patterns('',
    (r'^$', login_required('django.views.static.serve'), {
            'path': 'index.html', 'document_root': get_document_root()}),
    (r'(?P<path>.*)$', login_required('django.views.static.serve'), {
        'document_root': get_document_root()}))
