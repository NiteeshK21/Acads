# You are using Python
n = int(input())
lst = list(map(int,input().split()))

lst.sort()
for i in lst:
    print(i, end=" ")
