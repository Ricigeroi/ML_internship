class Solution:
    def count_substrings(self, string: str) -> int:
        def count_palindromes_around_center(left, right):
            count = 0
            while left >= 0 and right < len(string) and string[left] == string[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0
        for i in range(len(string)):
            total_palindromes += count_palindromes_around_center(i, i)

            total_palindromes += count_palindromes_around_center(i, i + 1)

        return total_palindromes
