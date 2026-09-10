from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = Staff
        fields = [
            "id",
            "employee_id",
            "password",
            "full_name",
            "role",
            "department",
            "email",
            "phone",
            "status",
            "date_of_birth",
            "ug_qualification",
            "pg_qualification",
            "designation",
            "appointment_nature",
            "registration_number",
            "photo",
            "experience",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        password = validated_data.get("password")

        if password:
            validated_data["password"] = make_password(password)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        if password:
            instance.password = make_password(password)

        return super().update(instance, validated_data)