# Solution1 : 재귀 구조로 연결 -> 복습 필요(https://www.youtube.com/watch?v=_MZbRhMgtls)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
