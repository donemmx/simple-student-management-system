
from django.contrib import admin
from django.urls import path,include,re_path

#from django.conf.urls import url
from django.views.static import serve

admin.autodiscover()
admin.site.enable_nav_sidebar = False
#importing static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('parach_dashboard.urls', namespace='parach_dashboard')),

    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    # re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 