
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
    
        return dummy.next

# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Remove the 2nd node from the end
result_head = Solution().removeNthFromEnd(head, 2)

# Print the result linked list
while result_head:
    print(result_head.val, end=" ")
    result_head = result_head.next
