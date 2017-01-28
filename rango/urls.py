<<<<<<< HEAD
from django.conf.urls import url
=======
from  django.conf.urls import url
>>>>>>> 5641c55aa379b7b8734e81bee0ab4a82b7d72637
from rango import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
]