from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import cv2
#import os

#current_directory = os.path.dirname(os.path.abspath(__file__))
#jewellery_img_path = os.path.join(current_directory, 'jewellery8.png')
#jewellery_img = cv2.imread(jewellery_img_path, -1)

@csrf_exempt
@api_view(['POST'])
# Create your views here.
def home(request):

    user_face = request.POST.get('user_face')
    jewellery = request.POST.get('jewellery')
    cv2.imread(user_face,-1)
    cv2.imread(jewellery,-1)
    message = "image got successfully"
    return HttpResponse(message)
