mystack=[1,7,6]
stacksize=3
def display_stack():
    print("Currently stack contains")
    for i in mystack:
        print(i)

def push(value):
    if len(mystack)<=stacksize:
        mystack.append(value)
        print(mystack)
    else:
        print("Stack is false")

def pop():
    if len(mystack)>0:
        mystack.pop()
        print(mystack)
    else:
        print("Stack is empty")
print("1:Display the stacks\n 2:Push\n 3:Pop")
choice=int(input("Enter your choice:"))
if choice==1:
    display_stack()
elif choice==2:
    a=int(input("Enter the value to be pushed:"))
    push(a)
elif choice==3:
    pop()
