size=int(input())
array=[]
for i in range(size):
    array.append(int(input()))

array.sort(reverse=True)
for i in array:
    print(i,end=" ")