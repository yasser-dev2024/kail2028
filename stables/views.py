from django.shortcuts import render
from .models import Horse

def home(request):
    # أحدث الخيول أولاً
    horses = Horse.objects.order_by('-id')
    return render(request, 'stables/home.html', {'horses': horses})
