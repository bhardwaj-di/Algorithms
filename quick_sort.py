def quick_sort(arr,left,right):
    if left < right :
        partition_index = partition(arr,left,right)
        quick_sort(arr,left,partition_index-1)
        quick_sort(arr,partition_index+1,right)

    return arr
def partition(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i],arr[right] = arr[right], arr[i]

    return i

a = [102,23,45,2,4,98,204]
sort_arr = quick_sort(a,0,len(a)-1)
print(sort_arr)