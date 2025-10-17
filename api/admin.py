from django.contrib import admin
from .models import NhaCungCap, NguyenPhuLieu, SanPham, KhachHang, DonHang, ChiTietDonHang,PhieuNhapKho, ChiTietPhieuNhap

admin.site.register(NhaCungCap)
admin.site.register(NguyenPhuLieu)
admin.site.register(SanPham)
admin.site.register(KhachHang)
admin.site.register(DonHang)
admin.site.register(ChiTietDonHang)
admin.site.register(PhieuNhapKho)
admin.site.register(ChiTietPhieuNhap)