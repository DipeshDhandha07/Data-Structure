class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key()
        root=Node()

#Inorder tree=4,2,5,1,3(Left,Root,Right)
    def PrintIndex(root):
        if root:
        #first reccur on left child
            print Inorder(root.left)
            print(root.val)
        #now reccur of right child
            print Inorder(root.right)
            print(root.val)

    def PrintPreorder(root):
        if root:
        # Printkey rootnode/value
            print(root.val)
        # Reccur on left child
            print Preorder(root.left)
        # Finally reccur on right child
            print Preorder(root.right)
