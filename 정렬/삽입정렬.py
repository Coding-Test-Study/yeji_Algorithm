array=[7,8,2,4,3,1,0,6,9,5]
for i in range(len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break

print(array)
