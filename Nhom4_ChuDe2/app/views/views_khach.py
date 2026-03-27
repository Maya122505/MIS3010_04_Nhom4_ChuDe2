from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('username')
        # Logic phân quyền demo: gõ đúng tên là đi đúng luồng
        if user_input == 'admin':
            return redirect('admin_users')
        elif user_input == 'tiemhoa':
            return redirect('vendor_dashboard')
        else:
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    return redirect('home')

def home(request):
    # Data giả cho trang chủ
    tiems = [
        {'id': 1, 'ten': 'Lavender Studio', 'anh': 'images/tiemhoa1.jpg', 'rate': 4.8},
        {'id': 2, 'ten': 'Hồng Hạc Shop', 'anh': 'images/tiemhoa2.jpg', 'rate': 4.9},
    ]
    return render(request, 'khach/home.html', {'tiem_hoas': tiems})

def shop_detail(request, id):
    return render(request, 'khach/shop_detail.html', {'id': id})

def create_request(request):
    return render(request, 'khach/create_request.html')

def confirm_quote(request):
    return render(request, 'khach/confirm_quote.html')

def payment(request, order_id):
    return render(request, 'khach/payment.html', {'order_id': order_id})

def order_status(request):
    return render(request, 'khach/order_status.html')

def success_view(request):
    return render(request, 'success.html')

def register_khach(request):
    return render(request, 'khach/register.html')