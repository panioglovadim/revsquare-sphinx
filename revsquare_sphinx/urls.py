from django.conf import settings
from django.conf.urls import patterns, url, include

def get_document_root():
    """Returns the default Sphinx document root. Tries to trigger it from
    settings. 

    :returns:  Sphinx document root. Tries to trigger from settings. 
    :rtype: string
    """
    return settings.SPHINX_ROOT
    
urlpatterns = patterns('',
    (r'^doc/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': get_document_root()}))
