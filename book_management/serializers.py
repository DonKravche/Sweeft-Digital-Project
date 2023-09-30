from rest_framework import serializers

from user.models import User
from user.serializers import UserSerializer
from .models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class AuthorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)
    owner = UserSerializer()

    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model in the serializer


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'condition', 'owner', 'location', 'recipient', 'image_poster']


class BookInterestSerializer(serializers.Serializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)


class BookTransferSerializer(serializers.Serializer):
    recipient_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
