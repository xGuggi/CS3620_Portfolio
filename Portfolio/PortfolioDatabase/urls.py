from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('hobbies/<int:hobbies_id>/', views.detail_hobbies, name='detail_hobbies'),
    path('portfolio/<int:portfolio_id>/', views.detail_portfolio, name='detail_portfolio'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
]
