from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from stables.models import Horse, NewsTicker

def home_view(request):
    horses = Horse.objects.order_by('-id')
    ticker = NewsTicker.objects.filter(is_active=True).order_by('-updated_at').first()
    return render(request, 'home.html', {'horses': horses, 'ticker': ticker})

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
    path('finance/', include('finance.urls')),
    path('ops/', include('ops.urls')),
    path('stables/', include('stables.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
