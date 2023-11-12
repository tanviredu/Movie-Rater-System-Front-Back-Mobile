from rest_framework import viewsets, status,permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Movie, Rating
from api.serializer import MovieSerializer, RatingSerializer,UserSerializer
from django.contrib.auth.models import User


## i want list view allowany
## detail view Isauthenticated
## rate_movie Is authticated
## rest of them Is autheticated
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    
    
## 

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    ## override the get permission method
    def get_permissions(self):
        if self.action == "list":
            return [permissions.AllowAny()]
        elif self.action in ["retrieve","rate_movie"]:
            return [permissions.IsAuthenticated()]
        elif self.action in ["update","destroy"]:
            return [permissions.IsAuthenticated()]
        else:
            return super().get_permissions()
        


    ## detail = True mens get by id te kaj korbe
    ## specfic movie
    ## when detail = True then you need to provide pk
    ## detail false means list of movie

    ## we create the rating inside the movie
    @action(detail=True, methods=["POST"])
    def rate_movie(self, request, pk):
        if "stars" in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data["stars"]
            user = request.user
            ##data = {"movie":movie.title,"stars":stars,"user":user.username}
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.user = request.user
                rating.save()
                json_res = RatingSerializer(rating, many=False)

                return Response(
                    {"message": "Updated", "data": json_res.data},
                    status=status.HTTP_200_OK,
                )
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                json_res = RatingSerializer(rating, many=False)
                return Response(
                    {"message": "created", "data": json_res.data},
                    status=status.HTTP_200_OK,
                )
        else:
            response = {"messgae": "not working"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
