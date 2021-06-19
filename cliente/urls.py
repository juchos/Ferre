from rest_framework import routers

from .viewsets import ClienteViewSet

router = routers.SimpleRouter()
router.register('cliente', ClienteViewSet)


urlpatterns = router.urls
