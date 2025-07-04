arr = [1,3,2,2,2,2]

def find_the_missing_nums(arr):
    ret =[]
    se = set(arr)
    for i in range(1,len(arr)+1):
        if i not in se:
            ret.append(i)
    return ret
        
if __name__ == "__main__":
    print(find_the_missing_nums(arr))  
    