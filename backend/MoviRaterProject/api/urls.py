from rest_framework import routers
from api.views import MovieViewSet,RatingViewSet

router = routers.DefaultRouter()
router.register("movies",MovieViewSet,basename='movies')
router.register("ratings",RatingViewSet,basename='ratings')

urlpatterns = [
    
]

urlpatterns += router.urls