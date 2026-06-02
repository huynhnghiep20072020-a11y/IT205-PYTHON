branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    if choice not in ["1", "2", "3", "4"]:
        print("\n[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")
        continue
        
    if choice == "1":
        print("\n--- BÁO CÁO DOANH THU TỔNG HỢP ---")
        print(f"{'Tên Cơ Sở':<25} | {'Doanh Thu':<12} | {'Trạng Thái'}")
        print("-" * 55)
        for i in range(len(branch_names)):
            trang_thai = "Đạt" if target_achieved[i] == True else "Không Đạt"
            print(f"{branch_names[i]:<25} | {daily_revenues[i]:<12} | {trang_thai}")
            
        print("-" * 55)
        print(f"=> TỔNG DOANH THU TOÀN VÙNG: {sum(daily_revenues)} VNĐ")
        
    elif choice == "2":
        doanh_thu_cao_nhat = max(daily_revenues)
        doanh_thu_thap_nhat = min(daily_revenues)
        
        index_cao = daily_revenues.index(doanh_thu_cao_nhat)
        index_thap = daily_revenues.index(doanh_thu_thap_nhat)
        
        print("\n--- THỐNG KÊ CƠ SỞ NỔI BẬT ---")
        print(f"- Cơ sở có doanh thu CAO NHẤT: {branch_names[index_cao]} ({doanh_thu_cao_nhat} VNĐ)")
        print(f"- Cơ sở có doanh thu THẤP NHẤT: {branch_names[index_thap]} ({doanh_thu_thap_nhat} VNĐ)")
        
    elif choice == "3":
        failed_branches = []
        
        for i in range(len(target_achieved)):
            if target_achieved[i] == False:
                failed_branches.append(branch_names[i])
                
        print("\n--- DANH SÁCH CƠ SỞ CẦN HỖ TRỢ TRA CỨU ĐƯỢC ---")
        print(failed_branches)
        
    elif choice == "4":
        print("\nHệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        break