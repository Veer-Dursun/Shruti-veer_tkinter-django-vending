from rest_framework import routers
from .views_api import StudentViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
