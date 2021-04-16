#이진탐색
def serch(start,end):
    mid=(start+end)//2
    if start>end:
        print("원소가 존재하지 않습니다")
        return
    if list[mid]>target:
        serch(start,mid-1)
    elif list[mid]<target:
        serch(mid+1,end)
    else:
        print(mid+1)
        return


n, target = map(int,input().split())
list=list(map(int,input().split()))

serch(0,n-1)

"""
10 19
1 5 3 7 9 11 13 15 17 19
"""