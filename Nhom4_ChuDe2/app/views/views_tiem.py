from django.shortcuts import render, redirect

# 1. TRANG ĐĂNG KÝ TIỆM (Sửa lỗi AttributeError bà vừa gặp)
def register_tiem(request):
    # Trang này sẽ hiện giao diện đăng ký 4 bước như Figma
    return render(request, 'tiem/register.html')

# 2. DASHBOARD TIỆM HOA (Thống kê & Yêu cầu thiết kế mới)
def dashboard(request):
    # Dữ liệu giả để bà demo các con số trên Dashboard Tiệm
    context = {
        'stats': {
            'revenue': '15.500.000đ',
            'orders_count': 42,
            'new_requests': 5,
            'shop_name': 'Lavender Studio'
        },
        'yeu_cau_cho': [
            {'id': 101, 'khach': 'Nguyễn Lệ Uyên', 'ngan_sach': '500.000đ', 'dip': 'Sinh nhật', 'status': 'Chờ báo giá'},
            {'id': 102, 'khach': 'Trần Minh Quân', 'ngan_sach': '1.200.000đ', 'dip': 'Khai trương', 'status': 'Chờ báo giá'},
        ],
        'don_hang_dang_lam': [
            {'id': 'ORD-9618', 'khach': 'Phạm Hải Nam', 'status': 'Đang cắm hoa'},
        ]
    }
    return render(request, 'tiem/dashboard.html', context)

# 3. QUẢN LÝ ĐƠN HÀNG (Danh sách đơn và cập nhật tiến độ)
def manage_orders(request):
    orders_list = [
        {'id': '9618', 'khach': 'Phạm Hải Nam', 'sp': 'Bó hồng đỏ 50 bông', 'status': 'Đang thực hiện'},
        {'id': '9619', 'khach': 'Lê Thị Bình', 'sp': 'Lẵng hoa hướng dương', 'status': 'Hoàn thành'},
        {'id': '9620', 'khach': 'Hoàng Nam', 'sp': 'Bó hoa Tulip trắng', 'status': 'Đã hủy'},
    ]
    return render(request, 'tiem/manage_orders.html', {'orders': orders_list})

# 4. GỬI BÁO GIÁ (Khi tiệm ấn nút "Gửi báo giá" cho một yêu cầu)
def send_quote(request, req_id):
    # Truyền req_id sang để biết là đang báo giá cho yêu cầu nào
    return render(request, 'tiem/send_quote.html', {'req_id': req_id})

# 5. HỒ SƠ NĂNG LỰC (Nơi tiệm cập nhật ảnh mẫu sản phẩm)
def profile(request):
    return render(request, 'tiem/profile.html')