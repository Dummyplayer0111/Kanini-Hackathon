from django.urls import path
from . import views

urlpatterns = [

    # 🔹 Session APIs
    path('api/login/', views.login_api),
    path('api/logout/', views.logout_api),
    path('api/user-role/', views.user_role),

    # 🔹 Dashboard APIs
    path('api/nurse-dashboard/', views.nurse_dashboard_api),
    path('api/doctor-dashboard/', views.doctor_dashboard_api),
]
