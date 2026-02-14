import uuid
from django.db import models
from django.contrib.auth.models import User


# -------------------------
# DEPARTMENT CHOICES
# -------------------------

DEPARTMENT_CHOICES = [
    ("Emergency", "Emergency"),
    ("General_Medicine", "General Medicine"),
    ("Cardiology", "Cardiology"),
    ("Neurology", "Neurology"),
    ("Pulmonology", "Pulmonology"),
    ("Gastroenterology", "Gastroenterology"),
    ("Orthopedics", "Orthopedics"),
    ("Pediatrics", "Pediatrics"),
    ("Nephrology", "Nephrology"),
    ("Endocrinology", "Endocrinology"),
]


def generate_employee_id():
    return f"EMP-{uuid.uuid4().hex[:6].upper()}"


# =========================
# STAFF PROFILE
# =========================

class StaffProfile(models.Model):
    LANGUAGE_CHOICES = [
        ("auto", "Auto-detect"),
        ("ta", "Tamil"),
        ("hi", "Hindi"),
        ("te", "Telugu"),
        ("kn", "Kannada"),
        ("ml", "Malayalam"),
        ("mr", "Marathi"),
        ("bn", "Bengali"),
        ("gu", "Gujarati"),
        ("ur", "Urdu"),
        ("pa", "Punjabi"),
        ("en", "English"),
        ("es", "Spanish"),
        ("fr", "French"),
        ("ar", "Arabic"),
        ("zh", "Chinese"),
        ("ja", "Japanese"),
        ("ko", "Korean"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employee_id = models.CharField(
        max_length=20,
        default=generate_employee_id,
        unique=True
    )

    # ✅ Updated with fixed department choices
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES
    )

    language = models.CharField(
        max_length=5,
        choices=LANGUAGE_CHOICES,
        default="auto"
    )

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.department}"


# =========================
# PATIENT
# =========================

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    blood_group = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True)
    past_surgeries = models.TextField(blank=True)

    diabetes = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    chronic_kidney_disease = models.BooleanField(default=False)
    previous_stroke = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    obese = models.BooleanField(default=False)
    previous_heart_attack = models.BooleanField(default=False)
    previous_hospitalization = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# =========================
# TRIAGE REQUEST
# =========================

class TriageRequest(models.Model):

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name="triage_request"
    )
    nurse = models.ForeignKey(User, on_delete=models.CASCADE, related_name="nurse_requests")

    systolic_bp = models.IntegerField()
    heart_rate = models.IntegerField()
    temperature = models.FloatField()
    oxygen = models.IntegerField()

    chest_pain = models.BooleanField(default=False)
    severe_breathlessness = models.BooleanField(default=False)
    sudden_confusion = models.BooleanField(default=False)
    stroke_symptoms = models.BooleanField(default=False)
    seizure = models.BooleanField(default=False)
    severe_trauma = models.BooleanField(default=False)
    uncontrolled_bleeding = models.BooleanField(default=False)
    loss_of_consciousness = models.BooleanField(default=False)
    severe_allergic_reaction = models.BooleanField(default=False)

    persistent_fever = models.BooleanField(default=False)
    vomiting = models.BooleanField(default=False)
    moderate_abdominal_pain = models.BooleanField(default=False)
    persistent_cough = models.BooleanField(default=False)
    moderate_breathlessness = models.BooleanField(default=False)
    severe_headache = models.BooleanField(default=False)
    dizziness = models.BooleanField(default=False)
    dehydration = models.BooleanField(default=False)
    palpitations = models.BooleanField(default=False)
    migraine = models.BooleanField(default=False)

    mild_headache = models.BooleanField(default=False)
    sore_throat = models.BooleanField(default=False)
    runny_nose = models.BooleanField(default=False)
    mild_cough = models.BooleanField(default=False)
    fatigue = models.BooleanField(default=False)
    body_ache = models.BooleanField(default=False)
    mild_abdominal_pain = models.BooleanField(default=False)
    skin_rash = models.BooleanField(default=False)
    mild_back_pain = models.BooleanField(default=False)
    mild_joint_pain = models.BooleanField(default=False)

    predicted_risk = models.CharField(max_length=10, blank=True, null=True)

    # ✅ Department limited to your 10 departments
    recommended_department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        blank=True,
        null=True
    )

    assigned_doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor_requests"
    )

    created_at = models.DateTimeField(auto_now_add=True)


# =========================
# EMERGENCY REQUEST
# =========================

class EmergencyRequest(models.Model):

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name="emergency_request"
    )

    nurse = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_emergencies"
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assigned_emergencies"
    )

    # ✅ Added department tracking
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency: {self.patient.full_name} - {self.department}"
