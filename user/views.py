from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from book_management.models import Book
from book_management.serializers import BookSerializer
from user.models import User
from user.serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer, UserBookInterestSerializer


class UserRegistrationView(APIView):

    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):

    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserBookInterestSerializer
    lookup_field = 'id'

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(request_body=UserBookInterestSerializer)
    def add_interest(self, request, *args, **kwargs):
        user = self.get_object()
        book_id = request.data.get('book_id')
        if book_id:
            book = Book.objects.get(pk=book_id)
            user.book_interests.add(book)
            user.save()
            return Response({'status': 'Interest added successfully'})
        return Response({'status': 'Failed to add interest'})

    @action(detail=True, methods=['delete'])
    @swagger_auto_schema(request_body=UserBookInterestSerializer)
    def remove_interest(self, request, *args, **kwargs):
        user = self.get_object()
        book_id = request.data.get('book_id')
        if book_id:
            book = Book.objects.get(pk=book_id)
            user.book_interests.remove(book)
            user.save()
            return Response({'status': 'Interest removed successfully'})
        return Response({'status': 'Failed to remove interest'})

    @action(detail=True, methods=['get'])
    def interests_by_user(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = BookSerializer(user.book_interests.all(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def users_by_book(self, request, *args, **kwargs):
        book_id = request.query_params.get('book_id')
        if book_id:
            book = Book.objects.get(pk=book_id)
            serializer = UserSerializer(book.book_interests.all(), many=True)
            return Response(serializer.data)
        return Response({'status': 'Book ID is required'})
