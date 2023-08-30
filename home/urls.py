from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cars', views.cars),
    # path('product/details/<int:id>', views.product),
    # path('search/<str:query>', views.search),
    # path('user/create', views.user_create),
    # path('user/login', views.user_login),
    # path('user/<int:id>', views.user),
]
