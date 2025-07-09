arr = [-4,1,0,3,-10]

def sqSrt(arr):
    n = len(arr)
    res = [0]*n
    l,r = 0,n-1
    pos = n-1
    
    while l < r:
        left_sq = arr[l]*arr[l]
        right_sq = arr[r]*arr[r]
        
        if left_sq > right_sq :
            res[pos] = left_sq
            l += 1
        else:
            res[pos] = right_sq
            r -= 1
            
        pos -= 1
        
    return res

if __name__ == "__main__":
    print(sqSrt(arr))