#This is the program to create list.
list=['L','I','S','T']
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print('--------------------------------')

#This is the program to create list with for loop
list1=['L','I','S','T']
for i in range(0,4):
    print(list1[i])
print('--------------------------------')

# This is the program to create list by changing index value
list2=['l','i','s','t']
print(list2[0])
print(list2[-1])
print(list2[2])
print(list2[3])
print('---------------------------------')

list3=['l','i','s','t']
print(list3[-1])
print(list3[-2])
print(list3[-3])
print(list3[-4])
print('---------------------------------')

my_second=['a',5]
for i in range(0,2):
    print(my_second[i])
print('---------------------------------')
print(list3[1:3])
print(list3[1:])
print(list3[:3])
print(list3[:])
print('---------------------------------')

nlist=["Somaiya",[2,0,1,5],[3,4,5,6]]
print(nlist[0][1])
print('---------------------------------')

list4=['L','I','S','T']
print(list4[-4])
print(list4[-3])
print(list4[-2])
print(list4[-1])
print('---------------------------------')

list4[0]='A'
print(list4)

list4[1:3]='n','o','p'
print(list4)

list4[1:4]='n','o','p'
print(list4)

list4.append('z')
print(list4)
list4.append('x')
print(list4)
print('---------------------------------')

empty=[]
print(empty)

empty.insert(1,1)
empty.insert(1,3)
print(empty)
del empty[1]
print(empty)
print('---------------------------------')

del list4[1:3]
print(list4)

empty.extend([11,12,13,14,15])
print(empty)

empty.remove(11)
print(empty)

empty.pop()
print(empty)
empty.pop(0)
print(empty)
print('---------------------------------')
