from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
class getBias(APIView):

	def post(self, request, *args, **kwargs0:
		bias = get_agg_bias(*args, **kwargs)
		
