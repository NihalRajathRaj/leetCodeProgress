# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def traverse(head):
            while head:
                yield head
                head = head.next
        
        visited = set()
        if head == None:
            return False

        for i, node in enumerate(traverse(head)):
            if node in visited:
                return True
            visited.add(node)
        return False

        