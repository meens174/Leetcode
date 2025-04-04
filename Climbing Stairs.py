import random
import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        options=1

        quotient=n//2
        for i in range(1,quotient+1):
            print(i)
            rem=n-i*2
            bits=rem+i
            count_1=rem
            count_2=i
            options+=math.factorial(bits)/(math.factorial(count_1)*math.factorial(count_2))
        return options

sol=Solution()
opt=sol.climbStairs(45)
print(opt)
        