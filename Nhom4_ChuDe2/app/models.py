from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 1. Thông tin chung (Dùng để phân quyền)
class TaiKhoan(models.Model):
    VAI_TRO_CHOICES = [
        ('KHACH_HANG', 'Khách hàng'),
        ('TIEM_HOA', 'Tiệm hoa'),
        ('ADMIN', 'Quản trị viên'),
    ]
    ten_dang_nhap = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mat_khau = models.CharField(max_length=128)
    so_dien_thoai = models.CharField(max_length=15, blank=True, null=True)
    vai_tro = models.CharField(max_length=20, choices=VAI_TRO_CHOICES)
    trang_thai = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ten_dang_nhap} ({self.vai_tro})"

# 2. Actor: Khách hàng
class KhachHang(models.Model):
    tai_khoan = models.OneToOneField(TaiKhoan, on_delete=models.CASCADE, primary_key=True)
    ten_khach_hang = models.CharField(max_length=255)
    dia_chi = models.TextField(blank=True, null=True)

# 3. Actor: Tiệm hoa
class TiemHoa(models.Model):
    tai_khoan = models.OneToOneField(TaiKhoan, on_delete=models.CASCADE, primary_key=True)
    ten_tiem_hoa = models.CharField(max_length=255)
    mo_ta = models.TextField(blank=True, null=True)
    ma_so_thue = models.CharField(max_length=50, blank=True, null=True)
    hinh_anh_san_pham = models.ImageField(upload_to='tiem_hoa/products/', blank=True, null=True)
    logo_tiem_hoa = models.ImageField(upload_to='tiem_hoa/logos/', blank=True, null=True)
    trang_thai_duyet = models.BooleanField(default=False)

# 4. Nghiệp vụ: Yêu cầu thiết kế
class YeuCauThietKe(models.Model):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    tiem_hoa = models.ForeignKey(TiemHoa, on_delete=models.CASCADE)
    dip_su_dung = models.CharField(max_length=255)
    ngan_sach = models.DecimalField(max_digits=12, decimal_places=0) # Tiền VNĐ không cần số lẻ
    mau_sac = models.CharField(max_length=100)
    thoi_gian_hoan_thanh = models.DateTimeField()
    phong_cach = models.CharField(max_length=255)
    ghi_chu = models.TextField(blank=True, null=True)
    dia_chi_giao_hang = models.TextField()

# 5. Nghiệp vụ: Báo giá
class BaoGia(models.Model):
    yeu_cau = models.ForeignKey(YeuCauThietKe, on_delete=models.CASCADE)
    chi_phi_thiet_ke = models.DecimalField(max_digits=12, decimal_places=0)
    phi_van_chuyen = models.DecimalField(max_digits=12, decimal_places=0)
    tong_tien = models.DecimalField(max_digits=12, decimal_places=0)
    anh_mau_de_xuat = models.ImageField(upload_to='baogia/samples/', blank=True, null=True)
    noi_dung_tu_van = models.TextField()
    trang_thai = models.CharField(max_length=50, default='ChoDuyet')

# 6. Nghiệp vụ: Đơn hàng
class DonHang(models.Model):
    bao_gia = models.OneToOneField(BaoGia, on_delete=models.CASCADE)
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    ngay_dat = models.DateTimeField(auto_now_add=True)
    anh_san_pham_thuc_te = models.ImageField(upload_to='orders/actual/', blank=True, null=True)
    trang_thai_don_hang = models.CharField(max_length=50, default='DangXuLy')
    ngay_giao_du_kien = models.DateTimeField()

# 7. Nghiệp vụ: Thanh toán
class ThanhToan(models.Model):
    don_hang = models.OneToOneField(DonHang, on_delete=models.CASCADE)
    so_tai_khoan = models.CharField(max_length=50)
    ten_ngan_hang = models.CharField(max_length=100)
    ten_chu_tai_khoan = models.CharField(max_length=255)
    qr_tiem_hoa = models.ImageField(upload_to='payments/qr/', blank=True, null=True)
    tong_tien = models.DecimalField(max_digits=12, decimal_places=0)
    hinh_anh_bien_lai = models.ImageField(upload_to='payments/receipts/')

# 8. Tương tác: Đánh giá và Chat
class DanhGia(models.Model):
    don_hang = models.OneToOneField(DonHang, on_delete=models.CASCADE)
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    tiem_hoa = models.ForeignKey(TiemHoa, on_delete=models.CASCADE)
    so_sao = models.IntegerField(default=5)
    noi_dung = models.TextField()
    ngay_danh_gia = models.DateTimeField(auto_now_add=True)

class PhienChat(models.Model):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    tiem_hoa = models.ForeignKey(TiemHoa, on_delete=models.CASCADE)
    thoi_gian_tao = models.DateTimeField(auto_now_add=True)

class ChatBox(models.Model):
    phien_chat = models.ForeignKey(PhienChat, on_delete=models.CASCADE)
    nguoi_gui = models.ForeignKey(TaiKhoan, on_delete=models.CASCADE)
    noi_dung = models.TextField()
    thoi_gian = models.DateTimeField(auto_now_add=True)