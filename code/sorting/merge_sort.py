def merge(arr, low, mid, high):
    A = arr[low : mid + 1]
    B = arr[mid + 1 : high + 1]

    i = j = k = 0
    m = len(A)
    n = len(B)

    C = [0] * (m + n)

    while i < m and j < n:
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
            k += 1
        else:
            C[k] = B[j]
            j += 1
            k += 1
        
    while i < m:
        C[k] = A[i]
        i += 1
        k += 1

    while j < n:
        C[k] = B[j]
        j += 1
        k += 1
    
    return C



def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        arr[low : high + 1] = merge(arr, low, mid, high)



if __name__ == "__main__":
    arr = [4, 1, 8, 7]
    low = 0
    high = len(arr) - 1

    print("Before Sorting:", arr)
    merge_sort(arr, low, high)
    print("After Sorting:", arr)