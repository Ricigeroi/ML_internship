class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0
            freq[s[right]] += 1

            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
