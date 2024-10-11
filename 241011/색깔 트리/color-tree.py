import sys

input = sys.stdin.readline

class Tree:

    def __init__(self, MID, PID, color, maxDepth):
        self.root = Node(MID, PID, color, maxDepth, None)
    
    def addNode(self, MID, PID, color, maxDepth):
        parent = self.findNode(self.root, PID)

        if (parent is not None and self.checkMaxDepth(parent, 2)):
            if (parent.left is None):
                parent.left = Node(MID, PID, color, maxDepth, parent)
            elif (parent.right is None):
                parent.right = Node(MID, PID, color, maxDepth, parent)
    
    def changeColor(self, MID, color):
        node = self.findNode(self.root, MID)
        
        def doChange(node, color):
            if node is None:
                return
            node.color = color
            doChange(node.left, color)
            doChange(node.right, color)
        
        doChange(node, color)

    def getNodeColor(self, MID):
        node = self.findNode(self.root, MID)
        if node is not None:
            return node.color
        return None
    
    def getPoint(self, node):
        def calc(node, colors):
            if node is None:
                return 0
            cur = 0
            if node.color not in colors:
                colors.append(node.color)
                cur += 1

            return calc(node.left, colors) + calc(node.right, colors) + cur

        return pow(calc(node, []), 2)
    
    def getAmountPoint(self, node):
        if node is None:
            return 0
        
        left = self.getAmountPoint(node.left)
        right = self.getAmountPoint(node.right)
        
        return left + right + self.getPoint(node)

    def checkMaxDepth(self, node, depth):
        if node is None:
            return True
        if depth > node.maxDepth:
            return False
        return self.checkMaxDepth(node.parent, depth + 1)
    
    def findNode(self, node, MID):
        if node is None:
            return
        if node.MID == MID:
            return node
        
        left = self.findNode(node.left, MID)
        if left is not None:
            return left
        right = self.findNode(node.right, MID)
        return right

    def inOrder(self, node):
        if (node is None):
            return
        self.inOrder(node.left)
        print(node.toString())
        self.inOrder(node.right)
        

class Node:
    def __init__(self, MID, PID, color, maxDepth, parent):
        self.MID = MID
        self.PID = PID
        self.color = color
        self.maxDepth = maxDepth
        self.parent = parent
        self.right = None
        self.left = None

    def toString(self):
        return f"MID : {self.MID} / PID : {self.PID} / COLOR : {self.color} / maxDepth : {self.maxDepth}"

def addNode(trees, command):
    if (command[2] == -1):
        trees.append(Tree(command[1], command[2], command[3], command[4]))
    else:
        for tree in trees:
            tree.addNode(command[1], command[2], command[3], command[4])

def changeColor(trees, MID, color):
    for tree in trees:
        tree.changeColor(MID, color)

def getNodeColor(trees, MID):
    for tree in trees:
        result = tree.getNodeColor(MID)
        if result is not None:
            return result

def getAmountPoint(trees):
    result = 0
    for tree in trees:
        result += tree.getAmountPoint(tree.root)
    return result

if __name__ == "__main__":
    Q = int(input())
    trees = []

    for i in range(Q):
        command = list(map(int, input().split()))
        if (command[0] == 100):
            addNode(trees, command)
        elif (command[0] == 200):
            changeColor(trees, command[1], command[2])
        elif (command[0] == 300):
            color = getNodeColor(trees, command[1])
            print(color)
        elif (command[0] == 400):
            print(getAmountPoint(trees))
    
    # tree.inOrder(tree.root)