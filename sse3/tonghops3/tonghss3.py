
while True:
    
    so_luong_nv = int(input("\nNhập số lượng nhân viên: "))

    
    for i in range(1, so_luong_nv + 1):
        print(f"\nNhân viên {i}")
        
       
        ten_nv = input("Tên nhân viên: ")
        so_ngay = int(input("Số ngày đi làm: "))

       
        print("Thông tin nhân viên:")
        print(f"Tên: {ten_nv}")
        print(f"Số ngày đi làm: {so_ngay}")

        
        if so_ngay < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")

    
    print() 
    lua_chon = input("Tiếp tục chương trình? (y/n): ")
    
    
    if lua_chon.lower() == 'n':
        print("Chương trình kết thúc")
        break  