from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.login_user, name='login'),
    path("register", views.register_user, name='register'),
    path("logout", views.logout_user, name='logout'),
    path("info/<int:pk>/", views.info, name='info'),
    path("cart", views.cart, name='cart'),
    path("add_good/<int:pk>/", views.add_good, name='add_good'),
    path("remove_good/<int:pk>/", views.remove_good, name='remove_good')
]
