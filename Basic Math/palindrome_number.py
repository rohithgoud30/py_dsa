# Solution 1
n = int(input())
# print('true' if str(n)[::-1]==str(n) else 'false')
# Solution 2
org = n
rev = 0
while n != 0:
    rev = rev * 10 + n % 10
    n //= 10
print("true" if rev == org else "false")
