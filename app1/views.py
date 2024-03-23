from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from app1.models import Task
# import requests

class Test(APIView):
    def get(self, request):
        return Response({"message":"Success bro !!!!!"})


class GetWeatherData(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def is_location_valid(self, latitude, longitude):
        return latitude>=-90 and latitude<=90 and longitude>=-180 and longitude<=180

    def get(self, request):
        latitude = float(request.GET.get('latitude'))
        longitude = float(request.GET.get('longitude'))

        if not self.is_location_valid(latitude, longitude):
            return Response({"message":"Invalid coordinates"}, status=400)

        return Response({"temperature":10, "humidity":10, "weather description":"Humid weather"})

class TaskView(APIView):
    def get(self, request):
        try:
            task_id = int(request.GET.get("id"))
            task = Task.objects.get(id=task_id)
            return Response({"task_id":task.id, "title":task.title, "status":task.status})
        except Task.DoesNotExist:
            return Response({"message":"Invalid task id"}, status=400)

    def post(self, request):
        try:
            import json
            title = json.loads(request.body).get("title")
            status = json.loads(request.body).get("status")

            task = Task.objects.create(title=title, status=status)

            return Response({"task_id":task.id, "message":"Updated succesfully"})
        except:
            return Response({"message":"Internal error"}, status=500)


    def put(self, request):
        try:
            import json
            task_id = json.loads(request.body).get("id")
            title = json.loads(request.body).get("title")
            status = json.loads(request.body).get("status")

            task = Task.objects.get(id=task_id)
            task.title = title
            task.status = status
            task.save()

            return Response({"task_id":task.id, "message":"Updated succesfully"})
        except Task.DoesNotExist:
            return Response({"message":"Invalid task id"}, status=400)

    def delete(self, request):
        try:
            import json
            task_id = json.loads(request.body).get("id")
            task = Task.objects.get(id=task_id)
            task.delete()
        except Task.DoesNotExist:
            return Response({"message":"Invalid task id"}, status=400)
