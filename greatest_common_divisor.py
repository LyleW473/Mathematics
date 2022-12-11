""" GCD is found using Euclid's algorithm 
    The algorithm follows this expression: greater_number = (lower_number * q) + r
"""

def gcf_euclids_algo(number1, number2):
    # Set the remainder as a random value other than 0
    r = 1
    
    # Find the greatest and lowest numbers
    greater_number = max(number1, number2)
    lower_number = min(number1, number2)

    # While the remainder is not 0.
    # Note: When the remainder becomes 0, it means that we have find the greatest common divisor, which is the previous remainder
    while r != 0:
        
        # Find the largest number of times the lower number goes into the greater number
        q = greater_number // lower_number
        # Find the remainder from subtracting q from the greater number
        r = greater_number - (lower_number * q)

        print(f"{greater_number} = ({lower_number} x {q}) + {r}")

        # # Set the greater number as the value of the lower number. Set the lower number as the value of the remainder
        greater_number, lower_number = lower_number, r


    print(f"{greater_number} = ({lower_number} x {q}) + {r}")

    # The greater number would be the remainder of the last calculation before r was equal to 0. (Returns the previous remainder, which would be the greatest common divisor)
    return greater_number

print(f"The greatest common divisor is: {gcf_euclids_algo(number1 = 1701, number2 = 3768)}")