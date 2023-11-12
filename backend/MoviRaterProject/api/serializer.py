from rest_framework import serializers
from api.models import Rating, Movie
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {'password':{'write_only':True}}
        
    ## you have to override the create method
    ## if you dont do that password will be stored 
    ## in clean text and then registration work
    ## but login wont work because django try to compare hash password
    ## not clean password
    ## you have to understand that this APIView is not creating users
    ## it is just storing data in the database
    ## in order to create the user you have to hash the password
    ## overrite function
    ## this function is autometically called
    ## in the serializer
    ## we need to customize the data
    ## in the create method the validated_data is passed
    ## autometically and contverted to json
    ## so we can get the data from the dictionary
    ## then you call the function the by default function
    ## wont work, new function work
    ## so when we try to post data 
    ## insted of just storing the data
    ## it will now invoke the create override method
    ## and create the user.
    def create(self,validated_json_data):
        user = User.objects.create_user(
            username = validated_json_data['username'],
            password = validated_json_data['password']
        )
        return user
    

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description","number_of_ratings","avg_rating"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "stars", "user", "movie"]
