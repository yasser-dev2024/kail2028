# kail2028/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from stables.models import Horse  # نمرّر الخيول للصفحة الرئيسية

# الصفحة الرئيسية تستخدم templates/home.html (الموجود أصلًا)
def home_view(request):
    horses = Horse.objects.order_by('-id')
    return render(request, 'home.html', {'horses': horses})

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

    # تطبيقات محلية
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
    path('finance/', include('finance.urls')),
    path('ops/', include('ops.urls')),
    path('stables/', include('stables.urls')),
]

# ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
