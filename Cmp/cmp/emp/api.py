from rest_framework import generics
from .models import *
from .Serializers import StudentSerialzer


class StudentCreateApi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer


class StudentGetApi(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer


class StudentUpdateApi(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer


class StudentDeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer


class StudentReterive(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
