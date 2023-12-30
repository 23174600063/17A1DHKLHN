def tinh_bmi(can_nang,chieu_cao):
    bmi = can_nang / (chieu_cao*chieu_cao)
    return bmi
def danh_gia_bmi(bmi):
    if bmi < 18.5:
        return " Gầy"
    elif 18.5<= bmi <= 24.9:
        return "Bình thường"
    else :
        return "Thừa cân"
chieu_cao = 1.60    # đơn vị m
can_nang = 52       # đơn vị kg
bmi = tinh_bmi(chieu_cao,can_nang)
danh_gia = danh_gia_bmi(bmi)
print("Chỉ số BMI:", bmi)
print("Kết quả đánh giá theo chỉ số:", danh_gia)




