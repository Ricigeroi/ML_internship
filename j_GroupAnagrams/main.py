class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string in dict:
                dict[sorted_string].append(string)
            else:
                dict[sorted_string] = [string]

        return list(dict.values())