from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import Staff


class StaffJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        # Read the access token from the HttpOnly cookie
        raw_token = request.COOKIES.get("access_token")

        if raw_token is None:
            return None

        try:
            validated_token = self.get_validated_token(
                raw_token.encode("utf-8")
            )
        except Exception:
            raise AuthenticationFailed("Invalid or expired access token.")

        # Get Staff ID from the JWT
        staff_id = validated_token.get("user_id")

        if not staff_id:
            raise AuthenticationFailed("Invalid access token.")

        try:
            staff = Staff.objects.get(id=staff_id)
        except Staff.DoesNotExist:
            raise AuthenticationFailed("Staff account not found.")

        # Only active staff can use protected APIs
        if staff.status != "active":
            raise AuthenticationFailed(
                "Your account is inactive. Contact administrator."
            )

        return (staff, validated_token)