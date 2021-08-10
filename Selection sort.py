#Code for selection sort
def selsort(a):
    for i in range(len(a)):
        pos=i
        for j in range(i+1,len(a)):
            if(a[pos]>a[j]):
                pos=j

                temp=a[i]
                a[i]=a[pos]
                a[pos]=a[j]
                a[j]=temp
print("Sorted array:")
a=[1,11,4,3,9,5]
for i in range(len(a)):
    selsort(a)
    print(a[i])
