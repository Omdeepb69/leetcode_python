#268 Missing Number

nums = [0,1,2]

def find_missing_number(nums):
    n = len(nums)
    expected_total = n * (n + 1) //2
    actual_total = sum(nums)
    missing_number = expected_total - actual_total
    return missing_number

if __name__ == "__main__":
    print(find_missing_number(nums))
    print("is the missing number in the array")