from django.conf.urls import url
from. import views
urlpatterns = [
    url(r'^first',views.first_try, name = 'first_try'),
	url(r'^second',views.second_try, name = 'second_try'),
	url(r'^history', views.disease_history, name='disease_history')]
