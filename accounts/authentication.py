from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import accounts

class AccountsJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
            #looks for the user in the accounts table
            user = accounts.objects.get(id=user_id)
            return user
        except accounts.DoesNotExist:
            raise AuthenticationFailed('User not found', code='user_not_found')