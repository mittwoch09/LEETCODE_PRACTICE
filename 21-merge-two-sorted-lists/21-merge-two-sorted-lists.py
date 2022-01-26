# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result= ListNode()
        tmp = result
        while list1 and list2:

            if list1.val >= list2.val:
                tmp.next = list2
                list2 = list2.next
            else:
                tmp.next = list1
                list1 = list1.next
            tmp = tmp.next
        
        if list1:
            tmp.next = list1
        elif list2:
            tmp.next = list2
        
        return result.next
    
        """
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
        """
        