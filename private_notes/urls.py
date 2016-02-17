from django.conf.urls import include, url
from django.contrib import admin
from notesapp import  views 
urlpatterns = [
    # Examples:
    # url(r'^$', 'private_notes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.home,name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('notesapp.urls')),
]
