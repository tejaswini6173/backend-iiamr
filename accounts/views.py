from django.contrib.auth.hashers import check_password

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Staff
from .serializers import StaffSerializer


# ---------------------------------------------------------
# STAFF CRUD
# ---------------------------------------------------------

class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all().order_by("-created_at")
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]


class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]


# ---------------------------------------------------------
# STAFF LOGIN
# POST /api/login/staff/login/
# ---------------------------------------------------------

class StaffLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        employee_id = request.data.get("employee_id")
        password = request.data.get("password")

        if not employee_id or not password:
            return Response(
                {
                    "status": "error",
                    "message": "Employee ID and password are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            staff = Staff.objects.get(employee_id=employee_id)
        except Staff.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Invalid credentials"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not check_password(password, staff.password):
            return Response(
                {
                    "status": "error",
                    "message": "Invalid credentials"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if staff.status != "active":
            return Response(
                {
                    "status": "error",
                    "message": "Your account is inactive. Contact administrator."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(staff)

        response = Response(
            {
                "status": "success",
                "user": {
                    "employee_id": staff.employee_id,
                    "full_name": staff.full_name,
                    "role": staff.role,
                    "department": staff.department,
                }
            },
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key="access_token",
            value=str(refresh.access_token),
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=30 * 60,
        )

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=5 * 60 * 60,
        )

        return response


# ---------------------------------------------------------
# STAFF LOGOUT
# POST /api/login/logout/
# ---------------------------------------------------------

