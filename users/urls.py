from django.db import router

from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = router.urls
