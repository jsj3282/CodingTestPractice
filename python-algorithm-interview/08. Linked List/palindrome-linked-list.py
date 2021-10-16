# Solution1 : 리스트 변환

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []
        
        if not head:
            return True
        
        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True
   
 
# Solution2 : 데크를 이용한 최적화

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()
            
        if not head:
            return True
        
        node = head
        
        if node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True


# Solution3 : 런너를 이용한 우아한 풀이 -> 복습 필요(https://velog.io/@jayb/LeetCode-234.Palindrome-Linked-List%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = None
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 홀수 일때
        if fast:
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
