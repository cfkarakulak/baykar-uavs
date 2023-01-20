from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateUavAPIView.as_view(), name='get_post_uavs'),
    path('<int:pk>/', views.RetrieveUpdateDestroyUavAPIView.as_view(), name='get_delete_update_uav'),
]