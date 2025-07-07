from typing import List, Tuple
points = [[1,1],[3,4],[-1,0]]

def mst(points : List[List[int]]) -> int:
    total_time=0
    for i in range(1,len(points)):
        x1,y1=points[i]
        x2,y2=points[i-1]
        dx =abs(x1-x2)
        dy =abs(y1-y2)
        total_time += max(dx,dy)
    return total_time

if __name__ == "__main__":
    print(mst(points)) 


        