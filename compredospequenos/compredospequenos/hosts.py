from django_hosts import patterns, host

host_patterns = patterns('path.to',
    host(r'condoviz', 'condominiosevizinhanca.urls', name='condoviz'),
    host(r'viviremedia', 'homepage.urls', name='viviremedia'),
)