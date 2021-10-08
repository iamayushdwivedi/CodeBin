def merge_sort(arr):
    count = 0
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            count += (len(left) - i)  # just count here !
            merged.append(right[j])
            j += 1
    for l in range(i, len(left)):
        merged.append(left[l])
    for r in range(j, len(right)):
        merged.append(right[r])
        return merged
    merge_sort(arr)
    if count % 2 == 0:
        return "YES"
    else:
        return "NO"

def main()
    arr = list(map(int(input().split())))
    print(merge_sort(arr))



def toys(w):
    w.sort()
    temp = w[0]
    count = 1
    for i in w:
        if i > temp + 4:
            temp = i
            count += 1
    return count

def main():
    n = int(input())
    while n != 0:
        w = list(map(int, input().split()))
        print(toys(w))