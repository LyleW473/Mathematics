""" Uses prime factorisation to find the number of divisors of a given number"""

def count_divisors(prime_factors_list):
    """     
        The prime factorisation of n is given by:
        n = p1^a1 x p2^a2 x ... x pk^ak
    
        The number of divisors of a number is given by:

        d = (a1 + 1) x (a2 + 1) x .... x (ak + 1)
    """


    # Find the number of different numbers
    unique_num_set = set(prime_factors_list) # Convert to a set to get rid of duplicate values
    num_of_unique_nums = len(unique_num_set) # Find the length of the set, giving the amount of unique numbers

    # Find the exponents of each number

    # Create a new list with the number, 
    new_list = [[list(unique_num_set)[i], 0] for i in range(0, num_of_unique_nums)]

    # For each number in the prime factors list
    for number in prime_factors_list:

        # For each pair in the new list
        for pair in new_list:

            # If the number in the prime factors list is the same as the number in the prime factors list
            if number == pair[0]:

                # Increase the quantity
                pair[1] += 1

    # Finding the number of factors of the given number
    divisors = 1
    for i in range(0, len(new_list)):
        # Find the number of factors of the number by using the second equation in the commented section
        divisors *= (new_list[i][1] + 1)

    return divisors