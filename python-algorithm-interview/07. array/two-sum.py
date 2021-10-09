# Solution1 : 브루트 포스로 계산

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution2 : in을 이용한 탐색

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
        
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]
 

# Solution3 : 첫 번째 수를 뺀 결과 키 조회

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]
 

# Solution4 : 조회 구조 개선

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target-num]]
            nums_map[num] = i
