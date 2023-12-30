def phan_nguyen(a,b):
    if b == 0:
        return "Không thể chia cho 0"
    return a // b
so_chia = int(input("Nhập số chia:"))
so_bi_chia = int(input("Nhập số bị chia:"))
ket_qua = phan_nguyen(so_chia,so_bi_chia)
print(f"Phần nguyên của phép chia 2 số nguyên {so_chia,so_bi_chia} là:{ket_qua}")