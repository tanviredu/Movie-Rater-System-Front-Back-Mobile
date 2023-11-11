from rest_framework import viewsets

from bookapp.models import Book
from bookapp.serializer import BookSerializer

from rest_framework import parsers
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,]
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    queryset = Book.objects.all()
    