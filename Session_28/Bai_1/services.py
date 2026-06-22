class VietcombankCorporateService:
    """Cổng dịch vụ ngân hàng doanh nghiệp Vietcombank."""

    def transfer_salary(self, employee, amount):
        """Thực hiện giải ngân lương qua hệ thống VCB."""
        print("[Hệ thống VCB Corporate]: Đang kết nối tới cổng chi trả Rikkei...")
        print(f"Ngân hàng đối tác đã giải ngân thành công số tiền: {amount:,.0f} VND tới nhân sự {employee.emp_code}.")


class TechcombankCorporateService:
    """Cổng dịch vụ ngân hàng doanh nghiệp Techcombank."""

    def transfer_salary(self, employee, amount):
        """Thực hiện giải ngân lương qua hệ thống TCB."""
        print("[Hệ thống TCB Corporate]: Đang xử lý lệnh chuyển tiền lương...")
        print(f"Ngân hàng đối tác đã giải ngân thành công số tiền: {amount:,.0f} VND tới nhân sự {employee.emp_code}.")


def execute_payroll(payment_service, employee, amount):
    """Hàm toàn cục điều phối chi trả lương sử dụng Duck Typing."""
    try:
        payment_service.transfer_salary(employee, amount)
        print("Xác thực đối tác bằng Duck Typing thành công!")
    except AttributeError:
        print("Lỗi: Cổng dịch vụ ngân hàng doanh nghiệp không hợp lệ hoặc chưa được liên kết liên thông kỹ thuật.")