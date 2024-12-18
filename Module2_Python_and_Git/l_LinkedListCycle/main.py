class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()

        while head:
            if head in nodes:
                return True
            else:
                nodes.add(head)
            head = head.next
        return False
