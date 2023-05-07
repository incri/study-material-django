from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import User
from .serializers import ProfileSerializer, UserCreateSerializer, UserSerializer
from rest_framework.viewsets import GenericViewSet


class UserViewSet(
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=True, methods=["GET", "PUT"])
    def me(self, request):
        if request.method == "GET":
            (profile, created) = User.objects.get_or_create(user_id=request.user.id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def get_serializer_context(self):
        return {"request": self.request}
