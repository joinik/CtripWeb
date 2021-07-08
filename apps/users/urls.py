from django.contrib import admin
from django.urls import path, include, register_converter

from apps.users.views import IndexView, MobileCountView, UsernameCountView, RegisterView, LoginView
from utils.myconverters import UsernameConverter, PhoneConverter

register_converter(UsernameConverter, 'user')
register_converter(PhoneConverter, 'phone')

urlpatterns = [
    path('', IndexView.as_view()),
    path('mobiles/<phone:mobile>/count/', MobileCountView.as_view()),
    path('usernames/<user:username>/count/', UsernameCountView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

]
