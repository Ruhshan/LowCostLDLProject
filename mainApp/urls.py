from django.conf.urls import url

app_name='mainapp'
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^labs/$', views.LabsView.as_view(), name="labs"),
    url(r'^labs/add/$', views.LabAddView.as_view(), name="lab-add"),
    url(r'^labs/(?P<pk>[0-9]+)/$',views.LabsDetail.as_view(), name="lab-detail"),
    url(r'^labs/(?P<pk>[0-9]+)/update/$',views.LabUpdate.as_view(), name="lab-update"),
]
