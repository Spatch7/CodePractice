
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        if list2:
            node.next = list2
            
        return dummy.next
    




if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    sol = Solution()
    merged_list = sol.mergeTwoLists(list1, list2)