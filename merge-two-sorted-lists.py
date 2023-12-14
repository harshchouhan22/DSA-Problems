class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        return dummy.next

# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)


while merged_list is not None:
    print(merged_list.val, end=' ')
    merged_list = merged_list.next
