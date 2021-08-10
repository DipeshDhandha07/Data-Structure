def linear_search(list,value):
    for i in range(0,len(list)):
        if list[i]==value:
            return i
    return(-1)
item=list()
num=int(input("Enter no of elements:"))
for i in range(0,int(num)):
    n=input("Enter elements:")
    item.append(int(n))
choice='y'
while(choice=='y'):
    s=input("Enter elements to be searched:")
    i=linear_search(item,int(s))
    if i==-1:
        print("Value not found")
    else:
        print("Value found at position {}".format(i))
        choice=input("Do you wish to continue(y/n):")
