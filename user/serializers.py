from rest_framework import serializers

from book_management.models import Book
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'book_interests')


class UserBookInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id',)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords must match.')

        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid email.')

            if not user.check_password(password):
                raise serializers.ValidationError('Invalid password.')

        else:
            raise serializers.ValidationError('Both email and password are required.')

        data['user'] = user
        return data
