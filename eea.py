# EEA --> gcd(m,n) = xm + yn.
def eea(m, n):

    # First ensure m >= n.
    if m < n:
        m, n = n, m

    # Initialise the triples:
    a, x, y = m, 1, 0
    b, z, w = n, 0, 1

    # Loop until b = 0.
    while b != 0:

        # Compute the quotient.
        q = a // b

        # Update the triples:

        new_a, new_x, new_y = b, z, w

        # (a, x, y) - q * (b, z, w)
        new_b, new_z, new_w = a - q * b, x - q * z, y - q * w

        a, x, y = new_a, new_x, new_y
        b, z, w = new_b, new_z, new_w

    # Output
    print("\ngcd(m, n) = a")
    print(f"gcd({m}, {n}) = {a}")
    print("\nUsing the invariants, x, y, z, and w. we can also calculate...")
    print(f"gcd({m}, {n}) = {x}*{m} + {y}*{n} = {a} --> Verified to be {a == x*m + y*n}\n")
    print(f"COPRIMALITY (when gcd = 1)\nIs {m}, {n} coprime? {a == 1}\n")

    return 

m = int(input("\nEnter m: "))
n = int(input("Enter n: "))

gcd = eea(m, n)