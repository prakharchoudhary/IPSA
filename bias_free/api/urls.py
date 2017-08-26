from django.conf.urls import url
from views import getBias

urlpatterns = [
	url(r'^bias$', getBias.as_view(), name='get-bias'),
]