from django.shortcuts import render, redirect

def login_shop(request):
    return render(request, 'tiem/login_shop.html')

# 1. TRANG ĐĂNG KÝ GIAN HÀNG
def register_tiem(request):
    return render(request, 'tiem/register.html')

# 1b. TRANG ĐĂNG KÝ GIAN HÀNG (URL RIÊNG)
def register_shop(request):
    return render(request, 'tiem/register_shop.html')


# 2. DASHBOARD TIỆM HOA
def dashboard(request):
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

# 3. QUẢN LÝ ĐƠN HÀNG
def manage_orders(request):
    orders_list = [
        {'id': '9618', 'khach': 'Phạm Hải Nam', 'sp': 'Bó hồng đỏ 50 bông', 'status': 'Đang thực hiện'},
        {'id': '9619', 'khach': 'Lê Thị Bình', 'sp': 'Lẵng hoa hướng dương', 'status': 'Hoàn thành'},
        {'id': '9620', 'khach': 'Hoàng Nam', 'sp': 'Bó hoa Tulip trắng', 'status': 'Đã hủy'},
    ]
    return render(request, 'tiem/manage_orders.html', {'orders': orders_list})

# 4. GỬI BÁO GIÁ
def send_quote(request, req_id):
    return render(request, 'tiem/send_quote.html', {'req_id': req_id})

# 5. HỒ SƠ NĂNG LỰC
def profile(request):
    return render(request, 'tiem/profile.html')

# 6. CẬP NHẬT HỒ SƠ NĂNG LỰC
def profile_edit(request):
    return render(request, 'tiem/profile_edit.html')

# 7. CHAT TIỆM
def chat(request):
    return render(request, 'tiem/chat.html')

# 8. DANH SÁCH ĐỀ XUẤT & BÁO GIÁ
def quotes(request):
    return render(request, 'tiem/quotes.html')

# 9. THỐNG KÊ KINH DOANH
def stats(request):
    return render(request, 'tiem/stats.html')

# 10. CHI TIẾT YÊU CẦU
def order_detail(request, order_id):
    return render(request, 'tiem/order_detail.html', {'order_id': order_id})
