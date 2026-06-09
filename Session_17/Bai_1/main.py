raw_logs = []
processed_logs = []

def input_and_clean_logs():
    """Nhập log thô, sử dụng maketrans để dọn dẹp ký tự rác và chia tách thành danh sách."""
    global raw_logs
    print("--- NẠP DỮ LIỆU LOG ---")
    raw_data = input("Nhập chuỗi log thô: ")
    
    table = str.maketrans("", "", "!@#$")
    clean_data = raw_data.translate(table)
    
    temp_logs = clean_data.split(";")
    raw_logs = []
    
    for log in temp_logs:
        if len(log.strip()) > 0:
            raw_logs.append(log.strip())
            
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

def filter_critical_logs():
    """Lọc các log chứa từ khóa nguy hiểm bằng List Comprehension và lưu vào biến toàn cục."""
    global processed_logs
    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return

    print("--- LỌC CẢNH BÁO ---")
    processed_logs = [log for log in raw_logs if "ERROR" in log.upper() or "CRITICAL" in log.upper()]
    
    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
    for log in processed_logs:
        print(f"- {log}")

def mask_ips():
    """Che giấu 2 dải số cuối của địa chỉ IP trong danh sách log để bảo mật thông tin."""
    global processed_logs
    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return []

    print("--- MÃ HÓA IP ---")
    for i in range(len(processed_logs)):
        words = processed_logs[i].split()
        for word in words:
            if "." in word:
                parts = word.split(".")
                if len(parts) == 4:
                    masked_ip = f"{parts[0]}.{parts[1]}.*.*"
                    processed_logs[i] = processed_logs[i].replace(word, masked_ip)

    print("Báo cáo log an toàn:")
    for i in range(len(processed_logs)):
        print(f"{i + 1}. {processed_logs[i]}")
        
    return processed_logs

def main():
    """Menu điều hướng chính của chương trình phân tích log bảo mật."""
    while True:
        print("\n--------------- SECURITY LOG ANALYZER -----------------")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("---------------------------------------------------------")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            input_and_clean_logs()
        elif choice == "2":
            filter_critical_logs()
        elif choice == "3":
            mask_ips()
        elif choice == "4":
            print("Hệ thống kết thúc và thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()