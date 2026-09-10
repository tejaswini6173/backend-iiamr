from django.db import models


class Staff(models.Model):
    ROLE_CHOICES = [
        ("doctor", "Doctor"),
        ("admin", "Admin"),
        ("receptionist", "Receptionist"),
        ("nurse", "Nurse"),
        ("lab_technician", "Lab Technician"),
    ]

    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("terminated", "Terminated"),
        ("on_leave", "On Leave"),
    ]

    APPOINTMENT_CHOICES = [
        ("regular", "Regular"),
        ("contractual", "Contractual"),
        ("deputation", "Deputation"),
        ("part_time", "Part Time"),
        ("adhoc", "Adhoc"),
    ]

    employee_id = models.CharField(max_length=32, unique=True, db_index=True)
    password = models.CharField(max_length=255)

    full_name = models.CharField(max_length=150)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    date_of_birth = models.DateField(blank=True, null=True)
    ug_qualification = models.CharField(max_length=255, blank=True)
    pg_qualification = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=100)
    appointment_nature = models.CharField(
        max_length=30,
        choices=APPOINTMENT_CHOICES,
        blank=True
    )
    registration_number = models.CharField(max_length=150)
    photo = models.ImageField(
        upload_to="staff_photos/",
        blank=True,
        null=True
    )
    experience = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_id} ({self.full_name})"


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ("create", "Create"),
        ("read", "Read"),
        ("update", "Update"),
        ("delete", "Delete"),
        ("login", "Login"),
        ("logout", "Logout"),
    ]

    STATUS_CHOICES = [
        ("success", "Success"),
        ("failed", "Failed"),
    ]

    staff = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs"
    )

    employee_id = models.CharField(
        max_length=32,
        blank=True
    )

    role = models.CharField(
        max_length=30,
        blank=True
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    module = models.CharField(
        max_length=100
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    description = models.TextField(
        blank=True
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee_id} - {self.action} - {self.module}"