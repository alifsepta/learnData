class Solution(object):  # Define a class named Solution
    def defangIPaddr(self, address):  # Define a method defangIPaddr with parameter address
        defanged_address = ""  # Initialize an empty string to store the defanged address
        for char in address:  # Iterate through each character in the input address
            if char == ".":  # If the character is a period
                defanged_address += "[.]"  # Replace it with "[.]" and append to the defanged_address string
            else:
                defanged_address += char  # Otherwise, just append the character as is
        return defanged_address  # Return the defanged address

# Test cases
solution = Solution()  # Instantiate the Solution class
address1 = "1.1.1.1"  # Input address
address2 = "255.100.50.0"  # Input address
print(solution.defangIPaddr(address1))  # Print the defanged version of address1
print(solution.defangIPaddr(address2))  # Print the defanged version of address2
