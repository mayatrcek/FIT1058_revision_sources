from sympy import isprime
from fractions import Fraction

"""
This file calculates the euler totient and explains 
the steps for nubs like me.

Defined as the number of positive integers <= n 
that are coprime to n is denoted by phi(n)
"""

def phi(n):
    # If n is a prime:
    if isprime(n):

        print("Input is prime.")
        output = n - 1

        return output
    
    else:
        print("P is not prime. Calculating p...")
    
        # Step 1: break n down into its prime factors. -- AI generated below this line of code
        factors = prime_factorisation(n)
        primes = list(factors.keys())
        breakdown = " * ".join(f"{p}^{e}" for p, e in factors.items())
        print(f"  Step 1 - factorise: {n} = {breakdown}")
        print(f"  Step 2 - distinct primes: {primes}")
 
        # Step 3: apply phi(n) = n * product of (1 - 1/p) over distinct primes.
        formula = f"{n}" + "".join(f" * (1 - 1/{p})" for p in primes)
        print(f"  Step 3 - formula: phi({n}) = {formula}")
 
        # Step 4: multiply it out, showing the running value at each prime.
        running = Fraction(n)
        for p in primes:
            before = running
            running *= Fraction(p - 1, p)   # (1 - 1/p) = (p-1)/p, kept exact
            print(f"           {before}  * (1 - 1/{p})  =  {running}")
 
        output = int(running)               # the totient is always a whole number
        print(f"  Result: phi({n}) = {output}")
        return output
 
def prime_factorisation(n):
    """Break n down into primes by trial division.
 
    Returns a dict {prime: exponent}, e.g. 120 -> {2: 3, 3: 1, 5: 1}.
    """
    factors = {}
    remaining = n
    d = 2
    while d * d <= remaining:        # only need to test up to sqrt(remaining)
        while remaining % d == 0:    # pull out every copy of this prime
            factors[d] = factors.get(d, 0) + 1
            remaining //= d
        d += 1
    if remaining > 1:                # whatever is left is a prime factor too
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors

if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    print("=== phi({n}) ===")
    phi(n)