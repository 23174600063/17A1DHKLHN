def bai1c11():
 a = [1,2,3]
 b = [1,[2,3]]
 c = []
 d = [1,2,3][1:]
 print('đọ dài của a = ',len(a))
 print('độ dài củ b = ',len(b))
 print('đọ dài của c = ',len(c))
 print('độ dài của d = ',len(d))
 e = len(a)+ len(b)+len(c)+len(d)
 print('độ dài của tất cả các chuổi là =',e)
    
def bai2c11():
 teams=[['steven','neena','lex','alexander','bruce']
       ,['david','jack','bill','tom','mike','daniel']
       ,['alexander','adam','payam','kelvin','sigal','mike']]
 a =teams[2][1]
 print('đội trưởng của đội yếu nhất là : ',a)

def bai3c11():
 list = ['ant','bear','cat','dog','elephant','fish','goat','hippo','tigger','meal']

 print('danh sách các con thú gồm : ',list)
 a = str(input("nhập con thú cần tìm: "))
 b = list.index(a)
 print('con thú bạn cần tìm ở vị trí thứ ',b,'trong chuỗi các con thú')
 print('số lương các con thú là',len(list))

def bai4c11():
 a = []
 while True:
  i = int(input('Tiếp tục nhập giá trị không ? 1:Có, 2: không :   '))
  if i==1:
     a = int(input('Nhập giá trị bạn muốn thêm vào danh sách: '))
     list.append(a)
  elif i ==0:
    break
 print("List bạn vừa nhập là : ",list)
# tìm giá trị x trong list
x = int(input('NHập X đi iem yêu :'))
find = x in list
if find:
   print(x,'Có lặp trong dãy List ,số lần lặp của x là :',list.count(x))
else:
   print(x,'không xuất hiện trong dãy List')

# tìm coi phải max không
list1 =[]
if x == max(list):
   print(x,'Là number lớn nhất in List bạn vừa nhập')
else:
   for i in list:
      if i >x:
         list1.append(i)
print('danh sách các số lớn hơn ',x,'là',list1)
    
   
print('tổng các number trong list là :', sum(list))

def bai5c11():
 list_numbers2 = []
 while True:
  i = int(input('Tiếp tục nhập giá trị không ? 1:Có, 2: không :   '))
  if i==1:
     a = int(input('Nhập giá trị bạn muốn thêm vào danh sách: '))
     list_numbers2.append(a)
  elif i ==0:
    break
 print("List bạn vừa nhập là : ",list_numbers2)

# tìm số nguyên tố trong list

list_nguyen_to =[]
for a in list_nguyen_to:
   if a < 2 :
      continue
   nt = True
   for i in range(2,a+1):
      if a % i ==0:
         nt = False
         break
      if nt:
        list_nguyen_to.append(a)

print('Danh sách các số nguyên tố trong list_numbers2 là : ',list_nguyen_to)

# Tính trung bình cộng của phần tử âm và duong
phan_tu_am = [x for x in list_nguyen_to if x < 0]
phan_tu_duong = [x for x in list_nguyen_to if x > 0]
TB_am = sum(phan_tu_am)/len(phan_tu_am) if phan_tu_am else 0
TB_duong = sum(phan_tu_duong)/len(phan_tu_duong) if phan_tu_duong else 0
print("Trung bình cộng các phần tử âm :", TB_am)
print("Trung bình cộng các phần tử dương:", TB_duong)

def bai6c11():
 height_inch =[74,74,72,72,73,69,69,71,76,71]
# chiều cao trung bình 
 a = sum(height_inch)/len(height_inch)
# chiều cao nhất
 b = max(height_inch)
 c = min(height_inch)
# in ra 3 chiều cao đầu cuối
 d  = height_inch[:3]
 e = height_inch[-3:]
# sắp xếp tăng dần , nhỏ dần
 f = sorted(height_inch)
 g = height_inch
 h =g.reverse()
 print("Chiều cao trung bình là:",a)
 print("chiều cao lớn nhất là: ",b)
 print("chiều cao nhỏ nhất là: ",c)
 print("3 chiều cao đầu:",d)
 print("3 chiều cao cuối:", e)
 print("Xắp xếp list theo giá trị tăng dần là:",f)
 print("Xắp xếp list theo thứ tự giảm dần là:",g)
 print("đổi đơn vị sang inch: ",h)

def bai7c11():
 thresh=int(input('nhập số:'))
 a=[]
 def elementwice_greater_than(L,thresh):
     for i in L:
         if i <= thresh:
             b=False
             a.append(b)
         if i > thresh:    
             b=True
             a.append(b)
     return a
 print(elementwice_greater_than(L,thresh))
    
def bai8c11():
 nums=[1,2,3,4,7,5,6,8,9]
 def has_lucky_numbers(nums):
     for i in nums:
        if i%7==0:
            print(True)
            break 
     else:
        print(False)
     return
 has_lucky_numbers(nums)
    
def bai9c11():
 arivals = ['Adela','Fleda','Owen',
           'May','Mona','Gilbert','Ford']
 def party_late(arivals,name):
    if(arivals.index(name)+1)==(len(arivals)):
        return False
    if(arivals.index(name)+1)>(len(arivals)/2):
        return True
    else:
        False
 print(party_late(arivals,name='Gilbert'))
 print(party_late(arivals,name="Ford"))
 print(party_late(arivals,name="Mona"))

def bai10c11():
 meals_1 = ['redneck ribs','prawn star','san quentin squid',
           'fist full of pizza','honky tonk chicken']
 meals_2 = ['redneck','prawn star','running bear salmon',
           'running bear salmon','honky tonk chicken']

 def meal(ls):
    for i in range(len(ls)):
        for j in range(i +1 ,len(ls)):
            if ls[i]==ls[j]:
                return True
    return False


# Kiểm tra xem có phần tử trùng nhau trong list không
 a = meal(meals_1)
 b = meal(meals_2)

 print(f'Bữa ăn 1 có phần tử trùng nhau không?',a)
 print(f'Bữa ăn 2 có phần tử trùng nhau không?',b)  








