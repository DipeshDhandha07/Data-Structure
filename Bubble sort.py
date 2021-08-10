#Code for bubble sort
def bubblesort(a1):
    for i in range(len(a1)):
        for j in range(len(a1)-i-1):
            if (a1[j]>a1[j+1]):
                temp=a1[j]
                a1[j]=a1[j+1]
                a1[j+1]=temp
a1=[12,13,23,78,9,8,7,5]
print(a1)
print("Length:",len(a1))
print("\nSorting the list:")
bubblesort(a1)
print(a1)
