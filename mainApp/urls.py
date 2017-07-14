from django.conf.urls import url

app_name='mainapp'
from . import views, data_views


urlpatterns = [
    url(r'^$', data_views.HomeView.as_view(), name="home"),
    url(r'^labs/$', views.LabsView.as_view(), name="labs"),
    url(r'^labs/add/$', views.LabAddView.as_view(), name="lab-add"),
    url(r'^labs/(?P<pk>[0-9]+)/$',views.LabsDetail.as_view(), name="lab-detail"),
    url(r'^labs/(?P<pk>[0-9]+)/update/$',views.LabUpdate.as_view(), name="lab-update"),

    url(r'^users/$', views.UsersView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UsersDetail.as_view(), name="user-detail"),
    url(r'^users/add/$',views.UserAddView.as_view(),name="user-add"),
    url(r'^users/(?P<pk>[0-9]+)/update/$',views.UserUpdateView.as_view(),name="user-update"),

    url(r'data/add/regular/$', data_views.DataAddReView.as_view(), name="data-add-re"),
    url(r'data/add/qc/$', data_views.QCDataAddView.as_view(), name="data-add-qc"),
    url(r'data/qc/all/$', data_views.DataQCs.as_view(), name="data-qc"),
    url(r'data/qc/(?P<pk>[0-9]+)/$', data_views.DataQCDetails.as_view(), name="data-qc-detail"),
    url(r'data/(?P<pk>[0-9]+)/$', data_views.DataDetails.as_view(), name="data-detail"),


    url(r'qc/$', data_views.QCsView.as_view(), name="qcs"),
    url(r'qc/add/$', data_views.QCAddView.as_view(), name="qc-add"),
    url(r'qc/(?P<pk>[0-9]+)/$', data_views.QCDetails.as_view(), name="qc-detail"),


    ## ajax urls
    url(r'^get_labs_ajax/', data_views.get_labs_ajax, name="get_labs_ajax"),
    url(r'^get_users_ajax/', data_views.get_users_ajax, name="get_users_ajax"),

]
