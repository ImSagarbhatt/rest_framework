from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def listview(request):
    """
    to view the all the serializer data
    """
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return Response(serializer.data)

@api_view()
def detailview(request,pk):
    '''
    to get the one object
    '''
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    return Response(serializer.data)

@csrf_exempt
@api_view(["GET","POST"])
def createview(request):
    """
    to add the create the object
    """
    if request.method == "POST":
        stu_data= request.data
        serializer = StudentSerializer(data = stu_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response(serializer.data)

@csrf_exempt
@api_view(["PUT"])
def updateview(request):
    """
    to update the value of object
    """
    if request.method == "PUT":
        try:
            stu_data = request.data
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


@csrf_exempt
@api_view(["DELETE"])
def deleteview(request):
    """
    delete the object
    """
    if request.method =="DELETE":
        try:
            stu_data = request.data
            id = stu_data.get("id")
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({"msg":"Deleted successfully"})
        except Exception:
            return Response({"msg":"Object not found!!"})
    else:
        return Response({"msg":" Its a GET request!!"})


