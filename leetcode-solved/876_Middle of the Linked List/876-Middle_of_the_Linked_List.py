class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        # Initialize two pointers, slow and fast, both pointing to the head of the linked list.
        slow = fast = head
        
        # Traverse the linked list. Move slow one step at a time and fast two steps at a time.
        # When fast reaches the end of the list (fast.next is None), slow will be at the middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Return the node where slow is pointing, which is the middle node.
        return slow

# Function to print the elements of the linked list starting from a given node.
def printLinkedList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Test cases
if __name__ == "__main__":
    # Example 1
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    print("Example 1 Output:")
    result1 = Solution().middleNode(head1)
    printLinkedList(result1)  # Output should be 3 4 5

    # Example 2
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    head2.next.next.next.next.next = ListNode(6)
    print("Example 2 Output:")
    result2 = Solution().middleNode(head2)
    printLinkedList(result2)  # Output should be 4 5 6
