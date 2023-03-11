"""
there is capacity empty seats
only drives east
given array trips
trips[i] = numPassengers, from, to
ith trip has numPassengers and the locations to pick up and drop off are from, to

numbers = # of km due east from initial location
return true if possible to pick up and drop off all passengers for all given trips

i already know we may have to keep people in the car for multiple stops

trips = [[2, 1, 5], [3, 3, 7]], capacity = 4

so the first stop is 1 mile away
we pick up 2 people

we hit mile 3, and we don't have capacity, so false

trips = [[2, 1, 5], [3, 3, 7]], capacity = 5
hit mile 1, pick up 2
hit mile 3, pick up 3,
drop off at mile 5
drop off at mile 7
true

1 <= trip length <= 1000
1 <= passengers <= 100
0 <= from, to <= 1000
1 <= capacity <= 10^5

if capacity < numPassengers, return false

iterate through list, and create a new array based on drop of and pick up
add (pickUpLocation, +numPassengers), add (dropOffLocation, -numPassengers)
sort
iterate through sorted list and change capacity
if capacity < 0, return false


[(1, -2), (3, -3), (5, +2) (7, +3)]

capacity =
O n log n + O n sp[ace]

----

[[2, 1, 5], [3, 5, 7]]

[(1, -2), (5, -3), (5, 2), (7, 3)]
             i

capacity = -2
nextLocation = (5)

"""

trips = [[2,1,5],[3,3,7]]

[(from, numPassangeers), (to, -numPassengers)]

allTrips = [(1, 2), (5, -2), (3, 3), (7, -3)]
allTrips.sorted() = [(1, -2), (3, -3), (5, 2),(7, 3)]
capacity = 5


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        carpoolSchedule = []
        # iterate through list, and create a new array based on drop of and pick up
        # add (pickUpLocation, +numPassengers), add (dropOffLocation, -numPassengers)
        for numPassengers, pickUpLocation, dropOffLocation in trips:
            carpoolSchedule.append((pickUpLocation, -numPassengers))
            carpoolSchedule.append((dropOffLocation, numPassengers))

        # sort
        carpoolSchedule.sort()

        # iterate through sorted list and change capacity
        # if capacity < 0, return false
        index = 0
        while index < len(carpoolSchedule):
            currentLocation, numPassengers = carpoolSchedule[index]
            capacity += numPassengers

            if index < len(carpoolSchedule) - 1:
                nextLocation, numPassengers = carpoolSchedule[index + 1]

                if nextLocation > currentLocation and capacity < 0:
                    return False

            index += 1

        return True

solution = Solution()
print(f"Expected: false, Actual: {solution.carPooling([[2,1,5],[3,3,7]], 4)}")
print(f"Expected: true, Actual: {solution.firstUniqChar([[2,1,5],[3,3,7]], 5)}")
