class Solution(object):
    def largestAltitude(self, gain):
        altitude = [0]  # Start at altitude 0
        for g in gain:
            # Calculate the next altitude by adding the gain to the previous altitude
            altitude.append(altitude[-1] + g)
        # Return the maximum altitude reached during the trip
        return max(altitude)

solution = Solution()
print(solution.largestAltitude([-5,1,5,0,-7]))
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))
