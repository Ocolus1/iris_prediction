from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('predict/', views.predict_chances, name="submit_prediction"),
    path('results/', views.results, name="results"),
    
] 