""" Johnson and Trotter algorithm
https://www.geeksforgeeks.org/johnson-trotter-algorithm/
"""

def johnson_and_trotter(lower_bound = 1, upper_bound = 4): # Default sequence is [1, 2, 3, 4]

    permutations_list = []
    # The sublists in the digits list represent: Number, Direction its facing, mobile or not
    digits = [ [i, "left", False] for i in range(lower_bound, upper_bound + 1)]

    # Add the first permutation to the permutations list
    first_permutation = ""
    for i in range(0, len(digits)):
        first_permutation += str(digits[i][0])
    permutations_list.append(first_permutation)

    while True:

        # Assume that it is completed until proven False
        completed = True
        # Check if there are no mobiles left and set them to mobile if they are
        for i in range(0, len(digits)):
            
            # If the index is 0 (The first item), and its pointing to the left, it cannot be mobile
            if i == 0 and digits[i][1] == "left":
                digits[i][2] = False

            # If the index is the last index, and the item is pointing right, it cannot be mobile
            elif i == len(digits) - 1 and digits[i][1] == "right":
                digits[i][2] = False

            # If the index is greater than 0, or if the index is 0 and the direction is "right"
            else:
                
                # If the directed integer is facing left
                if digits[i][1] == "left":
                    
                    # If the integer is greater than the integer that it is pointing to
                    if digits[i][0] > digits[i - 1][0]:
                        # Set the integer as mobile
                        digits[i][2] = True

                # If the directed integer is facing right
                elif digits[i][1] == "right":

                    # If the integer is greater than the integer that it is pointing to
                    if digits[i][0] > digits[i + 1][0]:
                        # Set the integer as mobile
                        digits[i][2] = True
                    
            # If any of the digits are still mobile 
            if digits[i][2] == True:
                # Set completed to False
                completed = False

        # This only occurs if all digits aren't mobile
        if completed == True:
            # Return the list of all the permutations 
            print("All permutations added!")
            return permutations_list

        # Find the largest mobile
        largest_mobile = -1
        for i in range(0, len(digits)):
            
            # If the number is mobile, and greater than the largest mobile we have found so far
            if (digits[i][0] > largest_mobile) and digits[i][2] == True :
                # Set the largest mobile as this digit
                largest_mobile = digits[i][0]
        
        i = 0
        # Find the largest mobile:
        while digits[i][0] != largest_mobile:
            # Increment the index
            i += 1

        # Choose the path based on its direction

        # If it is pointing left
        if digits[i][1] == "left":

            # If the integer is greater than the item it is pointing to
            if digits[i][0] > digits[i - 1][0]:
                # Swap the elements
                digits[i], digits[i - 1] = digits[i- 1], digits[i]
                
        # If it is pointing right
        elif digits[i][1] == "right":

            # If the integer is greater than the item it is pointing to
            if digits[i][0] > digits[i + 1][0]:
                # Swap the elements
                digits[i], digits[i + 1] = digits[i + 1], digits[i]
    
        # Create a string to hold the permutation
        permutation = ""
        # Iterate through the digits list
        for j in range(0, len(digits)):
            # Add the digit to the string
            permutation += str(digits[j][0])

            # Check if there are any values greater than the mobile integer value
            if digits[j][0] > largest_mobile:

                # Switch the directions based on where it was looking
                if digits[j][1] == "left":
                    digits[j][1] = "right"

                elif digits[j][1] == "right":
                    digits[j][1] = "left"

        # Add the permutation to the permutations list
        permutations_list.append(str(permutation))
        # Reset the string for the next iteration
        permutation = ""


print(johnson_and_trotter(0, 2))
print(johnson_and_trotter(1, 4))