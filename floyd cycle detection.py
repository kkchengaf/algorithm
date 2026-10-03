


def floyd_cycle(head):
    fast,slow = head,head
    while fast != slow and fast is not None:
        slow = slow.next
        fast = fast.next
        if fast is not None: fast = fast.next

    # fast == slow, cycle exist
    if fast is not None:
        n = 0
        while True:
            fast = fast.next
            n += 1
            if fast == slow: break

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast,n
    return None,0
