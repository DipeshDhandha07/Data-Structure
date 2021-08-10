#To create a set
set1=set()
set1.add("Dipesh")
set1.add("Harshit")
set1.add("Shubham")
set1.add("Ganesh")
set1.add("Aayush")
print(set1)

#To create two sets and find common names
set2=set()
set2.add("Dipesh")
set2.add("Harshit")
set2.add("Aayush")
print(set2)

set3=set()
set3.add("Dipesh")
set3.add("Ganesh")
set3.add("Harshit")
print(set3,"\n")

if set2==set3:
    print("Both sets are equal")
else:
    common_names=set2.intersection(set3)
    print("Common names are", common_names)

if common_names==0:
    print("No common names are found")
else:
    print("Common names are found")
for std_names in common_names:
    print(std_names)

if set2==set3:
    print("Both sets are equal")
else:
    unique_names=set2.difference(set3)
    print("\nUnique names are",unique_names)

if unique_names==0:
    print("No unique names are found")
else:
    print("Unique names are found")
for std_names in unique_names:
    print(std_names,"\n")

set3=set()
set3.add("Dipesh")
set3.add("Divya")
set3.add("Niyati")
set3.add("Riddhi")
print(set3)

set4=set()
set4.add("Jash")
set4.add("Raj")
set4.add("Vaibhav")
set4.add("Rajat")
print(set4)

class set:
    def __init__(self):
        self_the_element=list()

    def len(self):
        return len(self_the_element)

    def contains(self_the_element):
        return element in self_the_element

    def add(self,element):
        if element not in set:
            self_the_element.append(element)

    def remove(self,element):
        assert element in self("The element should be in the first list")
        self_the_element.remove(element)

    def eq(self,set3):
        if len(self1=set3):
            return false
        else:
            return self1(set3)

    def subset_of(set3):
        for element in set3:
            if element==self:
                return true
            else:
                return false

    def union(self,set3):
        newset=set()
        newset.element.extend(self_the_element)
