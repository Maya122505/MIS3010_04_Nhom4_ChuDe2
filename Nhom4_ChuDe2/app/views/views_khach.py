from django.shortcuts import render, redirect
from django.contrib.auth import logout

# --- 1. TRANG CHỦ ---
def home_view(request):
    return render(request, 'khach/index.html')

# --- 2. XỬ LÝ TÌM KIẾM ---
def search_view(request):
    # Lấy từ khóa từ ô nhập liệu (form GET có name="q")
    query = request.GET.get('q', '').strip()

    # LOGIC ĐẶC BIỆT: Nếu gõ đúng "Lavender Studio" -> Nhảy thẳng sang trang chi tiết
    if query.lower() == "lavender studio":
        # 'detail' là name trong urls.py, id=1 là ví dụ ID của tiệm này
        return redirect('detail', id=1)

    # LOGIC HIỂN THỊ KẾT QUẢ:
    flower_shops = []
    if query:
        # Nếu gõ "Lalala" -> Trả về danh sách rỗng để hiện màn hình "Không tìm thấy"
        if query.lower() == "lalala":
            flower_shops = []
        else:
            # Các từ khóa khác -> Giả lập trả về 5 kết quả (range 5)
            flower_shops = range(5)
    else:
        # Nếu vào trang search mà chưa nhập gì, mặc định hiện 5 tiệm tiêu biểu
        flower_shops = range(5)

    return render(request, 'khach/search.html', {
        'flower_shops': flower_shops,
        'query': query
    })

# --- 3. CHI TIẾT TIỆM HOA ---
def detail_view(request, id=None):
    # Tham số id nhận giá trị từ URL (ví dụ: /detail/1/)
    return render(request, 'khach/detail.html', {'id': id})

# --- 4. HỆ THỐNG TÀI KHOẢN (AUTH) ---

def login_view(request):
    # Trả về giao diện đăng nhập
    return render(request, 'khach/login.html')

def register_view(request):
    # Nếu người dùng nhấn nút gửi form (POST)
    if request.method == 'POST':
        # Sau này xử lý lưu User tại đây
        return redirect('login')
    # Nếu chỉ xem trang
    return render(request, 'khach/register.html')

def logout_view(request):
    # Xóa phiên đăng nhập
    logout(request)
    # Quay về trang chủ
    return redirect('home')

# --- 5. CÁC TRANG TRẠNG THÁI KHÁC ---

def success_view(request):
    # Trang thông báo thành công (ví dụ sau khi đặt hàng/đăng ký)
    return render(request, 'khach/success.html')

def pending_view(request):
    # Trang chờ xử lý
    return render(request, 'khach/pending.html')

def after_login_view(request):
    # Trang giao diện sau khi đăng nhập (chỉ frontend)
    return render(request, 'khach/after_login.html')

def search_landing_view(request):
    # Trang tìm kiếm tiệm hoa (bước 1)
    query = request.GET.get('q', '').strip()
    return render(request, 'khach/search_landing.html', {'query': query})

def search_results_view(request):
    # Trang kết quả tìm kiếm (bước 2)
    query = request.GET.get('q', '').strip()
    return render(request, 'khach/search_results.html', {'query': query})

def detail_logged_view(request, id=None):
    # Trang chi tiết tiệm hoa cho user đã đăng nhập
    return render(request, 'khach/detail_logged.html', {'id': id})

def request_create_view(request, id=None):
    # Trang tạo yêu cầu (bước 1)
    return render(request, 'khach/request_create.html', {'id': id})

def request_pending_view(request, id=None):
    # Trang chờ phê duyệt (bước 2)
    return render(request, 'khach/request_pending.html', {'id': id})

def chat_kh_view(request, id=None):
    # Trang chatbox khách hàng
    return render(request, 'khach/chatbox_kh.html', {'id': id})

def quote_confirm_view(request, id=None):
    # Trang xác nhận báo giá
    return render(request, 'khach/quote_confirm.html', {'id': id})

def payment_view(request, id=None):
    # Trang thanh toán
    return render(request, 'khach/payment.html', {'id': id})

def order_status_view(request):
    # Trang theo dõi trạng thái đơn
    return render(request, 'khach/order_status.html')

def order_status_detail_view(request, id=None):
    # Trang chi tiết trạng thái đơn
    return render(request, 'khach/order_status_detail.html', {'id': id})

def order_status_detail_done_view(request, id=None):
    # Trang chi tiết đơn hoàn thành
    return render(request, 'khach/order_status_detail_done.html', {'id': id})

def review_service_view(request, id=None):
    # Trang đánh giá dịch vụ
    return render(request, 'khach/review_service.html', {'id': id})

def review_service_done_view(request, id=None):
    # Trang đánh giá dịch vụ (bước 2)
    return render(request, 'khach/review_service_done.html', {'id': id})

