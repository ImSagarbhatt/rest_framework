from .serializers import StudentSerializer
from .models import Student
from rest_framework import generics


class StudentList(generics.ListCreateAPIView):
    """
    to create and show the list of students
    """
    queryset= Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    to update,delete and retrieve the student
    """
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

