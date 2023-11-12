from rest_framework import serializers
from bookapp.models import Book,BookNumber,Character,Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Author
        fields = ["id","name","surname"]


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BookNumber
        fields = ["id","isbn_10","isbn_13"]

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Character
        fields = ["id","name"]
        
class BookSerializer(serializers.ModelSerializer):
    number    = BookNumberSerializer(many=False)
    character = CharacterSerializer(many=True)
    authors   = AuthorSerializer(many=True)
    class Meta:
        model  = Book
        fields = ["title","description","price","published","is_published","cover","number","character","authors"]



## mini serializer for the book
class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = ["id","title","price"]