from django.shortcuts import render
from django.utils import timezone
from .models import Hanzi

# Create your views here.
def hanzi_list(request):
	#hanzis = Hanzi.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	hanzis = Hanzi.objects.order_by('?')[:6]
	return render(request, 'hanzi/hanzi_list.html', {'hanzis': hanzis})