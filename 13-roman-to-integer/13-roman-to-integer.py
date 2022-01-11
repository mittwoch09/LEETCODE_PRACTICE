class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and roman_dic[s[i]] > roman_dic[s[i - 1]]:
                decimal += roman_dic[s[i]] - (2 * roman_dic[s[i - 1]])
            else:
                decimal += roman_dic[s[i]]
        return decimal
