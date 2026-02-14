from django.db import models
from django.contrib.auth.models import User


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    blood_group = models.CharField(max_length=5, blank=True)
    chronic_conditions = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    past_surgeries = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class TriageRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE, related_name="nurse_requests")

    symptoms = models.TextField()
    blood_pressure = models.IntegerField()
    heart_rate = models.IntegerField()
    temperature = models.FloatField()

    predicted_risk = models.CharField(max_length=10, blank=True, null=True)
    recommended_department = models.CharField(max_length=100, blank=True, null=True)

    assigned_doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor_requests"
    )

    created_at = models.DateTimeField(auto_now_add=True)
