from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as pr_views

urlpatterns = [
    url(r'^$', pr_views.index, name='index'),
    #url(r'index.html/', views.index, name='index'),
    #url(r'^demo/$', views.demo, name='demo_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
