class Node:
    def __init__(self, dataval=None) :
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self) :
        self.headval = None

    def Inbetween(self,middle__node,newdata) :
        if middle__node is None:
            print("The mentioned node is absent")
            return
        else:
            NewNode = Node(newdata)
            NewNode.nextval = middle__node.nextval
            middle__node.nextval = NewNode
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
e4=Node("Thu")
list.headval.nextval=list.headval
list.headval.nextval=e2
e2.nextval=e3
list.Inbetween(list.headval,"sun")
list.listprint()
