from typing import List


# Solution 1
# def printDivisors(n: int) -> List[int]:
#     # Write your code here
#     res=list()
#     for i in range(1,n+1):
#         if n%i==0:
#             res.append(i)
#     return res
# Solution 2:
def printDivisors(n: int) -> List[int]:
    # Write your code here
    res = list()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // i)
    return sorted(res)
