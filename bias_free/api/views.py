from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .utils import article_scorer
import requests

# Create your views here.

diff_api="0aa0a812950dd24ec099ba19c1391ea1"

main_url="https://api.diffbot.com/v3/analyze?token="+diff_api+"&url="

def main(url):
    m_url=main_url+url
    req=requests.get(m_url)
    text=req.json()['objects'][0]['text']
    return text

class getBias(APIView):

	def post(self, request):
		url = request.POST.get('url')
		text = main(url)
		bias = article_scorer(text)
		res = {'objectivity': json.loads(bias)}
		return Response(res, status=status.HTTP_200_OK)

