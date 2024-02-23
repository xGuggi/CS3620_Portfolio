from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('hobbies/<int:hobbies_id>/', views.detail_hobbies, name='detail_hobbies'),
    path('portfolio/<int:portfolio_id>/', views.detail_portfolio, name='detail_portfolio'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/add/', views.portfolio_add, name='portfolio_add'),
    path('portfolio/update/<int:id>/', views.portfolio_update, name='portfolio_update'),
    path('portfolio/delete/<int:id>/', views.portfolio_delete, name='portfolio_delete'),
]
