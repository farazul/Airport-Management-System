from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Flight Booking Admin'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('airport_mgmt/', views.airport_mgmt, name='airport_mgmt'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/security_login', views.login_security, name='security_login'),
    path('accounts/staff_login', views.login_staff, name='staff_login'),    
    path('security_clearing', views.clear_security, name='security_clearing'),
    path('clearing_for_security/<str:pk>', views.clear_for_security, name='clearing_for_security'),
    path('view_flights', views.view_flights, name='view_flights'),
    path('self_check_in/<int:pk>', views.self_check_in, name='self_check_in'),
    path('search_by_source', views.search_by_source, name='search_by_source'),
    path('search_by_destination', views.search_by_destination, name='search_by_destination'),
    path('staff_generating_report/<int:pk>', views.generate_report_staff, name='staff_generating_report'),
    path('view_available_flights/', views.view_available_flights, name='view_available_flights'),
    path('book_flight/<int:pk>', views.book_flight, name='book_flight'),
    path('passenger_home/<int:pnr>', views.passenger_home, name='passenger_home'),
    path('create_pdf/<int:pnr>', views.create_pdf, name='create_pdf'),

]