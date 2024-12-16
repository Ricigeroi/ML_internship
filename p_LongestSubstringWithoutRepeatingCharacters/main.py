class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}

        start = 0
        max_length = 0

        for end in range(len(s)):
            current_char = s[end]

            if current_char in char_index and char_index[current_char] >= start:
                start = char_index[current_char] + 1

            char_index[current_char] = end

            max_length = max(max_length, end - start + 1)

        return max_length