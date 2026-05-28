# 1. Phân tích Input / Output
# Input: 3 biến dạng số nguyên (int) nhập từ bàn phím: age (Tuổi), sbp (Huyết áp tâm thu), sugar (Đường huyết).
# Output: Thông báo lỗi nếu dữ liệu âm; ngược lại in kết quả sàng lọc y khoa ("ĐỦ ĐIỀU KIỆN" hoặc "TỪ CHỐI" kèm lý do cụ thể).
# 2. Phân tích và so sánh hai giải pháp:
# - Giải pháp 1: Gộp điều kiện (Flat Logic)
#   + Độ ngắn gọn của code: Rất ngắn gọn, chỉ dùng một dòng kiểm tra duy nhất dạng if ... and ... and ...
#   + Độ phức tạp khi đọc code (thụt lề): Thấp, mã nguồn phẳng, cấu trúc đơn giản, dễ nhìn tổng thể.
#   + Trải nghiệm người dùng và Giá trị y khoa: Kém. Hệ thống chỉ có thể thông báo "Từ chối phẫu thuật" chung chung, điều dưỡng và bác sĩ không thể biết bệnh nhân bị trượt ở chỉ số cụ thể nào để kịp thời xử lý.
# - Giải pháp 2: Điều kiện lồng nhau (Nested If)
#   + Độ ngắn gọn của code: Dài dòng hơn do phải bóc tách và viết nhiều cấp rẽ nhánh if-else độc lập.
#   + Độ phức tạp khi đọc code (thụt lề): Cao, mã nguồn bị thụt lề nhiều bậc, cấu trúc phức tạp hơn (Arrow Anti-pattern).
#   + Trải nghiệm người dùng và Giá trị y khoa: Xuất sắc. Hệ thống bắt lỗi chính xác từng chỉ số sinh hiệu và thông báo rõ ràng lý do từ chối cụ thể (ví dụ: do đường huyết cao vượt ngưỡng), giúp y bác sĩ nắm bắt ngay tình trạng của bệnh nhân.
# * Chốt lựa chọn: Chọn Giải pháp 2 (Điều kiện lồng nhau - Nested If).
# * Lý do và Trade-off: Chấp nhận đánh đổi việc mã nguồn dài hơn và thụt lề nhiều tầng hơn để đạt được giá trị y khoa tối cao. Trong môi trường y tế bệnh viện, việc biết rõ chính xác nguyên nhân khiến bệnh nhân không đủ điều kiện mổ quan trọng hơn việc giữ cho mã nguồn ngắn gọn, giúp đảm bảo an toàn tính mạng và hỗ trợ bác sĩ đưa ra phác đồ điều hòa chỉ số kịp thời.


# viết code
import sys

# 1. Nhập dữ liệu đầu vào
raw_age = input("Nhập tuổi bệnh nhân: ")
raw_sbp = input("Nhập huyết áp tâm thu (mmHg): ")
raw_sugar = input("Nhập đường huyết (mg/dL): ")

# Kiểm tra định dạng số nguyên
if not (raw_age.isdigit() or (raw_age.startswith('-') and raw_age[1:].isdigit())) or \
   not (raw_sbp.isdigit() or (raw_sbp.startswith('-') and raw_sbp[1:].isdigit())) or \
   not (raw_sugar.isdigit() or (raw_sugar.startswith('-') and raw_sugar[1:].isdigit())):
    print("Dữ liệu nhập vào không hợp lệ")
    sys.exit()

age = int(raw_age)
sbp = int(raw_sbp)
sugar = int(raw_sugar)

# 2. Xử lý bẫy dữ liệu âm (Edge Case)
if age < 0 or sbp < 0 or sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
    sys.exit()

# 3. Xét duyệt y khoa theo giải pháp Điều kiện lồng nhau (Nested If)
print("\n--- KẾT QUẢ SÀNG LỌC TIỀN PHẪU THUẬT ---")

if age < 75:
    if 90 <= sbp <= 140:
        if sugar < 150:
            print("KẾT LUẬN: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        else:
            print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
            print("Lý do: Đường huyết cao vượt ngưỡng an toàn (Hiện tại: {} mg/dL, yêu cầu: < 150).".format(sugar))
    else:
        print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
        print("Lý do: Huyết áp tâm thu nằm ngoài khoảng an toàn (Hiện tại: {} mmHg, yêu cầu: 90 - 140).".format(sbp))
else:
    print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
    print("Lý do: Bệnh nhân vượt quá độ tuổi phẫu thuật an toàn (Hiện tại: {} tuổi, yêu cầu: < 75).".format(age))