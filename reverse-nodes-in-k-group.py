class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        #This function is used to reverse the linked list
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr !=  end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev, start, end
        
        #this func is used to get the length of the linked list nodes
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        length = get_length(head)
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next
            next_group_start = group_end.next
            

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
solution = Solution()
result = solution.reverseKGroup(head, k)

# Print the result
while result:
    print(result.val, end=' ')
    result = result.next
