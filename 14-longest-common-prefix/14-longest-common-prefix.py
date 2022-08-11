class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        sorted_array = sorted(strs)
        smallest_str = len(min(strs, key=len))
        for i in range(smallest_str):
            if sorted_array[0][i] == sorted_array[-1][i]:
                common_prefix += sorted_array[0][i]
            else:
                break
        return common_prefix

            
            