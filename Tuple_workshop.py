#Tuple.py

'''students = ('Purm', 'new', 'max', 'view', 'ohm', 'friend', 'fluck')    #Tupleรายชื่อ

for std in students[0:6]:       #ระบุช่วง
    print(std)

for std in students[:3]:        #ระบุช่วง
    print(std)
    
for std in students[4:7]:       #ระบุช่วง
    print(std)

for std in students[4:1]:       #ระบุช่วง(ไม่สามารถบอกช่วง้อยกว่าได้)
    print(std)

for std in students[-1]:        #ระบุช่วง F O O K 
    print(std)'''

#Tuple_workshop.py

'''students = ('Purm', 'new', 'max', 'view', 'ohm', 'friend', 'fook', 'Ice', 'Fairy')
score = (30,25,21,28,26,30,25,21,21)


total = sum(score)
numStudent = len(score)
avg = total/numStudent

i = 0

for z in students:         #วนรอบ ระบุช่วง
    print('{} {:6} => {:5}'. format(i+0,z,score[i]))
    i +=1

print(type(students))
print('Totla:{:8}'. format(total))
print('Max Score:',max(score))
print('Min Score:', min(score))
print("Avg Score:{:6.2f}". format(avg))'''

#list_Example.py

'''score = [15,12,6,87,4]  #ประกาศสร้างlistพร้อมกำหนดข้อมูล
score.append(17)           #เพิ่มข้อมูลเข้าlist    .append(metond)
score.append(19)           #เพิ่มข้อมูลเข้าlist
score.append(44)           #เพิ่มข้อมูลเข้าlist

print(type(score))         #ข้อมูลในscore
print(score)'''

#WS1:list given total element

'''mylist = []
total_element = eval(input('Enter number of products: '))


for i in range(total_element):
    datai = eval(input('value for'+str(i)+":"))
    mylist.append(datai)

print(mylist)

amount = sum(mylist)
print('{}product(s)in Your cart. Total={}THB'. format(len(mylist),amount))'''

#ws; dict1

'''dict1 = {}

dict1['NP101'] = 'Mac'
dict1['NP102'] = 'Iphone'
dict1['NP103'] = 'Ipad'
dict1['NP104'] = 'Airpods'
dict1['NP105'] = 'applewatch'

for key in dict1:
    print(key,dict1[key])'''


#Assigment_Tuple.py
#Assigment_list_str_.py
