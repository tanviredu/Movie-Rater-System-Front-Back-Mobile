from rest_framework import viewsets

from bookapp.models import Book
from bookapp.serializer import BookSerializer,BookMiniSerializer

from rest_framework import parsers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    permission_classes = [IsAuthenticated,]
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    queryset = Book.objects.all()
    
    ## override method
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance=instance)
        return Response(serializer.data)
            
    