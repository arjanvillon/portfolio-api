from django.shortcuts import render
from rest_framework import viewsets, pagination, generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Project
from .serializers import ProjectSerializer, MessageSerializer
from .permissions import IsAdminUserOrReadOnly


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for projects"""

    serializer_class = ProjectSerializer
    permission_classes = [
        IsAdminUserOrReadOnly,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]
    pagination_class = StandardResultsSetPagination
    lookup_field = "uuid"

    def get_queryset(self):
        queryset = Project.objects.order_by("-year_start").prefetch_related("links")
        featured = self.request.query_params.get("featured", None)

        if featured is not None and featured == "True":
            queryset = queryset.filter(is_featured=True)
        else:
            queryset = queryset.filter(is_featured=False)

        return queryset


class MessageCreateApiView(generics.CreateAPIView):
    """API View for creating a single message"""

    serializer_class = MessageSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


def email(request):
    return render(request, "email.html")
