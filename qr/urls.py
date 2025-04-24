from django.urls import path
from .views import add_certificate, certificate_list, search_certificate

urlpatterns = [
    path('', add_certificate, name='add_certificate'),
    path('certificates/', certificate_list, name='certificate_list'),
    path('search/', search_certificate, name='search_certificate'),
]
