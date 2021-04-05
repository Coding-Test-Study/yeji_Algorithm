def dfs(v,invite,graph):
    
    print(v, end=" ")
    invite[v]=True

    for i in graph[v]:
        if invite[i]==False:
            dfs(i,invite,graph)

        
graph=[[], [2,3,8],[1,7,8],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

invite=[False]*9

dfs(1,invite,graph)