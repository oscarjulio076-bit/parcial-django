
from django.urls import path
from .views import ElementoView

urlpatterns = [
    path('api/elementos/', ElementoView.as_view()),
    path('api/elementos/<int:pk>/', ElementoView.as_view()),
]
