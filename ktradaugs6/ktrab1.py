print("--- KIỂM TRA TÌNH TRẠNG HÀNG HÓA ---")
stock_quantity = int(input("Nhập số lượng tồn kho của mặt hàng: "))
if stock_quantity >= 50:
    print("Tình trạng: Hàng đầy kho")
elif 10 <= stock_quantity < 50:
    print("Tình trạng: Mức an toàn")
else:
    print("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm")