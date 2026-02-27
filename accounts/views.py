from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import accounts
from .serializers import accountsSerializer, RegisterSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response(accountsSerializer(user).data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = accounts.objects.filter(email=email).first()

    if user:

        if check_password(password, user.password):
            refresh = RefreshToken.for_user(user)

            refresh['user_id'] = str(user.id)
            refresh['role'] = user.role

            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": user.role,
                "user": {
                    "full_name": user.full_name,
                    "email": user.email
                }
            })
        else:
            return Response({"error": "Invalid password"}, status=400)
    
    return Response({"error": "Invalid email"}, status=400)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):

    serializer = accountsSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        #gets the refresh token 
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=400)
        #initialize the token and blacklist it
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"message": "Successfully logged out"}, status=205)
    except Exception as e:
        return Response({"error": "Invalid token or already blacklisted"}, status=400)