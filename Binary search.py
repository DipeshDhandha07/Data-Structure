def BinarySearch(list_items,value):
    lb=0
    ub=len(list_items)
    ub=ub-1
    while(lb<=ub):
        mid=int((lb+ub)/2)
        if list_items[mid]==value:
            return mid
        elif value<list_items[mid]:
            ub=mid-1
        else:
            lb=mid+1
list_items=list()
num=input("Enter no of elements in list:")
num=int(num)
print("Enter elements in Sorted Order:")
for i in range(0,num):
    n=input("Enter any number:")
    list_items.append(int(n))
choice='y'
while choice=='y':
    a=input("Enter element to be searched:")
    i=BinarySearch(list_items,int(a))
    if i==-1:
        print("Value not found")
    else:
        print("Value found at position{}".format(i))
    choice=input("Do yo wish to continue(y/n):")
