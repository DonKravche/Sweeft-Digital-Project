from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import BookFilter
from .models import Book, Author, Genre
from .permissions import IsBookOwner
from .serializers import BookListSerializer, BookCreateSerializer, AuthorSerializer, GenreSerializer, \
    AuthorDeleteSerializer, BookInterestSerializer, BookTransferSerializer


class BookList(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser]
    queryset = Book.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListSerializer
        elif self.request.method == 'POST':
            return BookCreateSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


class AuthorCreate(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDelete(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDeleteSerializer


class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDelete(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookInterestView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_book(book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=BookInterestSerializer
    )
    def post(self, request, book_id):
        book = self.get_book(book_id)
        if not book:
            return Response({'message': 'Book does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = BookInterestSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user_id']
            if user in book.interested_users.all():
                return Response({'message': 'User is already interested in this book'},
                                status=status.HTTP_400_BAD_REQUEST)
            book.interested_users.add(user)
            return Response({'message': 'User added to interested users list'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookTransferView(APIView):
    permission_classes = [IsAuthenticated, IsBookOwner]

    @staticmethod
    def get_book(book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return None

    @swagger_auto_schema(
        request_body=BookTransferSerializer,
    )
    def post(self, request, book_id):
        self.check_object_permissions(request, self.get_book(book_id))
        book = self.get_book(book_id)
        if not book:
            return Response({'message': 'Book does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = BookTransferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recipient = serializer.validated_data['recipient_id']
        if recipient not in book.interested_users.all():
            return Response({'message': 'User is not interested in this book'},
                            status=status.HTTP_400_BAD_REQUEST)

        if book.recipient == recipient:
            return Response({'message': 'Book is already transferred to this user'},
                            status=status.HTTP_400_BAD_REQUEST)

        if book.owner == recipient:
            return Response({'message': 'Book is already owned by this user'},
                            status=status.HTTP_400_BAD_REQUEST)

        book.owner = recipient
        book.recipient = recipient
        book.save()
        return Response({'message': 'Book transferred successfully', },
                        status=status.HTTP_200_OK)
