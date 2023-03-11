from collections import defaultdict

"""
abcxb
  s
    e

charToCount = {
    a: 0,
    b: 1,
    c: 1,
    x: b,

}


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charToCount = defaultdict(int)
        longestSubstring = 0

        for end in range(len(s)):
            charToCount[s[end]] += 1

            while charToCount[s[end]] > 1:
                charToCount[s[start]] -= 1
                start += 1

            longestSubstring = max(longestSubstring, end - start + 1)

        return longestSubstring

solution = Solution()
print(f"Expected: 3, Actual: {solution.lengthOfLongestSubstring('abcabcbb')}")
print(f"Expected: 1, Actual: {solution.lengthOfLongestSubstring('bbbbb')}")
print(f"Expected: 3, Actual: {solution.lengthOfLongestSubstring('pwwkew')}")
