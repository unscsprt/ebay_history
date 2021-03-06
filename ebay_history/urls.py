from django.conf.urls import patterns, include, url
import views
from views import HomeView, SimilarView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^similar/$', SimilarView.as_view(), name='similar'),
    url(r'^search$', views.AverageView.as_view(), name='search'),

    url(r'^admin/', include(admin.site.urls)),
)
