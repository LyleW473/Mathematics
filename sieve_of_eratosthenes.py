from time import time

def sieve_of_eratosthenes(n):

    start_time = time()
    # Create a list of numbers from 2 to n
    numbers = [num for num in range(2, n)]

    for i in range(2, int((n ** 0.5) + 1)):
        # If the number is an integer (meaning that it isn't a composite number, otherwise it would be a Boolean value)
        if type(numbers[i - 2]) == int:

            # For numbers i till n, mark all multiples of i as False
            for x in range(i, n, i):

                # If x is any multiple of i, but not i (e.g. 48 would be a multiple of 7, but do not set 7 as False)
                if x != i: 

                    # Set the multiple as False
                    numbers[x - 2] = False

    # Convert the list into a set to get rid of all False statements except one
    numbers = list(set(numbers)) # Convert the set back to a list
    numbers.remove(False) # Remove the last False statement

    #print(sorted(numbers)) # Print the prime numbers list

    print(sorted(numbers)[-1]) # Print the last prime number from 2 to n

    end_time = time()

    return end_time - start_time

time_taken = sieve_of_eratosthenes(1000000)

print(time_taken)