#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    #二叉搜索树，如果root = None， t.root = list[0]

    @classmethod
    def create(self, sequence):
        if len(sequence) > 0:
            root = Tree(sequence[0])
        for item in sequence[1:]:
            root = self.insert(root, item)
        return root
        #self.insert(root, sequence[0])

    def insert(self, root, val):
        if root is None:
            root = Tree(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def preOrder(self):
        pass
    
    def postOrder(self):
        pass
N = 100005
class node:
    def __init__(self):
        self.val = 0
        self.left = 0
        self.right = 0

t = [node() for i in range(N)]

root, cnt = 0, 0

def insert(val, curNode):
    if curNode == 0:
        global cnt

        return curNode

    return curNode

def preOrder(curNode, ans):
    if curNode != 0:
        pass

def postOrder(curNode, ans):
    if curNode != 0:
        pass
  
# 给定一个1到n的排列，依次插入到二叉树中，返回前序遍历和后序遍历
# n：如题意
# sequence：给定的排列，大小为n
# 返回值：将要输出的元素依次加入到返回值中
def getAnswer(n, sequence):
    ''' 请在这里设计你的算法 ''' 
    global root, cnt
    root = cnt = 0

    for i in range(len(sequence)):
        root = insert(sequence[i], root)

    ans = []
    preOrder(root, ans)
    postOrder(root, ans)

    return ans

    tree = Tree.create(sequence)
    pre = tree.preOrder()
    post = tree.postOrder()

    return list(pre+post)
# ================= 代码实现结束 =================

n = int(input())
sequence = list(map(int, input().split(' ')))
ans = getAnswer(n, sequence)
print(' '.join(map(str, ans[0:n])))
print(' '.join(map(str, ans[n:n+n])))
    