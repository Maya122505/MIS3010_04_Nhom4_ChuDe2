from django.urls import path
from .views import views_khach, views_tiem, views_admin
from . import views

urlpatterns = [
    # --- LUỒNG CHUNG ---
    path('login/', views_khach.login_view, name='login'),
    path('logout/', views_khach.logout_view, name='logout'),
    path('success/', views_khach.success_view, name='success'),

    # --- LUỒNG KHÁCH HÀNG (CUSTOMER) ---
    # path('', views_khach.home, name='home'),
    # path('register/khach/', views_khach.register_khach, name='register_khach'),
    # path('shop/<int:id>/', views_khach.shop_detail, name='shop_detail'),
    # path('tao-yeu-cau/', views_khach.create_request, name='create_request'),
    # path('xem-bao-gia/', views_khach.confirm_quote, name='confirm_quote'),
    # path('thanh-toan/<int:order_id>/', views_khach.payment, name='payment'),
    # path('theo-doi-don-hang/', views_khach.order_status, name='order_status'),
    # --- LUỒNG KHÁCH HÀNG ---
    path('', views_khach.home_view, name='home'),
    path('after-login/', views_khach.after_login_view, name='after_login'),
    path('after_login/', views_khach.after_login_view, name='after_login_alias'),
    path('search-landing/', views_khach.search_landing_view, name='search_landing'),
    path('search-results/', views_khach.search_results_view, name='search_results'),
    path('detail-logged/<int:id>/', views_khach.detail_logged_view, name='detail_logged'),
    path('request/<int:id>/', views_khach.request_create_view, name='request_create'),
    path('request/<int:id>/pending/', views_khach.request_pending_view, name='request_pending'),
    path('chat/<int:id>/', views_khach.chat_kh_view, name='chat_kh'),
    path('quote/<int:id>/', views_khach.quote_confirm_view, name='quote_confirm'),
    path('payment/<int:id>/', views_khach.payment_view, name='payment'),
    path('orders/', views_khach.order_status_view, name='order_status'),
    path('orders/<int:id>/', views_khach.order_status_detail_view, name='order_status_detail'),
    path('orders/<int:id>/done/', views_khach.order_status_detail_done_view, name='order_status_detail_done'),
    path('orders/<int:id>/review/', views_khach.review_service_view, name='review_service'),
    path('orders/<int:id>/review/done/', views_khach.review_service_done_view, name='review_service_done'),
    path('search/', views_khach.search_view, name='search'),
    path('detail/<int:id>/', views_khach.detail_view, name='detail'),

    # --- AUTHENTICATION ---
    path('login/', views_khach.login_view, name='login'),
    path('logout/', views_khach.logout_view, name='logout'),
    path('register/', views_khach.register_view, name='register'),
    path('success/', views_khach.success_view, name='success'),
    # --- LUỒNG TIỆM HOA (VENDOR) ---
    path('register/tiem/', views_tiem.register_tiem, name='register_tiem'),
    path('vendor/dashboard/', views_tiem.dashboard, name='vendor_dashboard'),
    path('vendor/quan-ly-don/', views_tiem.manage_orders, name='vendor_orders'),
    path('vendor/gui-bao-gia/<int:req_id>/', views_tiem.send_quote, name='send_quote'),

    # --- LUỒNG QUẢN TRỊ (ADMIN) ---
    path('admin-hub/dashboard/', views_admin.admin_dashboard, name='admin_dashboard'),
    path('admin-hub/users/', views_admin.user_management, name='admin_users'),
]
