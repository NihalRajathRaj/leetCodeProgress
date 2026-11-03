# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        temp = head
        result = 0
        while temp:
            result = result * 2 + temp.val
            temp = temp.next
        return result
