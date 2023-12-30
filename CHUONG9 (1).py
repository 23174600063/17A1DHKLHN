def tinh_S(n,x):
    S = (x ** 2 + 1) ** n
    print("S =",S)
    return S


n = float(input("Nhập n: "))
x = float(input("Nhập x: "))
S = tinh_S(n, x)
    