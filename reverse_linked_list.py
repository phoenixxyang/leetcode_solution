# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head): # 48ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head

        prev = head
        node = head.next
        prev.next = None
        while node.next:
            temp_node = node.next
            node.next = prev
            prev = node
            node = temp_node
        node.next = prev
        return node
