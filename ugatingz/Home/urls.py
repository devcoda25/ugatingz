from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home,name="home_page" ),

    path('topic/<slug:category_slug>/<slug:topic_slug>/', views.topic_detail, name='topic_detail'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),



]
