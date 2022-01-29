from django.urls import path, include
from .views import getRoom, getRooms, getRoutes

urlpatterns = [
    path('', getRoutes),
    path('rooms/', getRooms),
    path('rooms/<str:pk>/', getRoom),
]
