class FedExCarrier:
    """Đối tác vận chuyển FedEx."""

    def ship_package(self, product, quantity):
        """Tiếp nhận và xử lý vận chuyển qua FedEx."""
        print(f"[Hệ thống FedEx]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        product.export_stock(quantity)


class DHLCarrier:
    """Đối tác vận chuyển DHL."""

    def ship_package(self, product, quantity):
        """Tiếp nhận và xử lý vận chuyển qua DHL."""
        print(f"[Hệ thống DHL]: Đang lên mã vận đơn cho {product.product_code}...")
        product.export_stock(quantity)


def dispatch_to_carrier(carrier_agent, product, quantity):
    """Hàm điều phối vận chuyển sử dụng Duck Typing để linh hoạt đối tác."""
    try:
        carrier_agent.ship_package(product, quantity)
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Đơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {quantity} đơn vị.")
    except AttributeError:
        print("Lỗi: Đơn vị vận chuyển không hợp lệ hoặc chưa ký kết hợp đồng kỹ thuật.")