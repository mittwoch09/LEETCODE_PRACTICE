from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []                                              
        brkt = {')': '(', '}': '{', ']': '['}                   
        brkt_open = brkt.values()                              

        for ch in s:                                           
            if ch in brkt_open:                                 
                stack.append(ch)                                
            else:                                               
                if len(stack) > 0 and stack[-1] == brkt[ch]:    
                    stack.pop()                                 
                else:                                           
                    return False                                
        return len(stack) == 0                                  