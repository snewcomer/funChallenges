def rotate(arr, n):
    n %= len(arr)
    print arr[-n:]+arr[:-n]
