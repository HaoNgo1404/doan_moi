from rest_framework import generics
from .models import SanPham, NhaCungCap, KhachHang
from .serializers import SanPhamSerializer, NhaCungCapSerializer, KhachHangSerializer


# View để xem danh sách và tạo mới Sản Phẩm
class SanPhamListCreateAPIView(generics.ListCreateAPIView):
    queryset = SanPham.objects.all()
    serializer_class = SanPhamSerializer

# View để xem danh sách và tạo mới Nhà Cung Cấp
class NhaCungCapListCreateAPIView(generics.ListCreateAPIView):
    queryset = NhaCungCap.objects.all()
    serializer_class = NhaCungCapSerializer

# View để xem danh sách và tạo mới Khách Hàng
class KhachHangListCreateAPIView(generics.ListCreateAPIView):
    queryset = KhachHang.objects.all()
    serializer_class = KhachHangSerializer

    # ... (giữ nguyên các import và các class View đã có)

# View để xem chi tiết, cập nhật, xóa một Sản Phẩm
class SanPhamDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SanPham.objects.all()
    serializer_class = SanPhamSerializer

# View để xem chi tiết, cập nhật, xóa một Nhà Cung Cấp
class NhaCungCapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NhaCungCap.objects.all()
    serializer_class = NhaCungCapSerializer

# View để xem chi tiết, cập nhật, xóa một Khách Hàng
class KhachHangDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KhachHang.objects.all()
    serializer_class = KhachHangSerializer
    # ... (giữ nguyên các import và View đã có)
from .models import DonHang
from .serializers import DonHangSerializer

# View để xem danh sách và tạo mới Đơn Hàng
class DonHangListCreateAPIView(generics.ListCreateAPIView):
    queryset = DonHang.objects.all()
    serializer_class = DonHangSerializer

# View để xem chi tiết, cập nhật, xóa một Đơn Hàng
class DonHangDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonHang.objects.all()
    serializer_class = DonHangSerializer
    # ... (giữ nguyên các import và View đã có)
from .models import PhieuNhapKho
from .serializers import PhieuNhapKhoSerializer

class PhieuNhapKhoListCreateAPIView(generics.ListCreateAPIView):
    queryset = PhieuNhapKho.objects.all()
    serializer_class = PhieuNhapKhoSerializer