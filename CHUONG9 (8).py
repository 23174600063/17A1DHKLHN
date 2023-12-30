a = int(input("nhập năm = "))
can = a % 10
chi = a % 12

# tính số can
can_names = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất","Bính","Đinh","Mẫu","Kỳ"]

if 0 <= can <= 10:
    x = can_names[can]
else:
    x = "Giá trị can không hợp lệ"

# tính số chi
chi_names = ["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]

if 0<= chi <= 12:
    y = chi_names[chi]
else:
    y = "Giá trị can không hợp lệ"


print("như vậy năm",a,"là năm","\"",x,y,"\"","âm lịch")