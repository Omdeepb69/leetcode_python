mat = list([[1,2,3],[4,5,6],[7,8,9]])


def sp_pr(mat: list[list[int]]) -> list[int]:
    r = list()
    if not mat:
        return r
    
    top,bottom = 0,len(mat)-1
    left,right=0,len(mat[0])-1
    
    while top <= bottom and left <= right:
        for i in range(left,right+1):
            r.append(mat[top][i])
        top += 1
        
        for i in range(top,bottom+1):
            r.append(mat[i][right])
        right -= 1
            
        for u in range(right,left-1,-1):
            r.append(mat[bottom][u])
        bottom -= 1
            
        for i in range(bottom,top-1,-1):
            r.append(mat[i][left])
        left += 1
            
    return r
    
    
if __name__ == "__main__":
    print(sp_pr(mat))  

