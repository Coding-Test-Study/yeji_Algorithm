def setting(data):
    return data[1]
    
n=int(input())
array=[]
for i in range(n):
    name,grade=input().split()  
    array.append((name,int(grade)))

array=sorted(array,key=setting) #array =sorted(array,key=lambda data:data[1])
for i in range(n):
    print(array[i][0],end=" ")

"""
2
홍길동 95
이순신 77
"""