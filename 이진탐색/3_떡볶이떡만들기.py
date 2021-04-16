## 순차탐색
# def recursive(h,array):
#     sum=0
#     for i in range(len(array)):
#         resu=array[i]-h
#         if resu > 0:
#             sum=sum+resu
#     if sum>=m:
#         return h
#     else:
#         return recursive(h-1,array)
#
# n,m=map(int,input().split())
# array=list(map(int,input().split()))
# h=max(array)
#
# print(recursive(h,array))

## 이진탐색
def serch(start,end):
    if start>end:
        return 0
    h=(start+end)//2
    sum = 0
    for i in range(len(array)):
        resu=array[i]-h
        if resu>0:
            sum=sum+resu
    if sum==m:
        return h
    elif sum>m:
        return serch(h+1,end)
    elif sum<m:
        return serch(start,h-1)
n,m=map(int,input().split())
array=list(map(int,input().split()))
print(serch(0,max(array)))

"""
4 6
19 15 10 17
"""