
from django.urls import path, include

from api_rest.views import client_views, vehicle_views, rent_views

urlpatterns = [
    path('clients/', client_views.get_clients, name='get-all-clients'),
    path('client/cpf=<str:cpf>/', client_views.get_client_by_cpf, name='get-client-by-cpf' ),
    path('client/', client_views.client_manager),
    # path('vehicle/', vehicle_views.get_vehicles, name='get-all-vehicles'),
    # path('vehicle/?code=<int:code>/', vehicle_views.get_vehicle_by_code, name='get-vehicle-by-code'),
    # path('vehicle/?', vehicle_views.vehicle_manager),
    # path('rent/', rent_views.get_rents, name='get-all-rents'),
    # path('rent/?code=<int:code>/', rent_views.get_rent_by_code, name='get-rent-by-code')
]