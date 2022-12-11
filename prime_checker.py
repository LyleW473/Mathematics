def prime_test(number):
    """
    Factors of 100:
    1 x 100
    2 x 50
    4 x 25
    5 x 20
    10 x 10 Loop to sqrt(n) + 1
    20 x 5 
    25 x 4
    50 x 2
    100 x 1
    """
    count = 0
    # If the number is less than 2, it is not prime i.e. 1, 0 or negative numbers
    if number < 2:
        return False

    # If the number is 2, it is a prime number
    if number == 2:
        return True
    
    # Loop from numbers 2 till the square root of the number + 1, this is because we can find all the factors of a given number n by only looping up to sqrt(n) (The + 1 is so that it includes sqrt(n))
    for i in range(2, int(number ** 0.5) + 1):
        # If the number is divisible by i, it means that i is a factor of number, so increment the counter
        if number % i == 0:
            count += 1
            # If the counter is greater than 0, it means that it is has a factor other than 1 and itself
            if count > 0:
                # Return False
                return False

    # Otherwise return True
    return True