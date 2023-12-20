
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next =  next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

node = ListNode(1, ListNode(1, ListNode(3, ListNode(4))))
result = Solution().deleteDuplicates(node)
print(result)

