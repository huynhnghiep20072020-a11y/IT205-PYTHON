# Lỗi tham chiếu bộ nhớ  Phép gán new_prescription = old_prescription chỉ tạo ra một tên gọi khác trỏ về cùng một danh sách gốc. 
# việc thêm thuốc mới bằng append() sẽ làm thay đổi luôn cả lịch sử bệnh án hôm qua. Cách sửa chuẩn xác là dùng phương thức .copy() để tạo ra một bản sao danh sách hoàn toàn độc lập.

# Lỗi không gán lại chuỗi Hàm replace() của chuỗi luôn sinh ra một chuỗi mới chứ không sửa trực tiếp trên chuỗi cũ.
# bạn bắt buộc phải gán kết quả vừa thay thế đè lại vào đúng vị trí new_prescription[0] thì danh sách mới thực sự được cập nhật dữ liệu.


yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    """
    Tạo bản sao của đơn thuốc cũ, cập nhật lại tên thuốc và thêm thuốc mới cho ngày hôm nay 
    mà không làm thay đổi lịch sử bệnh án của ngày hôm qua.
    """
    new_prescription = old_prescription.copy()
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    new_prescription.append("Oresol")
    return new_prescription

today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)