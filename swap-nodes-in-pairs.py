# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        #Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        #Point the next attribute of the dummy node to the actual head of the linked list
        dummy.next = head
        #Initialize a pointer to the dummy node for iteration and swapping
        current = dummy
        while current.next and current.next.next:
            #Nodes to be swapped
            first_node = current.next
            second_node = current.next.next
            #swapping 
            #Update the next pointer of the first node to skip the second node
            first_node.next = second_node.next
            #Update the next pointer of the second node to skip the first node
            second_node.next = first_node
            #Update the next pointer of the node before the swapped pair to point to the new head of the swapped pair
            current.next = second_node

            #Move to the next pair
            current = current.next.next
        return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = Solution().swapPairs(head)
# while result:    
#     print(result.val, end='')
#     result = result.next

