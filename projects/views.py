from rest_framework import viewsets, pagination
from rest_framework.authentication import TokenAuthentication
from .models import Project
from .serializers import ProjectSerializer
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
    queryset = Project.objects.all()
    lookup_field = "uuid"
