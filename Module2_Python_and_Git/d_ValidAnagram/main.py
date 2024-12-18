class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False
