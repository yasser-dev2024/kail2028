from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_view(request):
    """عرض إنشاء حساب جديد"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        # تحقق من تطابق كلمتي المرور
        if password != confirm:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
            return redirect('ops:register')

        # تحقق من أن اسم المستخدم غير مستخدم مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل.")
            return redirect('ops:register')

        # إنشاء المستخدم
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "تم إنشاء الحساب بنجاح ✅ يمكنك الآن تسجيل الدخول.")
        return redirect('ops:login')

    return render(request, 'ops/register.html')


def login_view(request):
    """عرض تسجيل الدخول"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"مرحبًا {user.username} 👋 تم تسجيل دخولك بنجاح!")
            # إعادة التوجيه لصفحة لوحة التحكم أو الصفحة الرئيسية
            return redirect('ops:dashboard')
        else:
            messages.error(request, "بيانات الدخول غير صحيحة. حاول مرة أخرى.")

    return render(request, 'ops/login.html')


@login_required
def logout_view(request):
    """تسجيل خروج المستخدم الحالي"""
    logout(request)
    messages.success(request, "تم تسجيل خروجك بنجاح ✅")
    return redirect('ops:login')


@login_required
def dashboard_view(request):
    """صفحة افتراضية بعد تسجيل الدخول"""
    return render(request, 'ops/dashboard.html', {
        'username': request.user.username
    })
