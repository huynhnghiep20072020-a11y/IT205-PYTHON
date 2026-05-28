# Qua kiểm tra mã nguồn, lỗi nghiêm trọng khiến kiosk duyệt sai quy định y tế xuất phát từ việc sử dụng sai toán tử logic.
# Cụ thể, hệ thống đang dùng toán tử or thay vì toán tử and tại dòng lệnh kiểm tra điều kiện: if donor_age >= 18 or donor_weight >= 50. code sửa đúng
print("--- BLOOD DONOR SCREENING SYSTEM ---")

# Nhập dữ liệu đầu vào từ tình nguyện viên
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

print("\n--- SCREENING RESULT ---")
# Hệ thống kiểm tra điều kiện hiến máu (Bắt buộc thỏa mãn ĐỒNG THỜI cả hai điều kiện)
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    print("Reason(s) for rejection:")
    
    # Phân tích và chỉ rõ lý do không đủ điều kiện cho người khai báo
    if donor_age < 18:
        print("- Age must be 18 or older (Current: {} years old).".format(donor_age))
    if donor_weight < 50:
        print("- Weight must be 50 kg or heavier (Current: {} kg).".format(donor_weight))