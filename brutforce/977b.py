arr = [-4,1,0,3,-10]

def sqSrt(arr):
    sq = list()
    
    for i in range(len(arr)):
        sq.append(arr[i]*arr[i])
        
    sq = sorted(sq)
    
    return sq

if __name__ == "__main__":
    print(sqSrt(arr))