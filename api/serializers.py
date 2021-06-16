from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Project, ProjectLink, Message


class ProjectLinkSerializer(serializers.ModelSerializer):
    """Serializes a project link"""

    class Meta:
        model = ProjectLink
        fields = ["id", "url", "type"]


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Serializes a project"""

    links = ProjectLinkSerializer(many=True, read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Project
        fields = [
            "uuid",
            "title",
            "description",
            "image",
            "year_start",
            "year_end",
            "links",
            "tags",
        ]


class MessageSerializer(serializers.ModelSerializer):
    """Serializes a message instance"""

    class Meta:
        model = Message
        fields = ["id", "name", "email", "created_at"]
