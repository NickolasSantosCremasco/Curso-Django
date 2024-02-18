
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
    #this path only accept numbers as an answer

]
