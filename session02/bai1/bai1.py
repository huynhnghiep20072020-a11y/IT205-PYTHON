# Chương trình bị lỗi logic do cấu trúc if-elif-else trong Python hoạt động theo nguyên tắc kiểm tra từ trên xuống dưới. 
# Với test case heart_rate = 135, chương trình kiểm tra điều kiện đầu tiên là heart_rate > 100 
# và kết quả đúng nên hệ thống lập tức phân loại bệnh nhân vào mức YELLOW rồi bỏ qua toàn bộ các nhánh elif phía dưới. 
# Vì vậy điều kiện heart_rate > 120 không bao giờ được kiểm tra dù bệnh nhân thuộc mức nguy kịch RED. 
# Nguyên nhân là do điều kiện lớn hơn 100 được đặt trước điều kiện lớn hơn 120. Để sửa lỗi cần đổi thứ tự điều kiện,
# ưu tiên kiểm tra mức nguy hiểm cao nhất trước. Code đúng như sau:

print("--- EMERGENCY TRIAGE SYSTEM ---")

heart_rate = int(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")
