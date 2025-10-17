from rest_framework import serializers
from .models import SanPham, NhaCungCap, KhachHang

# Serializer cho model SanPham
class SanPhamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanPham
        fields = ['id', 'ten_san_pham', 'mo_ta', 'don_gia_ban', 'hinh_anh_url']

# Serializer cho model NhaCungCap
class NhaCungCapSerializer(serializers.ModelSerializer):
    class Meta:
        model = NhaCungCap
        fields = ['id', 'ten_nha_cung_cap', 'thong_tin_lien_he', 'dia_chi']

# Serializer cho model KhachHang
class KhachHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhachHang
        fields = ['id', 'ho_ten', 'so_dien_thoai', 'dia_chi']
        # ... (giữ nguyên các serializer đã có)
from .models import DonHang, ChiTietDonHang

class ChiTietDonHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietDonHang
        fields = ['san_pham', 'so_luong']

class DonHangSerializer(serializers.ModelSerializer):
    # Dùng ChiTietDonHangSerializer cho trường 'chi_tiet', cho phép nhận nhiều chi tiết
    chi_tiet = ChiTietDonHangSerializer(many=True)

    class Meta:
        model = DonHang
        # Thêm 'chi_tiet' vào fields, 'tong_gia_tri' và 'trang_thai' sẽ được đọc sau khi tạo
        fields = ['id', 'khach_hang', 'nhan_vien', 'ngay_dat_hang', 'tong_gia_tri', 'trang_thai', 'chi_tiet']
        read_only_fields = ['tong_gia_tri', 'trang_thai', 'ngay_dat_hang']

    def create(self, validated_data):
        # Tách dữ liệu của chi tiết đơn hàng ra khỏi dữ liệu chính
        chi_tiet_data = validated_data.pop('chi_tiet')

        # Tạo đối tượng DonHang trước
        don_hang = DonHang.objects.create(**validated_data)

        tong_gia_tri = 0
        # Lặp qua từng chi tiết đơn hàng để tạo các đối tượng ChiTietDonHang
        for item_data in chi_tiet_data:
            san_pham = item_data['san_pham']
            so_luong = item_data['so_luong']
            don_gia = san_pham.don_gia_ban  # Lấy giá bán từ model SanPham
            
            ChiTietDonHang.objects.create(don_hang=don_hang, san_pham=san_pham, so_luong=so_luong, don_gia=don_gia)
            
            # Cộng dồn vào tổng giá trị
            tong_gia_tri += don_gia * so_luong

        # Cập nhật lại tổng giá trị cho đơn hàng và lưu lại
        don_hang.tong_gia_tri = tong_gia_tri
        don_hang.save()

        return don_hang
    # ... (giữ nguyên các serializer đã có)
from django.db import transaction
from .models import PhieuNhapKho, ChiTietPhieuNhap, NguyenPhuLieu

class ChiTietPhieuNhapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietPhieuNhap
        fields = ['nguyen_phu_lieu', 'so_luong_nhap', 'gia_nhap']

class PhieuNhapKhoSerializer(serializers.ModelSerializer):
    chi_tiet_nhap = ChiTietPhieuNhapSerializer(many=True)

    class Meta:
        model = PhieuNhapKho
        fields = ['id', 'nha_cung_cap', 'nhan_vien', 'ngay_nhap', 'tong_tien', 'chi_tiet_nhap']
        read_only_fields = ['tong_tien', 'ngay_nhap']

    def create(self, validated_data):
        chi_tiet_data = validated_data.pop('chi_tiet_nhap')
        
        # transaction.atomic đảm bảo tất cả các thao tác DB dưới đây hoặc thành công hết, hoặc thất bại hết
        # Tránh trường hợp tạo phiếu nhập thành công nhưng cập nhật kho thất bại
        with transaction.atomic():
            phieu_nhap_kho = PhieuNhapKho.objects.create(**validated_data)
            tong_tien = 0

            for item_data in chi_tiet_data:
                # Tạo chi tiết phiếu nhập
                ChiTietPhieuNhap.objects.create(phieu_nhap_kho=phieu_nhap_kho, **item_data)
                
                # CẬP NHẬT TỒN KHO
                nguyen_phu_lieu = item_data['nguyen_phu_lieu']
                so_luong_nhap = item_data['so_luong_nhap']
                nguyen_phu_lieu.so_luong_ton_kho += so_luong_nhap
                nguyen_phu_lieu.save()
                
                # Tính tổng tiền
                tong_tien += item_data['gia_nhap'] * so_luong_nhap

            # Cập nhật tổng tiền cho phiếu nhập
            phieu_nhap_kho.tong_tien = tong_tien
            phieu_nhap_kho.save()

        return phieu_nhap_kho