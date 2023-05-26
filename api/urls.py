from django.urls import path
from . import views

urlpatterns = [
    #path('', views.getData),
    #path('calc/', views.calculateStocks),
    path('testData/', views.YourView.as_view())
]