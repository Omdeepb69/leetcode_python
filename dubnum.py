def find_dub(arr):
    se = set(arr)
    if len(se) == len(arr):
        return False 
    return True

if __name__ == "__main__":
    arr = list(map(int,input("enter the elements of the array :").split()))
    print(find_dub(arr))