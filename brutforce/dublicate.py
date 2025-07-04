# this is a brutforce  solution for the finding dublicates in the array fuckk offf 

arr = [1,3,4,5,2,3]

def find_duplicate(arr):
    for i in range(len(arr)):
        key = arr[i]
        for j in range(i + 1, len(arr)):
          if key == arr[j]:
              return True
    return False

if __name__ == "__main__":
    print(find_duplicate(arr))