from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import TriageRequest
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Login successful"})
    else:
        return Response({"error": "Invalid credentials"}, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])

@csrf_exempt
def logout_api(request):
    logout(request)
    return Response({"message": "Logged out"})


# 🔹 Nurse Dashboard API
@api_view(['GET'])
@permission_classes([AllowAny])

def nurse_dashboard_api(request):

    if not request.user.groups.filter(name='Nurses').exists():
        return Response({"error": "Unauthorized"}, status=403)

    triage_requests = TriageRequest.objects.filter(
        nurse=request.user
    ).values()

    return Response(triage_requests)


# 🔹 Doctor Dashboard API
@api_view(['GET'])
@permission_classes([AllowAny])
def doctor_dashboard_api(request):

    if not request.user.groups.filter(name='Doctors').exists():
        return Response({"error": "Unauthorized"}, status=403)

    assigned_requests = TriageRequest.objects.filter(
        assigned_doctor=request.user
    ).values()

    return Response(assigned_requests)


# 🔹 User Role API
@api_view(['GET'])
@permission_classes([AllowAny])
def user_role(request):

    if request.user.groups.filter(name='Nurses').exists():
        return Response({"role": "nurse"})

    if request.user.groups.filter(name='Doctors').exists():
        return Response({"role": "doctor"})

    return Response({"role": "none"})
