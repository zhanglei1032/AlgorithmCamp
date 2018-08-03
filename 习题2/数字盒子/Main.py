#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
Mod = 1000003
table = [[] for i in range(Mod)]

def Hash(x):
    return x % Mod

# 执行操作时会调用这个函数
# op：对应该次操作的 op（具体请见题目描述）
# x：对应该次操作的 x（具体请见题目描述）
# 返回值：如果输出为"Succeeded"，则这个函数返回 1，否则返回 0
def check(op, x):
    ''' 请在这里设计你的算法 ''' 
    # 插入 
    h = hash(x) 
    ptr = -1
    hlist = table[h]
    for i in range(len(hlist)):
        if hlist[i] == x:
            ptr = i
            break
    if op == 1:
        if not x in hlist:
            hlist.append(x)
            return 1
    else:
        if x in hlist: 
            hlist.pop(ptr)
            return 1 
    return 0
        


# ================= 代码实现结束 =================

Q = int(input())
for _ in range(Q):
    op, x = map(int, input().split()) 
    print("Succeeded" if check(op, x) else "Failed")