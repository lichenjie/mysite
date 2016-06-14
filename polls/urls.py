from django.conf.urls import url
from . import views
#from . import settings
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jd/', views.jd, name='jd'),
    #url(r'^results/', views.results, name='results'),
    #url(r'^)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^en_xml/', views.en_xml, name='en_xml'),
	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}, name='static'),
    #url(r'^en_xml_operator/', views.en_xml_operator, name='en_xml_operator'),
]
