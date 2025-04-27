# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thiruvarur/', views.thiruvarur, name='thiruvarur'),
    path('thirupur/', views.thirupur, name='thirupur'),
    path('trichy/', views.trichy, name='trichy'),
    path('cuddolore/', views.cuddolore, name='cuddolore'),
    # ... your existing routes
    path('results/', views.results, name='results'),
    path('results/<str:location>/<str:product>/', views.results, name='results'),
]
