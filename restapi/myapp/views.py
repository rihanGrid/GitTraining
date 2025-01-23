from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import studentSerializers

# Create your views here.
class StudentListCreateAPIView(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = studentSerializers(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetailAPIView(APIView):
    def get(self, request, pk):
        students = Students.objects.get(pk=pk)
        serializer = studentSerializers(students)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = Students.objects.get(pk=pk)
        serializer = studentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = Students.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

