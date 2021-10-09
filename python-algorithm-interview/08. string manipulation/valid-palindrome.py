# Solution1 : 리스트로 변환

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True

# Solution2 : 데크 자료형을 위한 최적화

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
      
# 슬라이싱 사용

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자열 제거
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1] # 슬라이싱
