from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PasswordResetSerializer, PasswordResetConfirmSerializer

class PasswordResetView(APIView):
    """
    API for Forget Password - send reset email
    """
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password reset email sent."}, status=status.HTTP_200_OK)

class PasswordResetConfirmView(APIView):
    """
    API for Reset Password - update password
    """
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
