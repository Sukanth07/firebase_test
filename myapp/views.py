from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import cv2

@csrf_exempt
@api_view(['POST'])
# Create your views here.
def home(request):

    user_face = request.POST.get('url')
    cv2.imread(user_face,-1)
    message = "image got successfully"
    return HttpResponse(message)
