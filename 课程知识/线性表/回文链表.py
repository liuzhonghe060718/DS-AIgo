class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return self.val
hea=ListNode(1)
hea.next=ListNode(2)
hea.next.next=ListNode(2)
hea.next.next.next=ListNode(1)
def isPalindrome(head) -> bool:
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    start = slow.next
    slow.next = None
    pre = None
    cur = start
    while cur:
        nxt = cur.next
        cur.next = pre
        pre, cur = cur, nxt
    l1, l2 = head, pre
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True
print(isPalindrome(hea))