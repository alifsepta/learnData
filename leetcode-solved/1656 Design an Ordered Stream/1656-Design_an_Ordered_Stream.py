class OrderedStream(object):
    def __init__(self, n): 
        #Create a list to store the stream of values with size n.
        #Initially, all values are set to None
        self.stream = [None] * n
        self.ptr = 0

def insert(self, idKey, value):
    # insert the value at the specified ID position in the stream
    self.stream[idKey - 1] = value
    # List to store the chunk of currently inserted values
    result = []
    # Loop to find the next chunk of inserted values
    while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
        # Append the value tothe result chunk
        result.append(self.stream[self.ptr])
        # Move the pointer to the next position
        self.ptr += 1
    # Return the chunk of currently inserted values.
    return result