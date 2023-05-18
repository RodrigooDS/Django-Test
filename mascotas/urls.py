from django.urls import path

from .views import (
    AnimalCreateAPIView,
    AnimalDeleteAPIView,
    AnimalDetailAPIView,
    AnimalListAPIView,
    AnimalPartialUpdateAPIView,
)

app_name = "mascotas"


urlpatterns = [
    path("animals/", AnimalListAPIView.as_view(), name="animal-list"),
    path("animals/<int:pk>/", AnimalDetailAPIView.as_view(), name="animal-detail"),
    path("animals/create/", AnimalCreateAPIView.as_view(), name="animal-create"),
    path(
        "animals/<int:pk>/partial-update/",
        AnimalPartialUpdateAPIView.as_view(),
        name="animal-partial-update",
    ),
    path(
        "animals/<int:pk>/delete/", AnimalDeleteAPIView.as_view(), name="animal-delete"
    ),
]
