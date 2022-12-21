from time import time

def sieve(n):
    start_time = time()
    sieve = [True] * n
    prime_list = []

    # Check for prime from numbers 2 to input number
    for p in range(2, n):
        # If the item is set to True
        if sieve[p]: 
            # Add it to the prime list
            prime_list.append(p)

            # Starting from p^2, mark all multiples of p as False (as they are composite numbers)
            for i in range(p**2, n, p): 
                sieve[i] = False

    end_time = time()
    # Return a list of primes
    return prime_list, end_time - start_time

prime_list, time_taken = sieve(100)
print(f"Time taken: {time_taken}")
print(f"Prime list: {prime_list}")