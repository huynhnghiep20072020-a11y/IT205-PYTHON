atm_vault_balance = 50000000
user_account_balance = 10000000

def main():
    while True:
        print("\n================ SMART ATM ================")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("===========================================")
        
        choice = input("Vui lòng chọn giao dịch (1-4): ").strip()
        
        if choice == "1":
            display_balances()
            
        elif choice == "2":
            print("--- NẠP TIỀN ---")
            try:
                amount = int(input("Nhập số tiền muốn nạp: "))
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                else:
                    if deposit_money(amount):
                        print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VNĐ.")
            except ValueError:
                print("Số tiền không hợp lệ.")
                
        elif choice == "3":
            print("--- RÚT TIỀN ---")
            try:
                amount = int(input("Nhập số tiền cần rút: "))
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                elif amount % 50000 != 0:
                    print("Số tiền rút phải là bội số của 50,000.")
                else:
                    status = check_withdrawal_rules(amount)
                    if status == "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Số dư tài khoản không đủ để thanh toán tiền rút và phí.")
                    elif status == "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                    elif status == "OK":
                        fee = 1100
                        total_deduction = amount + fee
                        execute_withdrawal(total_deduction, amount)
            except ValueError:
                print("Số tiền không hợp lệ.")
                
        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()
    
def display_balances():
    """
    In ra màn hình số dư tài khoản hiện tại của người dùng và lượng tiền mặt còn lại trong ATM.
    """
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VNĐ")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VNĐ")

def deposit_money(amount):
    """
    Cộng tiền vào số dư tài khoản người dùng và tăng lượng tiền mặt vật lý trong máy ATM.
    """
    global user_account_balance, atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount
    return True

def check_withdrawal_rules(amount):
    """
    Kiểm tra các quy tắc rút tiền: kiểm tra số dư người dùng (bao gồm phí) và tiền mặt trong máy.
    """
    fee = 1100
    total_deduction = amount + fee
    
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    elif amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    else:
        return "OK"

def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện trừ tiền trong hệ thống toàn cục và in biên lai giao dịch ra màn hình.
    """
    global user_account_balance, atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VNĐ")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VNĐ.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VNĐ.")

