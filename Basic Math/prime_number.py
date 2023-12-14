# Solution 1
# n = int(input())
# flag = "true"
# for i in range(2, n):
#     if n % i == 0:
#         flag = "false"
#         break
# print(flag)
# Solution 2
n = int(input())
flag = "true"
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        flag = "false"
        break
print(flag)
