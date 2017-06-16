from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Hanzi
from .models import Test

from random import randint

# Create your views here.
def hanzi_list(request):
	hanzis = Hanzi.objects.exclude(classifiers=None).order_by('?')[:6]
	return render(request, 'hanzi/hanzi_list.html', {'hanzis': hanzis})
	
def test_card_list(request, pk):
        test = get_object_or_404(Test, pk=pk)
        hanzis = test.hanzis.all().order_by('?')[:6]
        return render(request, 'hanzi/test_card_list.html', {'hanzis': hanzis})