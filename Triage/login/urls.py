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

    # 🔹 Patient APIs
    path('api/inpatient-analyze/', views.inpatient_analyze),
    path('api/patient/search/', views.patient_search),
    path('api/patient/create/', views.patient_create),

    # 🔹 Emergency APIs
    path('api/doctors/', views.doctors_by_department),
    path('api/emergency/confirm/', views.emergency_confirm),

    # 🔹 Triage ML API
    path('api/whisper/', views.whisper_transcribe),
    path('api/triage/', views.triage_api),

    # 🔹 Triage Request CRUD
    path('api/triage-request/create/', views.triage_request_create),

    # 🔹 Doctor Action APIs
    path('api/triage-request/<int:triage_id>/resolve/', views.resolve_triage_request),
    path('api/emergency/<int:emergency_id>/convert/', views.convert_emergency_to_triage),
    path('api/patient/<int:patient_id>/history/', views.update_patient_history),
]
