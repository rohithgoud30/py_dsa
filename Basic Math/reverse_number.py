class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Solution 1
        rev = 0
        last = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            last = x % 10
            rev = rev * 10 + last
            x //= 10

        result = sign * rev

        if result <= (-(2**31)) or result >= (2**31 - 1):
            return 0
        return result
        # Solution 2
        # sign= -1 if x<0 else 1
        # x=abs(x)
        # rev=sign*int(str(x)[::-1])

        # if rev <= (-2**31) or rev >= (2**31 - 1):
        #     return 0
        # return rev
