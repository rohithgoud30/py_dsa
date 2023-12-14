# Solution 1
n = int(input())
sum = 0
copy = n
l = len(str(n))
while n != 0:
    rem = n % 10
    sum += rem**l
    n = n // 10
print("true" if copy == sum else "false")
