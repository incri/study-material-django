from .models import Course, Topic, Material
from .serializers import CourseSerializer, TopicSerializer, MaterialSerializer
from .pagination import CustomPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["course"]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_serializer_context(self):
        return {"course_id": self.kwargs["course_pk"], "request": self.request}


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_serializer_context(self):
        return {"topic_id": self.kwargs["topic_pk"], "request": self.request}
