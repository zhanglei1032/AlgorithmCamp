#!/usr/bin/env python3

# ================= 代码实现开始 =================\

''' 请在这里定义你需要的全局变量 '''

# 这是匹配函数，将所有匹配位置求出并返回
# n：串 A 的长度
# A：题目描述中的串 A
# m：串 B 的长度
# B：题目描述中的串 B
# 返回值：一个 list，从小到大依次存放各匹配位置
def match(n, A, m, B):
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n = int(input())
A = input()
m = int(input())
B = input()
ans = match(n, A, m, B)
for i in ans:
    print(i)
