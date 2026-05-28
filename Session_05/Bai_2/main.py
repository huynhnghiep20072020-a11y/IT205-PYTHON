# 1. Phân tích lỗi
# - Chương trình không gom được dữ liệu theo chi nhánh vì vòng lặp ngoài (outer loop) đang duyệt theo 'tháng' (month).
# - Vòng lặp ngoài chi phối toàn bộ tiến trình. Do duyệt theo tháng ở vòng ngoài, hệ thống sẽ chốt cố định Tháng 1, sau đó chạy vòng lặp trong (inner loop) để hỏi doanh thu của tất cả các chi nhánh trong tháng đó, rồi mới chuyển sang Tháng 2.
# - Theo yêu cầu nghiệp vụ (gom dữ liệu theo chi nhánh), vòng lặp ngoài phải duyệt theo: Chi nhánh (branch).
# - Vòng lặp trong phải duyệt theo: Tháng (month).

# 2. Sửa lỗi 
branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

result = ""

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        result = result + f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n"

print("\n-------------- Kết quả --------------")
print(result)