"""

1 THIẾT KẾ KIẾN TRÚC & LUỒNG DỮ LIỆU


1. Bảng Thiết kế Dữ liệu (5 trường thông tin):
 Tên biến (snake_case)  Nội dung input        Kiểu dữ liệu mong muốn 
---------------------------------------------------------------------
 patient_name           Họ và tên bệnh nhân  pstr                    
 patient_id             Mã CCCD / Số BHYT      str                   
 body_weight            Cân nặng (kg)         float                  
 body_temperature       Nhiệt độ cơ thể (°C)  float                  
 heart_rate             Nhịp tim (lần/phút)   int                    

2. Thiết kế luồng chương trình (Flow):
- Bước 1 (Khởi tạo): Hiển thị màn hình chào mừng thân thiện, rõ ràng 
  mục đích của Kiosk để bệnh nhân yên tâm thao tác.
- Bước 2 (Thu thập dữ liệu): Hiển thị tuần tự các câu hỏi (prompt) 
  được thiết kế tối ưu UX. Lưu toàn bộ dữ liệu người dùng nhập vào 
  dưới dạng chuỗi tạm thời (raw data) để tránh crash.
- Bước 3 (Xử lý ép kiểu): Chuyển đổi ngầm các chuỗi dữ liệu thô về đúng 
  định dạng toán học (float cho cân nặng, nhiệt độ; int cho nhịp tim).
- Bước 4 (Hiển thị):
  + In ra "Phiếu Khám Bệnh Điện Tử" cho bệnh nhân dễ đọc.
  + In ra "Log Hệ Thống" ẩn bên dưới để IT kiểm tra kiểu dữ liệu.

3. Thiết kế UX Prompt (Ngăn chặn lỗi crash):
- Các câu hỏi phải gọi bằng danh xưng lịch sự ("cô/chú").
- Bắt buộc phải có ví dụ (VD: 37.5) ngay trong câu hỏi để ép người 
  dùng nhập đúng định dạng số thập phân, tránh nhập chữ hoặc dấu phẩy.
"""

# 2TRIỂN KHAI CODE 
print("=" * 65)
print("     CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI BỆNH VIỆN SỨC KHỎE VÀNG")
print("   KIOSK KHAI BÁO TỰ PHỤC VỤ - Rút ngắn thời gian chờ đợi")
print("=" * 65)
print("Xin vui lòng làm theo hướng dẫn trên màn hình.\n")


print("--- THÔNG TIN CÁ NHÂN ---")
patient_name = input("1. Mời cô/chú nhập Họ và tên (VD: Nguyen Van A): ")
patient_id = input("2. Mời cô/chú nhập số CCCD hoặc BHYT (VD: 079123456789): ")

print("\n--- CHỈ SỐ SINH HIỆU CƠ BẢN ---")
raw_body_weight = input("3. Mời cô/chú nhập Cân nặng theo kg (VD: 65.5): ")
raw_body_temperature = input("4. Mời cô/chú nhập Nhiệt độ cơ thể theo độ C (VD: 37.5): ")
raw_heart_rate = input("5. Mời cô/chú nhập Nhịp tim hiện tại (VD: 85): ")



body_weight = float(raw_body_weight)
body_temperature = float(raw_body_temperature)
heart_rate = int(raw_heart_rate)



# In Phiếu Khám Bệnh Điện Tử 
print("\n" + "=" * 65)
print("                    PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("=" * 65)
print(f"Họ và tên bệnh nhân : {patient_name.upper()}")
print(f"Mã định danh (CCCD) : {patient_id}")
print("-" * 65)
print("CHỈ SỐ SINH HIỆU LÂM SÀNG:")
# 1f giúp hiển thị đẹp mắt với 1 chữ số thập phân
print(f"- Cân nặng          : {body_weight:.1f} kg")
print(f"- Nhiệt độ cơ thể   : {body_temperature:.1f} °C")
print(f"- Nhịp tim          : {heart_rate} nhịp/phút")
print("=" * 65)
print("Cảm ơn Quý khách! Vui lòng cầm phiếu này đến phòng khám.\n")

#  In Log Hệ Thống 
print(">>> [SYSTEM LOG] DỮ LIỆU ĐÃ ĐƯỢC CHUẨN HÓA THÀNH CÔNG:")
print(f"[DEBUG] patient_name     : {type(patient_name)}")
print(f"[DEBUG] patient_id       : {type(patient_id)}")
print(f"[DEBUG] body_weight      : {type(body_weight)}")
print(f"[DEBUG] body_temperature : {type(body_temperature)}")
print(f"[DEBUG] heart_rate       : {type(heart_rate)}")
print(">>> [SYSTEM LOG] SẴN SÀNG ĐỒNG BỘ LÊN DATABASE TỔNG.")