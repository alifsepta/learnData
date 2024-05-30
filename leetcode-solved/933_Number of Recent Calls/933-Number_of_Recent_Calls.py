class RecentCounter(object):
    def __init__(self):
        self.requests = []  # Initialize an empty list to store the timestamps of recent requests

    def ping(self, t):
        self.requests.append(t)  # Add the timestamp of the new request to the list
        
        # Remove requests that are outside the time frame of 3000 milliseconds
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        
        # Return the number of requests within the time frame
        return len(self.requests)

# Initialize the RecentCounter object
recentCounter = RecentCounter()

# Perform ping operations as described in the example
print(recentCounter.ping(1))    # Output: 1
print(recentCounter.ping(100))  # Output: 2
print(recentCounter.ping(3001)) # Output: 3
print(recentCounter.ping(3002)) # Output: 3
