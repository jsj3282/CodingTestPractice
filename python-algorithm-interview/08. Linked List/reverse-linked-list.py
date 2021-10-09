# Solution1 : 재귀 구조로 뒤집기 -> 복습 필요(https://www.youtube.com/watch?v=GkCnbndXBUs)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)


# Solution2 : 반복 구조로 뒤집기 -> 복습 필요

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
