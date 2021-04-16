def serch(start, end,target):
    if start > end:
        return "no"
    mid=(start+end)//2
    if array[mid]>target:
        return serch(start,mid-1,target)
    elif array[mid]<target:
        return serch(mid+1,end,target)
    else:
        return "yes"

n=int(input())
array=list(map(int,input().split()))
m=int(input())
targets=list(map(int,input().split()))
array.sort()

for i in targets:
    print(serch(0,n-1,i),end=" ")


#set
# n=int(input())
# array=set(map(int,input().split()))
# m=int(input())
# targets=list(map(int,input().split()))
# for i in targets:
#     if i in array:
#         print("yes",end=' ')
#     else:
#         print("no",end=' ')

"""
5
8 3 7 9 2
3 
5 7 9
"""