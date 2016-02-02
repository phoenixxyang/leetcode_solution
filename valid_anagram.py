import pdb

class Solution(object):
    def isAnagram(self, s, t): # 839ms
        if len(s) != len(t):
            return False
        for letter in t:
            pdb.set_trace()
            if letter in s:
                s = s.replace(letter, '', 1)
                continue
            else:
                return False
        return True

    def isAnagram2(self, s, t): # 48ms
        if len(s) != len(t):
            return False

        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        return True
