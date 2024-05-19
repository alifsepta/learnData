class Solution(object):
    def countStudents(self, students, sandwiches):
        # Initialize counters for circular and square sandwiches
        circular_count = students.count(0)
        square_count = students.count(1)
        
        # Iterate through the sandwiches
        for sandwich in sandwiches:
            # If the sandwich type matches the preference of the student at the front of the queue
            if sandwich == 0:
                if circular_count > 0:
                    # If there are circular sandwiches available, a student takes one
                    circular_count -= 1
                else:
                    # If there are no circular sandwiches available, return the remaining students who couldn't eat
                    return square_count
            else:
                if square_count > 0:
                    # If there are square sandwiches available, a student takes one
                    square_count -= 1
                else:
                    # If there are no square sandwiches available, return the remaining students who couldn't eat
                    return circular_count
        
        # If all students have taken a sandwich, return 0
        return 0

# Test cases
solution = Solution()
students1 = [1,1,0,0]
sandwiches1 = [0,1,0,1]
print(solution.countStudents(students1, sandwiches1))  # Output: 0

students2 = [1,1,1,0,0,1]
sandwiches2 = [1,0,0,0,1,1]
print(solution.countStudents(students2, sandwiches2))  # Output: 3
