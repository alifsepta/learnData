class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        # Initialize the result variable to store the decimal value
        result = 0
        
        # Traverse the linked list until the end
        while head:
            # Shift the current result to the left by 1 bit
            result = (result << 1) + head.val
            # Move to the next node in the linked list
            head = head.next
        
        # Return the final decimal value
        return result

# Test cases
# Example 1
head1 = ListNode(1)
head1.next = ListNode(0)
head1.next.next = ListNode(1)

# Example 2
head2 = ListNode(0)

sol = Solution()
print(sol.getDecimalValue(head1))  # Output: 5
print(sol.getDecimalValue(head2))  # Output: 0
