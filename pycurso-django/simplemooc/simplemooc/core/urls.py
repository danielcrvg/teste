from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.core.views',
    url(r'^$', 'home', name='home'), # qualquer url vazia (r'^$') aponta pra app core, e roda a funcao home, definida no views.py 
    url(r'^contato/', 'contact', name='contact'),
)