from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from stables.models import Horse, NewsTicker


def home_view(request):
    """عرض الصفحة الرئيسية (home.html) من المسار الرئيسي"""
    horses = Horse.objects.order_by('-id')
    ticker = NewsTicker.objects.filter(is_active=True).order_by('-updated_at').first()
    cart = request.session.get('cart', [])
    cart_count = len(cart)
    return render(request, 'home.html', {
        'horses': horses,
        'ticker': ticker,
        'cart_count': cart_count,
    })


urlpatterns = [
    # ✅ الصفحة الرئيسية للموقع بالكامل
    path('', home_view, name='home'),

    # ✅ لوحة التحكم
    path('admin/', admin.site.urls),

    # ✅ التطبيقات الداخلية
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
    path('finance/', include('finance.urls')),
    path('ops/', include('ops.urls')),
    path('stables/', include('stables.urls')),
]

# ✅ تحميل الصور أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
