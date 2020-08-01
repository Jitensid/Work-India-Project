from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.models import User
import urllib
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login

class register_API(APIView):

    def post(self, request, *args, **kwargs):
	    # serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status" : "account created"})

        return JsonResponse({"status" : "Failed"})
        
# class login_API(APIView):

#     def post(self, request, *args, **kwargs):

#     	username = request.data.get("username","")       

#     	password = request.data.get("password","")

#     	user = authenticate(username=username,password=password)

#     	if user is not None:
#     		# login(request=request,user=user)
#     		return JsonResponse({"status" : "Success","userId" : str(user.id)})

#     	return JsonResponse({"status" : "Failed"})

class login_API(APIView):

    def post(self, request, *args, **kwargs):

        username = request.data.get("username","")

        password = request.data.get("password","")

        user = authenticate(username=username, password=password)

        if user is not None:

            return JsonResponse({"status" : "Sucess","userId" : str(user.id)})

        return JsonResponse({"status" : "Failed"})