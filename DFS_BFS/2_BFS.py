from collections import deque

def bfs(first,visite,graph):
    queue=deque([first])
    visite[first]=True
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visite[i]:
                queue.append(i)
                visite[i]=True

graph=[[], [2,3,8],[1,7,8],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visite = [False] * 9

bfs(1,visite,graph)
