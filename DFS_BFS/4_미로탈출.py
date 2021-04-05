# n, m = map(int,input().split())
# graph=[list(map(int,input())) for _ in range(n)] 

# def maze(x,y,cnt):
#     dx=[-1, 0, 1, 0]
#     dy=[0, 1, 0, -1]
#     if x<0 or y<0 or y>=m or x>=n or graph[x][y]==0:
#         return
#     for i in range(0,4):
#         cnt=cnt+1
#         if graph[x][y]>cnt:
#             graph[x][y]=cnt
#         maze(x+dx[i],y+dy[i],cnt)
        

# maze(1,1,0)    
# print(graph)

from collections import deque

n, m = map(int,input().split())
maze=[list(map(int,input())) for _ in range(n)] 
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x, y=queue.popleft()
        for i in range(4):
            subx=x+dx[i]
            suby=y+dy[i]
            if subx<0 or suby<0 or subx>=n or suby>=m:
                continue
            if maze[subx][suby]==0:
                continue
            if maze[subx][suby]==1:
                maze[subx][suby]=maze[x][y]+1
                queue.append((subx,suby))
                print(subx,suby)
bfs(0,0)
print(maze)
print(maze[n-1][m-1])

"""
5 6
101010
111111
000001
111111
111111

4 5
10101
10101
11101
01111
"""
