
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('analysis', views.analysis),
    path('apriori', views.apriori),
]
