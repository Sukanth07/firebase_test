from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
# Create your views here.
def home(request):

    name = request.POST.get('name')
    return HttpResponse(f"hello, {name}")
