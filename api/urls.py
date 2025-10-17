from django.urls import path
from .views import (
    SanPhamListCreateAPIView,
    SanPhamDetailAPIView, # Thêm import này
    NhaCungCapListCreateAPIView,
    NhaCungCapDetailAPIView, # Thêm import này
    KhachHangListCreateAPIView,
    KhachHangDetailAPIView ,# Thêm import này
    DonHangListCreateAPIView, # Thêm import này
    DonHangDetailAPIView, # Thêm import này
    PhieuNhapKhoListCreateAPIView # Thêm import
)

urlpatterns = [
    # URLs cho Sản Phẩm
    path('products/', SanPhamListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', SanPhamDetailAPIView.as_view(), name='product-detail'), # URL mới

    # URLs cho Nhà Cung Cấp
    path('suppliers/', NhaCungCapListCreateAPIView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', NhaCungCapDetailAPIView.as_view(), name='supplier-detail'), # URL mới

    # URLs cho Khách Hàng
    path('customers/', KhachHangListCreateAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', KhachHangDetailAPIView.as_view(), name='customer-detail'), # URL mới
     # URLs cho Đơn Hàng
    path('orders/', DonHangListCreateAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', DonHangDetailAPIView.as_view(), name='order-detail'),
    # URL cho Phiếu Nhập Kho
    path('goods-receipts/', PhieuNhapKhoListCreateAPIView.as_view(), name='goods-receipt-list'),

   
]