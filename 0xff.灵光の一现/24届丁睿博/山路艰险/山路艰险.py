"""
题目描述
    蒜头君看着眼前从左到右在一条线上的n座山峰，
    他想从中选出两座山峰，作为旅行的起点和终点，要求选出的较左边的山峰高度大于选出的较右边的山峰，
    定义这样选择后这次旅行的困难程度为两座山峰的高度差。
    问所有可能的选择方案中困难程度最大的方案的困难程度是多少，如果没有合法方案，答案为0。
输入格式
    输入有两行:
        第一行为一个整数n，表示山峰的数目(1≤n≤10^5)
        第二行为几个空格隔开的整教a¡,为每座山峰的高度(1≤a¡≤10^9)
输出格式
    输出一行，包含一个整数，表示答案。
"""
n = int(input())
li = input().split(' ')
s = 0
for i in range(n):
    li[i] = int(li[i])
for i in range(n-1):
    temp = li[i] - li[i+1]
    s = s if s >= temp else temp
print(s)
