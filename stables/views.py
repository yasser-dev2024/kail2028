from django.shortcuts import render, redirect, get_object_or_404
from .models import Horse


def get_cart_count(request):
    """إرجاع عدد العناصر في السلة"""
    return len(request.session.get('cart', []))


def home(request):
    """عرض الصفحة الرئيسية مع الخيول (القالب في المسار الرئيسي templates/home.html)"""
    horses = Horse.objects.order_by('-id')
    cart_count = get_cart_count(request)
    return render(request, 'home.html', {   # ✅ تعديل هنا فقط
        'horses': horses,
        'cart_count': cart_count
    })


def horse_detail(request, horse_id):
    """عرض تفاصيل حصان"""
    horse = get_object_or_404(Horse, id=horse_id)
    cart_count = get_cart_count(request)
    return render(request, 'stables/horse_detail.html', {
        'horse': horse,
        'cart_count': cart_count
    })


def add_to_cart(request, horse_id):
    """إضافة حصان للسلة"""
    horse = get_object_or_404(Horse, id=horse_id)
    cart = request.session.get('cart', [])
    if horse_id not in cart:
        cart.append(horse_id)
        request.session['cart'] = cart
    return redirect('stables:home')


def view_cart(request):
    """عرض محتويات السلة"""
    cart = request.session.get('cart', [])
    horses = Horse.objects.filter(id__in=cart)
    cart_count = len(cart)
    return render(request, 'stables/cart.html', {
        'horses': horses,
        'cart_count': cart_count
    })


def remove_from_cart(request, horse_id):
    """إزالة حصان من السلة"""
    cart = request.session.get('cart', [])
    if horse_id in cart:
        cart.remove(horse_id)
        request.session['cart'] = cart
    return redirect('stables:view_cart')
