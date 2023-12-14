# Solution 1
# a=int(input())
# b=int(input())
# gcd=1
# for i in range(1,min(a,b)+1):
#     if(a%i==0 and b%i==0):
#         gcd=i
# print(gcd)

# or

# a=int(input())
# b=int(input())
# gcd=1
# for i in range(min(a,b),0,-1):
#     if(a%i==0 and b%i==0):
#         gcd=i
#         break
# print(gcd)


# Solution 2
# Euclidean’s theorem
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
