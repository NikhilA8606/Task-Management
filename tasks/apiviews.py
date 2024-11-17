from django.views import View
from django.http.response import JsonResponse
from tasks.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer  
from rest_framework.viewsets import ModelViewSet

class TaskSerializer(ModelSerializer):
    
    class Meta:
        model = Task
        fields = ["title","description","completed"]

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListAPI(APIView):
    def get(self,request):
        tasks = Task.objects.filter(deleted_data=False)
        data = TaskSerializer(tasks,many=True).data
        return Response({"task":data})
        

    