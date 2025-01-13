from django.urls import path  
from . import views
urlpatterns = [
  path('rewardsharing/', views.rewardsharing, name='rewardsharing'),
]