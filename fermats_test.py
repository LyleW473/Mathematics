from time import time
"""
a^p - a

a : 1 <= a < p 

if p is prime, a^p - a  will be a multiple of p 
"""

def fermats_test(n):

    start_time = time()
    prime_list = []
    for p in range(2, n):
        # Set the flag to True until proven False
        is_prime = True
        for a in range(1, p):
            # if a^p - a is not divisible by p, then it is not a prime number
            if int( (a ** p) - a )  % p != 0:
                # Set the flag that it is prime to False and end the current iteration
                is_prime = False
                break
        # If the value of p is prime, then add it to the list
        if is_prime == True:
            prime_list.append(p)

    end_time = time()
    print(prime_list)
    print(f"Time taken : {end_time - start_time}")


fermats_test(1000)