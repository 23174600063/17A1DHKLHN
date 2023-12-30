def kiem_tra_so_hoan_hao(n):
    if n <= 0:
        return False
    tong_uoc = 0
    for i in range(1,n):
        tong_uoc += 1
    return tong_uoc == n
so_can_kiem_tra = int(input("Nhập số cần tìm:"))
if kiem_tra_so_hoan_hao(so_can_kiem_tra):
    print(f"{so_can_kiem_tra} là số hoàn hảo")
else:
    print(f"{so_can_kiem_tra} không phải là số hoàn hảo")

