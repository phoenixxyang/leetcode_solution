class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 4:
            return True
        
        x = (n - 4) % 4
        if x in [1,2,3]:
            return True
        else:
            return False;

    def canWinNim2(self, n):
        return (n % 4) != 0
