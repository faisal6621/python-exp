#Bubble sort example 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n -1-i):
            if arr[j]> arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr;
# Lets use above function:
arr = [9,8,7,6,5,4,3,2,1,0]
arr1 = bubbleSort(arr)
for i in range(len(arr1)):
    print(arr1[i])