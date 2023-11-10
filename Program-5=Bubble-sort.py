def bubblesort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

n= int(input("Enter the number of elements: "))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)
bubblesort(arr)
print("Sorted array ")
print(arr)
