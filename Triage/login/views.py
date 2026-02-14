from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TriageRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def nurse_dashboard_api(request):

    if not request.user.groups.filter(name='Nurses').exists():
        return Response({"error": "Unauthorized"}, status=403)

    triage_requests = TriageRequest.objects.filter(
        nurse=request.user
    ).values()

    return Response(triage_requests)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_dashboard_api(request):

    if not request.user.groups.filter(name='Doctors').exists():
        return Response({"error": "Unauthorized"}, status=403)

    assigned_requests = TriageRequest.objects.filter(
        assigned_doctor=request.user
    ).values()

    return Response(assigned_requests)

@api_view(['GET'])

def test_api(request):
    return Response({"message": "Django API working"})

@login_required
def dashboard(request):

    if request.user.groups.filter(name='Nurses').exists():
        return redirect('http://localhost:3000/nurse')

    if request.user.groups.filter(name='Doctors').exists():
        return redirect('http://localhost:3000/doctor')

    return redirect('login')

