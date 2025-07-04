def two_sum(nums,target):
    prevMap = {}
    for i,n in enumerate(nums):
        diff = target - n 
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
    return 

def main():
    nums= [2,4,6,3,6,8,10]
    target = 10
    result = two_sum(nums,target)
    print("Indices of numbers that add up to target:", result)
    
    
if __name__ == "__main__":
    main()