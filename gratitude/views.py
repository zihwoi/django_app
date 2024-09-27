from django.shortcuts import render
from .models import GratitudeEntry
# Create your views here.

def home(request):
    entries = GratitudeEntry.objects.all()
    return render(request, 'gratitude/home.html', {'entries': entries})
