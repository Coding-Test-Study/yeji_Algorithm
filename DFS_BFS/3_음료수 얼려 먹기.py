

n,m=map(int,input().split())
array=[list(map(int,input())) for _ in range(n)]

#graph 만들기 재귀함수
def group(x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    if  x<0 or y<0 or y>=m or x>=n or array[x][y]==1:
        return
    for i in range(0,4):
        group(x+dx[i],y+dy[i])
        array[x][y]=1
    
cnt=0
for i in range(0,n):
    for j in range(0,m):
        if array[i][j]==0:
            cnt=cnt+1
            group(i,j)

print(cnt)

"""
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""