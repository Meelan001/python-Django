from django.urls import path
from .views import renderRegisterForm
from .views import renderLoginForm

urlpatterns=[
    path('register',renderRegisterForm),
    path('login',renderLoginForm)
]