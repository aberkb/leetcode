#Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#https://leetcode.com/problems/merge-two-sorted-lists/
#Definition for singly-linked list.

#first recurrentsive solution:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)

        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            return "no input given!"

        if l1.val < l2.val:
            temp.next = l1
            temp.next.next = self.mergeTwoLists(l1.next, l2)
        else:
            temp.next = l2
            temp.next.next = self.mergeTwoLists(l1, l2.next)
        return temp.next

#Runtime: 40 ms, faster than 40.83% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14.3 MB, less than 27.65% of Python3 online submissions for Merge Two Sorted Lists.


#iterative solution

#Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        current = temp

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return temp.next


#Runtime: 40 ms, faster than 40.83% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14.3 MB, less than 11.74% of Python3 online submissions for Merge Two Sorted Lists.
