from django.db import models
from django.contrib.auth.models import User # Sử dụng User có sẵn của Django cho Nhân viên

# Bảng Nhà Cung Cấp
class NhaCungCap(models.Model):
    ten_nha_cung_cap = models.CharField(max_length=255)
    thong_tin_lien_he = models.TextField(blank=True, null=True)
    dia_chi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ten_nha_cung_cap

# Bảng Nguyên Phụ Liệu (hàng nhập về)
class NguyenPhuLieu(models.Model):
    ten_nguyen_phu_lieu = models.CharField(max_length=255)
    don_vi_tinh = models.CharField(max_length=50)
    so_luong_ton_kho = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.ten_nguyen_phu_lieu

# Bảng Sản Phẩm (bán cho khách)
class SanPham(models.Model):
    ten_san_pham = models.CharField(max_length=255)
    mo_ta = models.TextField(blank=True, null=True)
    don_gia_ban = models.DecimalField(max_digits=10, decimal_places=2)
    hinh_anh_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ten_san_pham

# Bảng Khách Hàng
class KhachHang(models.Model):
    ho_ten = models.CharField(max_length=255)
    so_dien_thoai = models.CharField(max_length=15, unique=True)
    dia_chi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ho_ten

# Bảng Đơn Hàng
class DonHang(models.Model):
    TRANG_THAI_CHOICES = [
        ('CHO_XAC_NHAN', 'Chờ xác nhận'),
        ('DA_XAC_NHAN', 'Đã xác nhận'),
        ('DANG_GIAO', 'Đang giao'),
        ('HOAN_THANH', 'Hoàn thành'),
        ('DA_HUY', 'Đã hủy'),
    ]
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    nhan_vien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ngay_dat_hang = models.DateTimeField(auto_now_add=True)
    tong_gia_tri = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI_CHOICES, default='CHO_XAC_NHAN')

    def __str__(self):
        return f"Đơn hàng #{self.id} - {self.khach_hang.ho_ten}"

# Bảng Chi Tiết Đơn Hàng (nối Đơn Hàng và Sản Phẩm)
class ChiTietDonHang(models.Model):
    don_hang = models.ForeignKey(DonHang, related_name='chi_tiet', on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPham, on_delete=models.PROTECT)
    so_luong = models.PositiveIntegerField()
    don_gia = models.DecimalField(max_digits=10, decimal_places=2) # Lưu lại giá tại thời điểm mua

    def __str__(self):
        return f"{self.so_luong} x {self.san_pham.ten_san_pham}"
    # ... (giữ nguyên các model đã có)

# Bảng Phiếu Nhập Kho
class PhieuNhapKho(models.Model):
    nha_cung_cap = models.ForeignKey(NhaCungCap, on_delete=models.PROTECT)
    nhan_vien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ngay_nhap = models.DateTimeField(auto_now_add=True)
    tong_tien = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Phiếu nhập #{self.id} từ {self.nha_cung_cap.ten_nha_cung_cap}"

# Bảng Chi Tiết Phiếu Nhập
class ChiTietPhieuNhap(models.Model):
    phieu_nhap_kho = models.ForeignKey(PhieuNhapKho, related_name='chi_tiet_nhap', on_delete=models.CASCADE)
    nguyen_phu_lieu = models.ForeignKey(NguyenPhuLieu, on_delete=models.PROTECT)
    so_luong_nhap = models.PositiveIntegerField()
    gia_nhap = models.DecimalField(max_digits=10, decimal_places=2) # Giá tại thời điểm nhập

    def __str__(self):
        return f"{self.so_luong_nhap} x {self.nguyen_phu_lieu.ten_nguyen_phu_lieu}"