from django.shortcuts import render, redirect


# 1. TRANG THỐNG KÊ (Hàm này đổ số vào 3 cái Card Hồng-Xanh-Tím và Biểu đồ)
def admin_dashboard(request):
    # Lấy tab đang chọn từ URL (mặc định là doanh_thu)
    active_tab = request.GET.get('tab', 'doanh_thu')

    context = {
        'total_revenue': '128.450.000đ',
        'total_orders': '1,240',
        'new_users': '456',

        # SỐ LIỆU MỚI CHO TAB NGƯỜI DÙNG
        'users_count': '8,330',

        'active_tab': active_tab,  # Truyền cái này sang HTML
    }
    return render(request, 'admin/dashboard.html', context)
# 2. TRANG QUẢN LÝ NGƯỜI DÙNG (Duyệt tiệm và quản lý khách)
def user_management(request):
    # Dữ liệu tiệm đang chờ duyệt (tiems)
    tiems_cho_duyet = [
        {'id': 1, 'ten': 'Hồng Hạc Shop', 'chu_tiem': 'Nguyễn Thúy', 'ngay_dk': '26/03/2026', 'status': 'Chờ duyệt'},
    ]

    # Dữ liệu khách hàng/chủ tiệm (users)
    khach_hangs = [
        {'ten': 'Nguyễn Văn Hùng', 'email': 'hung.nv@gmail.com', 'role': 'Khách hàng', 'status': 'Hoạt động'},
        {'ten': 'Lê Minh Tuấn', 'email': 'tuan.florist@gmail.com', 'role': 'Chủ tiệm', 'status': 'Hoạt động'},
        {'ten': 'Phạm Minh Hải', 'email': 'hai.pm98@gmail.com', 'role': 'Khách hàng', 'status': 'Bị khóa'},
        {'ten': 'Trần Thùy Linh', 'email': 'linh.tran.boutique@gmail.com', 'role': 'Chủ tiệm', 'status': 'Hoạt động'},
    ]

    context = {
        'tiems': tiems_cho_duyet,
        'users': khach_hangs
    }
    return render(request, 'admin/user_management.html', context)