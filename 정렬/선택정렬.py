# 가장 작은 것을 골라 첫번째랑 바꾸기

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min=i
    for j in range(i+1,len(array)):
        if array[min]>array[j]:
            min=j
    array[i], array[min] =array[min], array[i]

print(array)
