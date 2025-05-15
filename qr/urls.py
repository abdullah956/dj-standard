from django.urls import path
from .views import add_certificate,logout_view, certificate_list, search_certificate,login_view

urlpatterns = [
    path('add/', add_certificate, name='add_certificate'),
    path('', certificate_list, name='certificate_list'),
    path('search/', search_certificate, name='search_certificate'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
