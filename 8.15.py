a = 0
while True:
    try:
        i = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
        if i == 0:
            break
        a += i
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

print("S=:", a)
