from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Uav
from .permissions import IsOwnerOrReadOnly
from .serializers import UavSerializer
from .pagination import CustomPagination
from .filters import UavFilter


class ListCreateUavAPIView(ListCreateAPIView):
    serializer_class = UavSerializer
    queryset = Uav.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UavFilter

    def perform_create(self, serializer):
        # Assign the user who created the Uav
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyUavAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UavSerializer
    queryset = Uav.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

