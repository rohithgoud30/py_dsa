import math


def countDigits(n: int) -> int:
    # Write your code here
    # Solution 1
    return int(math.log(n, 10)) + 1
    # Solution 2
    # return len(str(n))
    # Solution 3
    # count=0
    # while n!=0:
    #     n//=10
    #     count+=1
    # return count
