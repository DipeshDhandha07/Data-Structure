class delimeters:
    def __init__(self):
        self.item=[]
        self.size=-1

    def push(self,value):
        self.items.append(value)
        self.size+=1

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()

    def isEmpty(self):
        if(self.size==-1):
            return True
        else:
            return False

    def matchingDelimeters(self,expr):
        print("Inside the matchingDelimeters")
        openingbr='({['
        closingbr=')}]'
        for i in expr:
            if i in openingbr:
                self.push(i)
            elif i in closingbr:
                if self.isEmpty():
                    print("Unordered delimeters")
            elif closingbr.index(i)!= openingbr.index(self.pop()):
                print("Unordered delimeters")
                return  False
                print("Correctly Ordered delimeters")
D=delimeters()
string=input("Enter the expression to be checked:")
D.matchingDelimeters(string)
