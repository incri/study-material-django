from django.db import router

from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("course-list", views.CourseViewSet, basename="course-list")

course_router = routers.NestedDefaultRouter(router, "course-list", lookup="course")
course_router.register("topic-list", views.TopicViewSet, basename="topic-list")

topic_router = routers.NestedDefaultRouter(course_router, "topic-list", lookup="topic")
topic_router.register("material-list", views.MaterialViewSet, basename="material-list")

urlpatterns = router.urls + course_router.urls + topic_router.urls
