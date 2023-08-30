from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cars', views.cars),
    path('car/details/<int:id>', views.car),
    path('search/<str:query>', views.search),
    # path('user/create', views.user_create),
    # path('user/login', views.user_login),
    # path('user/<int:id>', views.user),
]
