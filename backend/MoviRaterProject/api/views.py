from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Movie, Rating
from api.serializer import MovieSerializer, RatingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

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
