from rest_framework import routers
from bookapp.views import BookViewSet


router = routers.DefaultRouter()
router.register("books",BookViewSet)


urlpatterns = [
    
]

urlpatterns+= router.urls
