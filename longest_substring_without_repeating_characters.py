"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        # char => last known index in string
        char_cache: dict[str, int] = {}
        
        for char in s:
            print(char_cache)
            cached = char_cache.get(char)
            
            if cached is not None:
                if cached >= start:
                    start = cached + 1
            
            char_cache[char] = end
            longest = max(longest, end - start + 1)
            end += 1
        
        return longest


_s = "abcabcbb"
solution = Solution()

print(solution.lengthOfLongestSubstring(_s))