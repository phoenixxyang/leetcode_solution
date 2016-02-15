class Solution(object):
    def titleToNumber(self, s): # 68ms
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        num = 0
        for i in range(0, len(s)):
            num = num + 26**(i) * (ord(s[len(s) - i - 1]) - 64)
        return num


if __name__ == "__main__":
    testList = ["A", "B", "C", "X", "Y", "Z", "AA", "AB", "AC", "AD", "ZZ",
    "AAA", "AAB"]
    so = Solution()
    for s in testList:
        print so.titleToNumber(s)

