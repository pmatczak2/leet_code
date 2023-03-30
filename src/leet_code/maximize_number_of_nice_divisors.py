# You are given a positive integer primeFactors. You are asked to construct a positive integer n that satisfies the
# following conditions:
#
# The number of prime factors of n (not necessarily distinct) is at most primeFactors. The number of nice divisors of
# n is maximized. Note that a divisor of n is nice if it is divisible by every prime factor of n. For example,
# if n = 12, then its prime factors are [2,2,3], then 6 and 12 are nice divisors, while 3 and 4 are not. Return the
# number of nice divisors of n. Since that number can be too large, return it modulo 109 + 7.
#
# Note that a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
# The prime factors of a number n is a list of prime numbers such that their product equals n.

# Example 1:
#
# Input: primeFactors = 5
# Output: 6
# Explanation: 200 is a valid value of n.
# It has 5 prime factors: [2,2,2,5,5], and it has 6 nice divisors: [10,20,40,50,100,200].
# There is not other value of n that has at most 5 prime factors and more nice divisors.

# Example 2:
#
# Input: primeFactors = 8
# Output: 18


def max_nice_divisors(primeFactors):
    mod = 10 ** 9 + 7
    if primeFactors < 4:
        return primeFactors
    if primeFactors % 3 == 0:
        return pow(3, primeFactors // 3, mod) % mod
    if primeFactors % 3 == 1:
        return 4 * pow(3, primeFactors // 3 - 1, mod) % mod
    return 2 * pow(3, primeFactors // 3, mod) % mod
print(max_nice_divisors(73))

# line 26: max_nice_divisors and it takes an integer primeFactors as input and returns an integer as output. line 27:
# This line sets the value of mod to be 1 billion plus 7. This number is used later in the function to take the
# modulus of large numbers and prevent overflow.

# line 28,29: If the input primeFactors is less than 4, the function
# simply returns primeFactors. This is because the maximum number of nice divisors for any number less than 4 is the
# number itself.

# Line 30,31: If primeFactors is divisible by 3, then the function returns the result of raising 3 to
# the power of primeFactors divided by 3, modulo mod. This is because the maximum number of nice divisors for any
# number that is divisible by 3 is 3 raised to the power of primeFactors divided by 3.

# line 32,33: If primeFactors is
# not divisible by 3 and leaves a remainder of 1 when divided by 3, then the function returns the result of
# multiplying 4 by 3 raised to the power of primeFactors divided by 3 minus 1, modulo mod. This is because the
# maximum number of nice divisors for any number that leaves a remainder of 1 when divided by 3 is 4 multiplied by 3
# raised to the power of primeFactors divided by 3 minus 1.
#
# line 34: If primeFactors is not divisible by 3 and leaves
# a remainder of 2 when divided by 3, then the function returns the result of multiplying 2 by 3 raised to the power
# of primeFactors divided by 3, modulo mod. This is because the maximum number of nice divisors for any number that
# leaves a remainder of 2 when divided by 3 is 2 multiplied by 3 raised to the power of primeFactors divided by 3
