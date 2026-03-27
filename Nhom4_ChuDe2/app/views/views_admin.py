from django.shortcuts import render, redirect


def login_admin(request):
    error = None
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        # TÀI KHOẢN GIẢ ĐỊNH ĐỂ TEST GIAO DIỆN
        if u == "admin" and p == "123456":
            # Lưu trạng thái đăng nhập giả vào Session để các trang khác biết
            request.session['is_admin_logged_in'] = True
            return redirect('admin_dashboard')
        else:
            error = "Sai tài khoản hoặc mật khẩu admin rồi!"

    return render(request, 'admin/login_admin.html', {'error': error})


def logout_admin(request):
    # Xóa session khi đăng xuất
    if 'is_admin_logged_in' in request.session:
        del request.session['is_admin_logged_in']
    return redirect('login_admin')


# Trang Dashboard (Kiểm tra session giả)
def admin_dashboard(request):
    if not request.session.get('is_admin_logged_in'):
        return redirect('login_admin')

    active_tab = request.GET.get('tab', 'doanh_thu')
    context = {
        'total_revenue': '128.450.000đ',
        'total_orders': '1,240',
        'new_users': '456',
        'users_count': '8,330',
        'active_tab': active_tab,
    }
    return render(request, 'admin/dashboard.html', context)


# Trang Quản lý người dùng (Kiểm tra session giả)
def user_management(request):
    if not request.session.get('is_admin_logged_in'):
        return redirect('login_admin')

    tiems_cho_duyet = [
        {'id': 1, 'ten': 'Hồng Hạc Shop', 'chu_tiem': 'Nguyễn Thúy', 'ngay_dk': '26/03/2026', 'status': 'Chờ duyệt'},
    ]
    khach_hangs = [
        {'ten': 'Nguyễn Văn Hùng', 'email': 'hung.nv@gmail.com', 'role': 'Khách hàng', 'status': 'Hoạt động'},
        {'ten': 'Lê Minh Tuấn', 'email': 'tuan.florist@gmail.com', 'role': 'Chủ tiệm', 'status': 'Hoạt động'},
    ]
    context = {'tiems': tiems_cho_duyet, 'users': khach_hangs}
    return render(request, 'admin/user_management.html', context)
