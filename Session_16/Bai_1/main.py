# Lỗi không gán lại giá trị chuỗi (Tính bất biến): Chuỗi (String) trong Python có tính bất biến. 
# Khi gọi các phương thức như strip() và title(), hệ thống tạo ra một chuỗi mới chứ không thay đổi chuỗi gốc.
# Vì mã cũ không gán lại kết quả nên chuỗi lộn xộn ban đầu vẫn bị giữ nguyên. Giải pháp là gán chuỗi đã xử lý vào một biến mới (ví dụ: cleaned_diagnosis).

# Dùng sai phương thức thêm phần tử (extend vs append): Lệnh extend() dùng để gộp các tập hợp. Khi truyền một chuỗi vào extend(), Python coi chuỗi đó là một tập hợp các chữ cái và tách rời từng ký tự ra để nhét vào danh sách. 
# Để thêm nguyên vẹn cả một cụm từ vào danh sách như một phần tử duy nhất, giải pháp bắt buộc là phải dùng append(


patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    """
    Chuẩn hóa chuỗi tên chẩn đoán (xóa khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ)
    và thêm phần tử đã chuẩn hóa vào danh sách bệnh án hiện tại.
    """
    cleaned_diagnosis = raw_diagnosis.strip().title()
    current_list.append(cleaned_diagnosis)
    return current_list

new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)