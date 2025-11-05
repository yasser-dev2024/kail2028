from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
            return redirect('ops:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل.")
            return redirect('ops:register')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect('ops:login')

    return render(request, 'ops/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح!")
            return redirect('ops:dashboard')  # عدّل الوجهة لاحقًا حسب تطبيقك
        else:
            messages.error(request, "بيانات الدخول غير صحيحة.")

    return render(request, 'ops/login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح.")
    return redirect('ops:login')
