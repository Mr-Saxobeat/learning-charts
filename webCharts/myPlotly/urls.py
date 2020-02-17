from django.urls import path, include
from . import views

app_name = 'myPlotly'

urlpatterns = [
    path('graph/', views.Graph.as_view(), name="myGraph"),
]
