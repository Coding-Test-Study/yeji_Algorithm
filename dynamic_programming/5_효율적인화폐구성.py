# n,m=map(int,input().split())
# array=[]
# for i in range(n):
#     array.append(int(input()))
# dp=[0]*(m+1)
# for i in range(1,len(dp)+1):
#     for j in range(len(array)):
#         if m-dp[i-1]>=array[j]:
#             dp[i]=max(dp[i-1]+array[j],dp[i])
#     print(i, ":", dp[i])
#
#     if m - dp[i] == 0:
#         print(i)
#         break
#     if m-dp[i-1]<min(array):
#         print("-1")
#         break
"""
4 19
2
5
4
3
"""
