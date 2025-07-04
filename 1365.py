arr = [8, 1, 2, 2, 3]

def find_how_many_smaller(arr):
    arr2 = sorted(arr)  
    d = {}
    for i, nums in enumerate(arr2):
        if nums not in d:
            d[nums] = i
            
    ret = []
    for i in arr:
        ret.append(d[i])
        
    return ret

if __name__ == "__main__":
    print(find_how_many_smaller(arr))  
