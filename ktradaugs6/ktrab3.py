print("\n--- XÁC THỰC LỆNH XUẤT KHO ---")
current_stock = 100
print(f"Tồn kho hiện tại của 'Bàn phím cơ': {current_stock} sản phẩm")
while True:
    export_quantity = int(input("Nhập số lượng muốn xuất kho: "))
    if export_quantity < 0:
        print("Không được nhập số âm, vui lòng nhập lại!")
    elif export_quantity > current_stock:
        print("Kho không đủ hàng, vui lòng nhập lại!")
    else:
        current_stock -= export_quantity
        print("=> Xuất kho thành công!")
        print(f"Tồn kho còn lại: {current_stock}")
        break
print("\n--- KẾT THÚC BÀI KIỂM TRA ---")