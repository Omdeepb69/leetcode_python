def two_sum(arr, target):
    seen = dict()
    for i, num in enumerate(arr):
        comp = target - num
        if comp in seen:
            return [arr[seen[comp]], arr[i]]
        seen[num] = i
    return []

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(two_sum(arr, 4))  
