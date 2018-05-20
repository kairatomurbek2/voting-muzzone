from django.urls import path, include
from web import views

urlpatterns = [
    path('<int:poll_id>/vote', views.vote),
    path('', views.feed)
]