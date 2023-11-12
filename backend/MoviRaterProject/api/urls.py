from rest_framework import routers
from api.views import MovieViewSet, RatingViewSet,UserViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("ratings", RatingViewSet, basename="ratings")
router.register("register", UserViewSet, basename="register")


urlpatterns = []

urlpatterns += router.urls
