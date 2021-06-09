from rest_framework import serializers
from .models import Project, ProjectLink


class ProjectLinkSerializer(serializers.ModelSerializer):
    """Serializes a project link"""

    class Meta:
        model = ProjectLink
        fields = ["id", "url", "type"]


class ProjectSerializer(serializers.ModelSerializer):
    """Serializes a project"""

    links = ProjectLinkSerializer(many=True, read_only=True)

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
        ]
