from models import BaseProduct, ColdStorageProduct, HazardousProduct, HybridPremiumProduct
from carriers import FedExCarrier, DHLCarrier, dispatch_to_carrier

def get_product_by_code(products, code):
    """Hàm phụ trợ tìm kiếm sản phẩm theo mã."""
    for p in products:
        if p.product_code == code:
            return p
    return None

def main():
    """Hệ thống điều hướng Menu CLI."""
    products = []
    current_product = None

    while True:
        print("\n===== AMAZON INVENTORY SIMULATOR PRO =====")
        print("1. Đăng ký mã hàng hóa mới (Chọn loại sản phẩm)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nhập / Xuất kho (Đa hình)")
        print("4. Kiểm tra điều kiện bảo quản / Tính chi phí phụ trội")
        print("5. Kiểm tra tính năng gộp lô hàng & So sánh tồn kho (Overloading)")
        print("6. Điều phối vận chuyển qua Đối tác thứ ba (Duck Typing)")
        print("7. Thoát chương trình")
        print("==========================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        match choice:
            case "1":
                print("--- CHỌN LOẠI SẢN PHẨM KHỞI TẠO ---")
                print("1. Cold Storage Product (Hàng Đông Lạnh)")
                print("2. Hazardous Product (Hàng Nguy Hiểm)")
                print("3. Hybrid Premium Product (Hàng Lai Cao Cấp)")
                prod_type = input("Chọn loại sản phẩm (1-3): ").strip()
                
                code = input("Nhập mã sản phẩm 10 ký tự: ").strip().upper()
                if not BaseProduct.validate_product_code(code):
                    print("Mã sản phẩm không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng chữ cái.")
                    continue
                    
                name = input("Nhập tên sản phẩm: ").strip()
                
                try:
                    if prod_type == "1":
                        temp = int(input("Nhập nhiệt độ bảo quản yêu cầu (độ C): "))
                        new_prod = ColdStorageProduct(code, name, temp)
                        type_name = "Đông Lạnh"
                    elif prod_type == "2":
                        limit = int(input("Nhập hạn mức an toàn tối đa: "))
                        new_prod = HazardousProduct(code, name, limit)
                        type_name = "Nguy Hiểm"
                    elif prod_type == "3":
                        temp = int(input("Nhập nhiệt độ bảo quản yêu cầu (độ C): "))
                        limit = int(input("Nhập hạn mức an toàn tối đa: "))
                        new_prod = HybridPremiumProduct(code, name, temp, limit)
                        type_name = "Lai Cao Cấp"
                    else:
                        print("Lựa chọn loại sản phẩm không hợp lệ.")
                        continue

                    products.append(new_prod)
                    current_product = new_prod
                    print(f"\nĐăng ký sản phẩm {type_name} thành công!")
                    print(f"Tên sản phẩm: {new_prod.name}")
                except ValueError:
                    print("Lỗi: Dữ liệu nhập vào phải là số nguyên.")

            case "2":
                if current_product is None:
                    print("Hệ thống chưa có thông tin sản phẩm. Vui lòng tạo sản phẩm trước.")
                    continue
                    
                print("--- THÔNG TIN SẢN PHẨM HIỆN TẠI ---")
                print(f"Loại sản phẩm: {current_product.__class__.__name__}")
                print(f"Chuỗi kho: {BaseProduct.warehouse_name}")
                print(f"Mã sản phẩm: {current_product.product_code}")
                print(f"Tên sản phẩm: {current_product.name}")
                print(f"Số lượng tồn kho: {current_product.stock_quantity} đơn vị")
                
                if isinstance(current_product, ColdStorageProduct):
                    print(f"Nhiệt độ yêu cầu: {current_product.required_temperature} độ C")
                if isinstance(current_product, HazardousProduct):
                    print(f"Hạn mức an toàn tối đa: {current_product.max_safety_limit} đơn vị")
                    
                print("\n[Danh sách MRO của lớp hiện tại]:")
                for cls in current_product.__class__.__mro__:
                    print(f"- {cls.__name__}")

            case "3":
                if current_product is None:
                    print("Hệ thống chưa có thông tin sản phẩm.")
                    continue
                    
                print("--- GIAO DỊCH NHẬP / XUẤT KHO ---")
                print("1. Nhập kho")
                print("2. Xuất kho")
                action = input("Chọn giao dịch (1-2): ").strip()
                
                try:
                    if action == "1":
                        qty = int(input("Nhập số lượng nhập kho: "))
                        current_product.import_stock(qty)
                    elif action == "2":
                        qty = int(input("Nhập số lượng cần xuất: "))
                        current_product.export_stock(qty)
                    else:
                        print("Lựa chọn giao dịch không hợp lệ.")
                except ValueError:
                    print("Lỗi: Số lượng nhập vào không hợp lệ.")

            case "4":
                if current_product is None:
                    print("Hệ thống chưa có thông tin sản phẩm.")
                    continue
                    
                if isinstance(current_product, ColdStorageProduct):
                    current_product.apply_cooling_cost()
                else:
                    print("Tính năng tính chi phí làm lạnh không hỗ trợ cho loại sản phẩm này.")

            case "5":
                if current_product is None:
                    print("Hệ thống chưa có thông tin sản phẩm.")
                    continue
                    
                print("--- ĐỒNG BỘ & SO SÁNH TỒN KHO (OPERATOR OVERLOADING) ---")
                print(f"Sản phẩm hiện tại (A): {current_product.name} (Tồn kho: {current_product.stock_quantity} đơn vị)")
                target_code = input("Chọn mã sản phẩm đối ứng (B) từ danh sách: ").strip().upper()
                target_product = get_product_by_code(products, target_code)
                
                if target_product:
                    print(f"Sản phẩm đối ứng (B): {target_product.name} (Tồn kho: {target_product.stock_quantity} đơn vị)")
                    try:
                        if current_product < target_product:
                            comp_res = "ÍT HƠN"
                        elif target_product < current_product:
                            comp_res = "NHIỀU HƠN"
                        else:
                            comp_res = "BẰNG NHAU"
                        
                        print(f"[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A {comp_res} tồn kho sản phẩm B.")
                        
                        total_sum = current_product + target_product
                        print(f"[Kết quả Tổng hợp (__add__)]: Tổng số lượng tồn kho của cả 2 mã sản phẩm là: {total_sum} đơn vị.")
                    except TypeError:
                        print("Lỗi: Dữ liệu đem ra so sánh không tương thích.")
                else:
                    print("Không tìm thấy mã sản phẩm đối ứng trong hệ thống.")

            case "6":
                if current_product is None:
                    print("Hệ thống chưa có thông tin sản phẩm.")
                    continue
                    
                print("--- ĐIỀU PHỐI ĐƠN VỊ VẬN CHUYỂN NGOÀI ---")
                print("1. Vận chuyển qua đối tác FedEx")
                print("2. Vận chuyển qua đối tác DHL")
                print("3. Vận chuyển qua Đối tác Lỗi (Test Duck Typing)")
                carrier_choice = input("Chọn đối tác vận chuyển (1-3): ").strip()
                
                try:
                    qty = int(input("Nhập số lượng hàng hóa bàn giao: "))
                    
                    if carrier_choice == "1":
                        agent = FedExCarrier()
                    elif carrier_choice == "2":
                        agent = DHLCarrier()
                    elif carrier_choice == "3":
                        class FakeCarrier:
                            pass
                        agent = FakeCarrier()
                    else:
                        print("Lựa chọn đơn vị không hợp lệ.")
                        continue
                        
                    dispatch_to_carrier(agent, current_product, qty)
                    print(f"Số lượng tồn kho cập nhật: {current_product.stock_quantity} đơn vị.")
                except ValueError:
                    print("Lỗi: Số lượng nhập vào không hợp lệ.")

            case "7":
                print("Cảm ơn đã sử dụng hệ thống Amazon Inventory Simulator Pro!")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 7.")


if __name__ == "__main__":
    main()