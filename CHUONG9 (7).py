def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


x = int(input("nhập x : "))
sign(x)
print(sign(x))


# Kiểm thử phương thức
# print(sign(-5))  # Kết quả: -1
# print(sign(10))  # Kết quả: 1
# print(sign(0))   # Kết quả: 0

