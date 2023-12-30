phong1 = float(1260000) 
phong2 = float(1550000)
phong3 = float(1830000) 
phong4 = float(1830000)
phong5 = float(2120000) 
phong6 = float(2120000)
phong7 = float(2540000) 
phong8 = float(4800000)
so_phong=float(input("nhập loại phòng:"))
so_dem=float(input("nhập số đêm:"))   
if(so_phong == 1) :
        tien_phong_1_dem = phong1
elif(so_phong == 2):
        tien_phong_1_dem = phong2
elif(so_phong == 3):
        tien_phong_1_dem = phong3
elif(so_phong == 4):
        tien_phong_1_dem = phong4
elif(so_phong == 5):
        tien_phong_1_dem = phong5
elif(so_phong == 6):
        tien_phong_1_dem = phong6
elif(so_phong == 7):
        tien_phong_1_dem = phong7
elif(so_phong == 8):
        tien_phong_1_dem = phong8    

if (so_dem == 1):
        so_tien = tien_phong_1_dem * 1
elif (so_dem >= 2 and so_dem <= 3):
        so_tien = tien_phong_1_dem * so_dem * 0.75
else:
        so_tien = tien_phong_1_dem * so_dem * 0.7
print("tổng số tiền phải trả:",so_tien)
