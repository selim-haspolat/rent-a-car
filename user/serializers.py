from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


# --------------------------------------------------
# UserSerializer
# --------------------------------------------------

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        required = False,
        write_only = True,
    )

    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password
            password = attrs['password']
            validate_password(password)
            attrs.update({'password': make_password(password)})
        return super().validate(attrs)

    class Meta:
        model = User
        exclude = [
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]


# -------------------------------
# UserTokenSerializer
# -------------------------------
from dj_rest_auth.serializers import TokenSerializer

class UserTokenSerializer(TokenSerializer):
    
    user = UserSerializer()

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')

