from . import views
from django.urls import path

urlpatterns = [
    path('create', views.add_service, name='add_service'),
    path('', views.service_list_view, name="services"),
    path('<int:service_id>', views.service_view, name="one_service"),
    # Category-specific URLs
    path('air-conditioner', views.service_list_view, {'category': 'AIR_CONDITIONER'}, name="services_air_conditioner"),
    path('all-in-one', views.service_list_view, {'category': 'ALL_IN_ONE'}, name="services_all_in_one"),
    path('carpentry', views.service_list_view, {'category': 'CARPENTRY'}, name="services_carpentry"),
    path('electricity', views.service_list_view, {'category': 'ELECTRICITY'}, name="services_electricity"),
    path('gardening', views.service_list_view, {'category': 'GARDENING'}, name="services_gardening"),
    path('home-machines', views.service_list_view, {'category': 'HOME_MACHINES'}, name="services_home_machines"),
    path('house-keeping', views.service_list_view, {'category': 'HOUSEKEEPING'}, name="services_housekeeping"),
    path('interior-design', views.service_list_view, {'category': 'INTERIOR_DESIGN'}, name="services_interior_design"),
    path('locks', views.service_list_view, {'category': 'LOCKS'}, name="services_locks"),
    path('painting', views.service_list_view, {'category': 'PAINTING'}, name="services_painting"),
    path('plumbing', views.service_list_view, {'category': 'PLUMBING'}, name="services_plumbing"),
    path('water-heaters', views.service_list_view, {'category': 'WATER_HEATERS'}, name="services_water_heaters"),
]
