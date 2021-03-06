import uuid
import datetime
from django.db import models
from taggit.managers import TaggableManager
from utilities.functions import generate_timestamp
from .choices import PROJECT_LINK_TYPE_CHOICES


def get_current_year():
    return datetime.date.today().year


def project_image_path(instance, filename):
    extension = filename.split(".")[-1]
    return "projects/{0}/{1}.{2}".format(instance.uuid, generate_timestamp(), extension)


class Project(models.Model):
    """Model for a single project"""

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=project_image_path, blank=True)
    year_start = models.PositiveIntegerField(
        choices=[(r, r) for r in range(2000, datetime.date.today().year + 1)],
        default=get_current_year,
    )
    year_end = models.PositiveIntegerField(
        choices=[(r, r) for r in range(2000, datetime.date.today().year + 1)],
        default=get_current_year,
    )
    is_featured = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class ProjectLink(models.Model):
    """Model for saving a single link of a project"""

    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="links"
    )
    url = models.URLField()
    type = models.PositiveIntegerField(choices=PROJECT_LINK_TYPE_CHOICES, default=1)

    def __str__(self):
        return f"{self.project.title}'s link"


class Message(models.Model):
    """Model for saving a sent message"""

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
