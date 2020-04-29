aparitii=[0]*2000001
index=1000000
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        self.splay(node)

    def find_function(self, node, key):
        if node == None or key == node.data:
            return node

        if key < node.data:
            return self.find_function(node.left, key)
        return self.find_function(node.right, key)

    def find_node(self, k):
        x = self.find_function(self.root, k)
        if x != None:
            self.splay(x)
            return x
        else:
            return None

    def find(self,x):
        if self.find_node(x):
            g.write(str(1)+"\n")
        else:
            g.write(str(0)+"\n")

    def delete_function(self, node, key):
        x = None
        tree1 = None
        tree2 = None
        while node != None:
            if node.data == key:
                x = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if x == None:
            g.write(str(aparitii[index+key]))
            return

        self.splay(x)
        if x.right != None:
            tree1 = x.right
            tree1.parent = None
        else:
            tree1 = None

        tree2 = x
        tree2.right = None
        x = None

        if tree2.left != None:
            tree2.left.parent = None

        self.root = self.join(tree2.left, tree1)
        tree2 = None

    def delete(self, data):
        self.delete_function(self.root, data)

    def rotate_Left(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_Right(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    self.rotate_Right(x.parent)
                else:
                    self.rotate_Left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.rotate_Right(x.parent.parent)
                self.rotate_Right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.rotate_Left(x.parent.parent)
                self.rotate_Left(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.rotate_Left(x.parent)
                self.rotate_Right(x.parent)
            else:
                self.rotate_Right(x.parent)
                self.rotate_Left(x.parent)

    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    def join(self, tree1, tree2):
        if tree1 == None:
            return tree2

        if tree2 == None:
            return tree1

        x = self.maximum(tree1)
        self.splay(x)
        x.right = tree2
        tree2.parent = x
        return x

    def afisare(self, node):
        if node != None:
            print(node.data,end=" ")
            self.afisare(node.left)
            self.afisare(node.right)

    def preorder(self):
        self.afisare(self.root)
        print("")

    def successor(self, x):
        while self.find_node(x) == None:
            x+=1
            if x > 1000001:
                return -1

        return self.find_node(x).data

    def predecessor(self, x):
        while self.find_node(x) == None:
            x-=1
            if x<-1000001:
                return -1

        return self.find_node(x).data

    def interval(self,x,y):
        for i in range(x+1,y):
            if self.find_node(i) != None:
                g.write(str(i)+" ")
        g.write("\n")




f=open("abce.in","r")
g=open("abce.out","w")

N=int(f.readline())
lines=f.readlines()
tree=SplayTree()
for i in lines:
    if int(i[0]) == 1:
        tree.insert(int(i[2:]))
        aparitii[index+int(i[2:])]+=1
    if int(i[0]) == 2:
        tree.delete(int(i[2:]))
    if int(i[0]) == 3:
        tree.find(int(i[2:]))
    if int(i[0]) == 4:
        g.write(str(tree.successor(int(i[2:])))+"\n")
    if int(i[0]) == 5:
        g.write(str(tree.predecessor(int(i[2:])))+"\n")
    if int(i[0]) == 6:
        tree.interval(int(i[2:i.find(" ",2)]),int(i[i.find(" ",2):]))
f.close()
g.close()