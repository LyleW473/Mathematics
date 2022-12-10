def find_prime_factors(number):
    prime_number = 2 # The smallest prime number is 2
    factors = []

    # 1 is not regarded as a prime number, so just return the number
    if number <= 1:
        return number

    # While the prime number squared is less than or equal to the number we want to find the number of prime factors for
    while prime_number ** 2 <= number:

        # If the number is divisible by the prime number 
        if number % prime_number == 0:
            
            # Append the prime number to the factors list
            factors.append(prime_number)
            # Set the number to be the number divided by the prime number e.g. (60 // 2 = 30)
            number //= prime_number

        # If the number is not divisible by the prime number
        else:
            # Increment the number
            prime_number += 1

        print(number, prime_number)

    # Number would be the final divisor 
    factors.append(number)

    # Return the factors
    return factors


print(find_prime_factors(10000))
    