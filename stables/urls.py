from django.urls import path
from . import views

app_name = 'stables'

urlpatterns = [
    # ✅ الصفحة الرئيسية - الآن تستخدم home.html من المسار الرئيسي templates/
    path('', views.home, name='home'),

    # ✅ صفحة تفاصيل الحصان
    path('horse/<int:horse_id>/', views.horse_detail, name='horse_detail'),

    # ✅ إضافة للسلة
    path('add/<int:horse_id>/', views.add_to_cart, name='add_to_cart'),

    # ✅ عرض السلة
    path('cart/', views.view_cart, name='view_cart'),

    # ✅ إزالة عنصر من السلة
    path('remove/<int:horse_id>/', views.remove_from_cart, name='remove_from_cart'),
]
