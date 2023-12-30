def bai11c11():
 tuple = ('red','green','yellow','blue','black','while',
         'pink','orange','red','blue')
 e = int(input('nhập số dương từ 0 -9 :'))
 f  = int(input('nhập số âm từ -1 - -9 :'))
 d  = str(input('nhập màu cần đếm số lần : '))
 a = tuple[e]
 b = tuple[-f]
 c =tuple.count(d)
 print('vị trí đứng thứ ',e,' theo chiều dương là :',a)
 print('vị trí đứng thứ ',f,' theo chiều âm là',b)
 print('số lần lặp của ',d,'là ',c,'lần')

def bai12c11():
 tuple_a = [3,1,2,4]
 tuple_b = [5,7,6,8]
 tuple_c = tuple_a + tuple_b
 tuple_d =   sorted(tuple_c)
 print('Tuple d :',tuple_d)
 print('Tuple c: ',tuple_c)
 print('Tuple[3] :',tuple_d[3])
 print('Tuple [5 :]',tuple_d[5:])





