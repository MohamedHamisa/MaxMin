def maxMin(k, arr):
    arr = sorted(arr)
    return min([arr[i+k-1] - arr[i] for i in range(len(arr)-k+1)])

