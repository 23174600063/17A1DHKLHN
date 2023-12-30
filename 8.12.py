a=int(input("nhập số:"))
t=0
for i in range(2,a):
    if a%i==0:
        t=1
        print("đây là số nguyên tố")
        break
if a==2:
  print("đây là số nguyên tố")
else:
  print("đây không là số nguyên tố")
  