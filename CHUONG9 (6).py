#Diện tích và chu vi hình tròn
dien_tich_hinh_tron = lambda r:3.14 * r ** 2
chu_vi_hinh_tron = lambda r:2 * 3.14 *r

#Diệ tích và chu vi hình chữ nhật
dien_tich_hcn = lambda a,b: a*b
chu_vi_hcn = lambda a,b: 2*(a+b)

r = int(input("nhập r:"))
a = int(input("nhập chiều dài:"))
b = int(input("nhập chiều rộng:"))
print(f"Diện tích hình tròn :",dien_tich_hinh_tron(r))
print(f"Chu vi hình tròn :",chu_vi_hinh_tron(r))
print(f"Diện tích hình chữ nhật:", dien_tich_hcn(a,b))
print(f"Chu vi hình chữ nhật:",chu_vi_hcn(a,b))
