from django.urls import path
from .import views
from .api import StudentCreateApi, StudentGetApi, StudentDeleteApi, StudentUpdateApi, StudentReterive
urlpatterns = [
    path('api/create', StudentCreateApi.as_view()),
    path('', StudentGetApi.as_view()),
    path('api/<int:pk>', StudentUpdateApi.as_view()),
    path('api/delete/<int:pk>', StudentDeleteApi.as_view()),
    path('api/get/<int:pk>', StudentReterive.as_view())
]
