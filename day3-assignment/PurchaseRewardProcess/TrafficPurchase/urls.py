from django.urls import path
from . import views
urlpatterns = [
  path('trafficpurchase/', views.trafficpurchase, name='trafficpurchase'),
]