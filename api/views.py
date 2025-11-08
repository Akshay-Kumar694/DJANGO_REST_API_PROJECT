from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({"message": f"Hello, {request.user.username}!"})

def home(request):
    return JsonResponse({"message": "Welcome to the Django REST API!"})

# Create your views here.
