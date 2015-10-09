from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^new/$', login_required(views.WorkoutCreateView.as_view()), name='workout-create'),
	url(r'^(?P<pk>[0-9]+)/$', login_required(views.WorkoutDetailView.as_view()), name='workout-detail'),
	url(r'^(?P<pk>[0-9]+)/update$', login_required(views.WorkoutUpdateView.as_view()), name='workout-update'),
	url(r'^(?P<pk>[0-9]+)/delete$', login_required(views.WorkoutDeleteView.as_view()), name='workout-delete'),	
	url(r'^(?P<pk>[0-9]+)/new$', views.ActivityCreateView.as_view(), name='activity-create'),
	url(r'^(?P<wpk>[0-9]+)/(?P<pk>[0-9]+)$', views.ActivityUpdateView.as_view(), name='activity-update'),
	url(r'^(?P<wpk>[0-9]+)/(?P<pk>[0-9]+)/delete$', views.ActivityDeleteView.as_view(), name='activity-delete'),

]