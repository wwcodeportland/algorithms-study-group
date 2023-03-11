"""
iterate through each char
i need two pieces of data: the location and the count

minPosition = 0

charToCount = {
    l: 0
    e: -7
    t: 3
    c: 4
    o: 5
    d: 6
}

"""

from collections import defaultdict
import math

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charToIndex = {}
        minIndex = math.inf

        for c in range(len(s)):
            if s[c] in charToIndex:
                charToIndex[s[c]] = -c

            else:
                charToIndex[s[c]] = c

        for key, index in charToIndex.items():
            if charToIndex[key] >= 0:
                minIndex = min(charToIndex[key], minIndex)

        return minIndex if minIndex != math.inf else -1


solution = Solution()
print(f"Expected: 0, Actual: {solution.firstUniqChar('leetcode')}")
print(f"Expected: 2, Actual: {solution.firstUniqChar('loveleetcode')}")
print(f"Expected: -1, Actual: {solution.firstUniqChar('aabb')}")
