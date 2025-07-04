nums = [1,0,5,20]



def find_missing_number(nums):
    for i in range(max(nums)):
        if i not in nums:
            print(i)
            
            
if __name__ == "__main__":
    find_missing_number(nums)
    print("are the missing numbers in the array")

