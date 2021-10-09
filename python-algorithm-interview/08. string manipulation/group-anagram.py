# Solution1 : 정렬하여 딕셔너리에 추가

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())
