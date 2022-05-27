from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



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

@csrf_exempt
def createview(request):
    """
    to add the create the object
    """
    if request.method == "POST":
        stu_data = JSONParser().parse(request)
        serializer = StudentSerializer(data = stu_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
    else:
        resp = {'msg':'its a get request'}
        return JsonResponse(resp)

@csrf_exempt
def updateview(request):
    """
    to update the value of object
    """
    if request.method == "PUT":
        try:
            stu_data = JSONParser().parse(request)
            id = stu_data.get("id")
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu,data=stu_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg":"updated"})
        except Exception as e:
            return JsonResponse({"error":"something wrong in query"})
    else:
        return JsonResponse({"msg":" its a GET request"})

