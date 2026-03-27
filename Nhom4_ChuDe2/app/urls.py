from django.urls import path
from .views import views_khach, views_tiem, views_admin

urlpatterns = [
    # --- LUỒNG CHUNG ---
    path('login/', views_khach.login_view, name='login'),
    path('logout/', views_khach.logout_view, name='logout'),
    path('success/', views_khach.success_view, name='success'),

    # --- LUỒNG KHÁCH HÀNG (CUSTOMER) ---
    path('', views_khach.home, name='home'),
    path('register/khach/', views_khach.register_khach, name='register_khach'),
    path('shop/<int:id>/', views_khach.shop_detail, name='shop_detail'),
    path('tao-yeu-cau/', views_khach.create_request, name='create_request'),
    path('xem-bao-gia/', views_khach.confirm_quote, name='confirm_quote'),
    path('thanh-toan/<int:order_id>/', views_khach.payment, name='payment'),
    path('theo-doi-don-hang/', views_khach.order_status, name='order_status'),

    # --- LUỒNG TIỆM HOA (VENDOR) ---
    path('register/tiem/', views_tiem.register_tiem, name='register_tiem'),
    path('vendor/dashboard/', views_tiem.dashboard, name='vendor_dashboard'),
    path('vendor/quan-ly-don/', views_tiem.manage_orders, name='vendor_orders'),
    path('vendor/gui-bao-gia/<int:req_id>/', views_tiem.send_quote, name='send_quote'),

    # --- LUỒNG QUẢN TRỊ (ADMIN) ---
    path('admin-hub/dashboard/', views_admin.admin_dashboard, name='admin_dashboard'),
    path('admin-hub/users/', views_admin.user_management, name='admin_users'),
]