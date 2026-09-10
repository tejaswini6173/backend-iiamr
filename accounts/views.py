from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Staff
from .serializers import StaffSerializer


class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all().order_by("-created_at")
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]


class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [AllowAny]