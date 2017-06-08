from django.shortcuts import render
from django.utils import timezone
from .models import Hanzi

from random import randint

# Create your views here.
def hanzi_list(request):
	hanzis = Hanzi.objects.exclude(classifiers=None).order_by('?')[:6]
	return render(request, 'hanzi/hanzi_list.html', {'hanzis': hanzis})