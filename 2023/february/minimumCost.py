"""

array sticks with sticks[i] = length of stick
you can connect any two sticks into a long stick by paying a cost of x + y
you must connect all sticks until only one stick remaining
return minimum cost when connecting sticks

sticks = [2, 4, 3]
[6, 3], 6
[9], 9

[1, 8, 3, 5]9, 11, 13
[13, 1, 3, 5] 14, 16, 18
[18, 1, 3]19, 21
[21, 1]22

min > 30

greedy solution
if, at each step you choose the minimum, the overall will be the minimum

how do we organize so that we always have the minimum?
can't keep in an array because then you're always removing, which is an O(N) operation
you can create a min heap

iterate through all numberes and create a min heap
[1, 3, 5, 8]

[2, 3, 4]
while sticks in heap > 2
pop twice, add together, then push new into heap
pop heap and return num

creating the heap is O(N) in Python
iterating through the heap again and doing a pop + push operation is O log N


[1, 3, 5, 8]
       i
    cost = 4

"""
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        print(sticks)

        heapq.heapify(sticks)
        cost = 0

        while len(sticks) > 1:
            first_stick = heapq.heappop(sticks)
            second_stick = heapq.heappop(sticks)
            heapq.heappush(sticks, first_stick + second_stick)
            cost += first_stick + second_stick

        return cost

solution = Solution()
print(f"Expected: 14, Actual: {solution.connectSticks([2,4,3])}")
print(f"Expected: 30, Actual: {solution.connectSticks([1,8,3,5])}")
print(f"Expected: 0, Actual: {solution.connectSticks([5])}")
