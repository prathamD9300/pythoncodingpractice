def kLargest(arr,N,K):
    arr1 = arr.sort(reverse = True)
    for i in range(0,K):
        print(arr[i],end=' ')
n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
kLargest(arr,n,k)
