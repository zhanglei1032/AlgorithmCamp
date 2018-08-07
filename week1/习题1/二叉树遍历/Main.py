#
# !/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
N = 100005
class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#t = [node() for i in range(N)]

root= node(0)

# 在以root为根的树中插入一个数字val
# val: 要插入的数字
# root: 当前节点
# 返回值：root
def insert(val, root):
    if root:
        # root = node(val) 
        if root.val < val:
            insert(val, root.left)
        else:
            insert(val, root.right) 
        return root

# 前序遍历首先访问根结点然后遍历左子树，最后遍历右子树。在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。
def preOrder(curNode, ans):
    if curNode:
        ans.append(curNode.val)
        preOrder(curNode.left, ans)
        preOrder(curNode.right, ans)
        return ans

# 后序遍历首先遍历左子树，然后遍历右子树，最后访问根结点，在遍历左、右子树时，仍然先遍历左子树，然后遍历右子树，最后遍历根结点
def postOrder(curNode, ans):
    if curNode:
        postOrder(curNode.right, ans)
        ans.append(curNode.val)
        postOrder(curNode.left, ans)
        return ans
  
# 给定一个1到n的排列，依次插入到二叉树中，返回前序遍历和后序遍历
# n：如题意
# sequence：给定的排列，大小为n
# 返回值：将要输出的元素依次加入到返回值中
def getAnswer(n, sequence):
    ''' 请在这里设计你的算法 ''' 
    global root 
    for i in range(len(sequence)): 
        root = insert(sequence[i], root)

    ans = []
    preOrder(root, ans)
    postOrder(root, ans)

    return ans 

# ================= 代码实现结束 =================

n = int(input())
sequence = list(map(int, input().split(' ')))
ans = getAnswer(n, sequence)
print(' '.join(map(str, ans[0:n])))
print(' '.join(map(str, ans[n:n+n])))
    