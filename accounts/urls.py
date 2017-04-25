from django.conf.urls import url

from .api import LoginView, LogoutView, RegistrationView

urlpatterns = [
	url(r'^register/$', RegistrationView.as_view()),
	url(r'^login/$', LoginView.as_view()),
	url(r'^logout/$', LogoutView.as_view()),	
]