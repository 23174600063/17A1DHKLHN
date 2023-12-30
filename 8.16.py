a=int(input("nhập số a:"))
b=int(input("nhập số b:"))
r = a % b
while r != 0:
        a = b
        b = r
        r = a % b
print(b)