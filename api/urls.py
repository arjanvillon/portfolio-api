from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("projects", views.ProjectViewSet, basename="Project")

urlpatterns = [
    path("message", views.MessageCreateApiView.as_view()),
    path("email", views.email, name="email"),
    path("", include(router.urls)),
]
