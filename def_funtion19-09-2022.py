#funtion_1.py

'''myPrint()'''         #เกิด Error name (not defined)

'''def myPrint():
    print('Hello,')
    print('Noppadol.P')


myPrint()       #ไม่มีจำเป็นต้องมา Parameter
myPrint()       #สามารถเรียกได้หลายครั้ง
myPrint()'''  

#funtion_2.1.py

'''def calArea(len):
    area = len * len
    return area
    print('Area = {}'. format(area))
    
x = 3
calArea(x)'''

#funtion_2.2.py

'''def calArea(len):
    area = len * len
    return area

x = 3
a = calArea(x)  #Argument
y = 6
b = calArea(y)

print('Area = {} {}'. format(a, b))'''

#main program โปรแกรมหลัก

'''def calArea(len):
    area = len * len
    return area
if __name__=='__main__'    #'__main__'  , if เว้นวรรคเสมอ    
  x = 3
  a = calArea(x)
  print('Area = ',a)'''

'''def calArea(a,b):
    area = a*b
    perimeter  = (2*a)+(2*b)
    print('Lenght : {} Width : {} '. format(a, b))
    print('Area = ',area)
    print('Perimeter',perimeter)
    return area


#main program
rec1 = calArea(2, 3)
rec2 = calArea(15, 4)
rec3 = calArea(10, 7)

total_Area = rec1 + rec2 + rec3

print('Total area = {} '. format(total_Area))'''

#local_funtion.py

'''def function():
    x = 4.5
    y = 3.4
    print(x)
    print(y)

function()          #NameError: name 'x' is not defined
print(x)
print(y)

x = 1           #Gobal var
y = 2'''


'''def myfunc():
    global x    #กำหนดให้ตัวแปร x ในฟังชันก์มีการอัพเดทกับตัวแปร global ด้วย
    x = 8       #local  var
    print('in function x = {} y = {}'. format(x, y))
    return x

#main program    , เมื่อมาตรงนี้แล้วตัวข้างบนไม่เกี่ยวกัน
if __name__=='__main__':
  myfunc()
  print('in Main Prg x = {} y = {}'. format(x, y))'''

'''def first(a,b):
    y = a + b
    z = a * b
    return y, z

#first()     #TypeError: first() missing 2 required positional arguments: 'a' and 'b'
#first(3)     #TypeError: first() missing 2 required positional arguments: 'a' and 'b'

a = first(1,2)  #
print('num:{}'. format(a))'''

#default_perimter.py

'''def second(a=2,b=4):
    y = a + b;
    z = a * b;
    return y, z
                                        #(นิยมแบบนี้เป็นส่วนมาก)
j = second()
print(j)            #(6, 8)

k = second(a=1)     #(5, 4)
print(k)

print(second(b=5))          #(7, 10)
print(second(3, 2))         #(5, 6)
print(second(a=20, b=14))   #(34, 280)
'''

#Assigment_discount.py
'''
def myPrice():
    calDiscount = Price * (5/100)
    DiscountNET = Price - calDiscount
    return DiscountNET,calDiscount


if price > 0:
    cal = myPrice()
    print('Discount:{} '. format(cal))
else:
    print('not discount')


Price = eval(input('Enter product price: '))
DiscountNET,calDiscount = myPrice()
print('Discount: {}, Net: {} '. format(DiscountNET,calDiscount))
'''

#Grading.py

def youSC():
    AmountSC = ComProMidSC + ComProFinalSC
    return AmountSC

ComProMidSC = eval(input('Enter Midterm score: '))
ComProFinalSC = eval(input('Enter Final score: '))


GPAcomPro = youSC()

if GPAcomPro >= 80:
    Grade = 'A'
elif GPAcomPro >= 70:
    Grade = 'B'
elif GPAcomPro >= 60:
    Grade = 'B'
elif GPAcomPro >= 50:
    Grade = 'B'
else:
    Grab = 'F'
    
print('MID: {} Final: {} Total score: {} --> Grade: {}'. format(ComProMidSC, ComProFinalSC, GPAcomPro, Grade))



14

