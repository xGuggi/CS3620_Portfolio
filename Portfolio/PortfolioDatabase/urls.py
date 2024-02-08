from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('hobbies/', views.Hobbies, name='hobbies'),
    path('portfolio/', views.Portfolio, name='portfolio'),
    path('contact/', views.Contact, name='contact')
]
