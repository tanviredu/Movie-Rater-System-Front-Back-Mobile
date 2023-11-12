from rest_framework import viewsets

from bookapp.models import Book
from bookapp.serializer import BookSerializer, BookMiniSerializer,UserSerializer

from rest_framework import parsers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    ## you have to override the create method
    ## if you dont do that password will be stored 
    ## in clean text and then registration work
    ## but login wont work because django try to compare hash password
    ## not clean password
    ## you have to understand that this APIView is not creating users
    ## it is just storing data in the database
    ## in order to create the user you have to hash the password
    def create(self,validated_data):
        print(validated_data)
        user = User.objects.create_user(
            username= validated_data['username'],
            password= validated_data['password']
        )
        print(user.username)
        print(user.password)
        return user
        
    
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    queryset = Book.objects.all()

    ## override method
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance=instance)
        return Response(serializer.data)
