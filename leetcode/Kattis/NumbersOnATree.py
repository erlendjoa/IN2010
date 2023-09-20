class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

class Tree:
    def __init__(self, H):
        self.H = H
        self.n = 0
        self.root = Node(self.n)

    def findN(self, H):
        if (H > 0):
            self.n += self.findN(H)
            self.n += self.findN(H)
            H -= 1
        return 1
        
    def setTree(self):
        node = self.root
        for i in range(H-1):
            self.n += 1
            if node.left == None:
                node.left = Node(self.n)
            else:
                self.right = Node(self.n)
                node = node

inp = input()
inputArr = inp.split(" ")
H = int(inputArr[0])
CMD = inputArr[1]

tree = Tree(3)
tree.findN
print(tree.n)