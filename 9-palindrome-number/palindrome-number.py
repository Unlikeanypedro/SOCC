class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i,li in enumerate(x):
            if li != x[- i - 1]:
                return False
        return True