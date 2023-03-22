class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def naive(head):
        prev = None
        while head:
            detach_remain = head.next
            head.next = prev
            prev = head
            head = detach_remain
        return prev

if __name__ == "__main__":
    inputs = [
        ListNode(val=1,
            next=ListNode(val=2,
            next=ListNode(val=3, 
            next=ListNode(val=4, 
            next=ListNode(val=5))))),
        ListNode(val=1,
            next=ListNode(val=2))
    ]
    for head in inputs:
        print(Solution.naive(head))