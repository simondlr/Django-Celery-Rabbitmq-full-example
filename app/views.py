# Create your views here.
from django.http import HttpResponse
from app import tasks

def test_celery(request):
	result = tasks.sleeptask.delay(10)
	filter_one = tasks.sleeptask.delay(10)
	filter_two = tasks.sleeptask.delay(10)
	return HttpResponse(result.task_id)

