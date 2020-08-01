from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.models import User
import urllib
import json
from .models import Note
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
import base64
# Create your views here.
class ListAPI(APIView):

    def get(self, request, *args, **kwargs):

    	user_id = (request.query_params.get("id"))

    	user = User.objects.get(id=user_id)

    	i = 0

    	notes = Note.objects.filter(author = user)

    	context = dict()

    	for note in notes : 
    		i += 1

    		x = (note.text)

    		x = (x).encode("ascii")

    		x = base64.b64decode(x)

    		x = x.decode("ascii")

    		context["Note" + str(i)] = x

    	return JsonResponse(context)

class Save_Note(APIView):

	def post(self, request, *args, **kwargs):

		text = request.data.get("note","")

		user_id = request.query_params.get("id")

		user = User.objects.get(id=user_id)

		text = text.encode("ascii")

		text = base64.b64encode(text)

		text = text.decode("ascii")

		note = Note(text=text, author=user)

		note.save()

		return JsonResponse({"status" : "Success"})