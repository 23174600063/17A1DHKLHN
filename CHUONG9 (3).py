def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range (2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
so_can_kiem_tra = 15
if kiem_tra_so_nguyen_to(so_can_kiem_tra):
    print(f"{so_can_kiem_tra} là số nguyên tố")
else:
    print(f"{so_can_kiem_tra} không phải là số nguyên tố")
