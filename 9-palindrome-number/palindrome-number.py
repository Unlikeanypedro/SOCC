class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for li in range(len(x)/2):
            if x[li] != x[-li-1]:
                return False
        return True