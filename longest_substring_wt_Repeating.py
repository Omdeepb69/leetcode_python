def lfls(s:str):
    charSet = set()
    res= 0
    l = 0 
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

def main():
    s = "abcabcbb"
    result = lfls(s)
    print("Length of the longest substring without repeating characters:", result)
    
if __name__ == "__main__":
    main() 