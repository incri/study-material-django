from rest_framework import serializers
from courses.models import Course, Topic, Material
from users.serializers import UserCreateSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "description", "user"]

    def get_fields(self):
        fields = super().get_fields()
        if self.context["request"].method == "GET":
            fields["user"] = UserCreateSerializer()
        return fields


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name", "description"]

    def get_fields(self):
        fields = super().get_fields()
        if self.context["request"].method == "GET":
            fields["course"] = CourseSerializer()
        return fields

    def create(self, validated_data):
        course = self.context["course_id"]
        return Topic.objects.create(course_id=course, **validated_data)


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ["id", "name", "link"]

    def get_fields(self):
        fields = super().get_fields()
        if self.context["request"].method == "GET":
            fields["topic"] = TopicSerializer()
        return fields

    def create(self, validated_data):
        topic = self.context["topic_id"]
        return Material.objects.create(topic_id=topic, **validated_data)
