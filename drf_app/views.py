from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
# Create your views here.


def listview(request):
    """
    to view the all the serializer data
    """
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data,safe=False)

def detailview(request,pk):
    '''
    to get the one object
    '''
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)
