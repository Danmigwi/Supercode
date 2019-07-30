from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('Picture', views.picture,name="picture"),
    path('Link', views.link,name="link"),
    path('About', views.about,name="about"),
]