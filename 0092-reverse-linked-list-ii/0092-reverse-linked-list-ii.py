# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):

        dummy = ListNode(0)
        dummy.next = head
        lprev = dummy
        curr = head

        for i in range(left - 1):
            lprev = curr
            curr = curr.next

        prev = None

        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        lprev.next.next = curr
        lprev.next = prev
        return dummy.next