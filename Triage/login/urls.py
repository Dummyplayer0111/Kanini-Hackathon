from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # API endpoints
    path('api/test/', views.test_api),
    path('api/nurse-dashboard/', views.nurse_dashboard_api),
    path('api/doctor-dashboard/', views.doctor_dashboard_api),
]
