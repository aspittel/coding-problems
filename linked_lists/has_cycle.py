"""
Check to see if linked list has a cycle in it.

From: https://www.hackerrank.com/challenges/ctci-linked-list-cycle
"""
def has_cycle(head):
    fast = slow = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
