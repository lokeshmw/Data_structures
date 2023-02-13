def bucket_sort(arr):
    n = len(arr)
    max_data = max(arr)
    list_ = []
    buckets = [list_] * 10
    for i in range(n):
        j = int(n * arr[i] / (max_data + 1))
        if len(buckets[j]) == 0:
            buckets[j] = [arr[i]]
        else:
            buckets[j].append(arr[i])
    for i in range(10):
        insertion_sort(buckets[i])
    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i].pop(0)
            k = k + 1


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = current_value


Array = [23, 32, 55, 47, 234, 111, 78]
print('Original_Array:', Array)
bucket_sort(Array)
print('Sorted_Array:', Array)
