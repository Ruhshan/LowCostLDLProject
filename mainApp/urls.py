from django.conf.urls import url

app_name='mainapp'
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^labs/$', views.LabsView.as_view(), name="labs"),
    url(r'^labs/add/$', views.LabAddView.as_view(), name="lab-add"),
    url(r'^labs/(?P<pk>[0-9]+)/$',views.LabsDetail.as_view(), name="lab-detail"),
    url(r'^labs/(?P<pk>[0-9]+)/update/$',views.LabUpdate.as_view(), name="lab-update"),

    url(r'^users/$', views.UsersView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UsersDetail.as_view(), name="user-detail"),
    url(r'^users/add/$',views.UserAddView.as_view(),name="user-add"),
]
