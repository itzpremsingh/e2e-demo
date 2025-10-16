from random import randint


# Simple function to check prime (not efficient, just for demo)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Generate a random prime in range
def generate_prime(start, end):
    while True:
        p = randint(start, end)
        if is_prime(p):
            return p


def generate_keys() -> tuple[int, int, int | None]:
    # 1. Choose two primes
    p = generate_prime(100, 300)
    q = generate_prime(100, 300)
    n = p * q
    phi = (p - 1) * (q - 1)

    # 2. Choose e
    e = 3
    while phi % e == 0:
        e += 2

    # 3. Compute d (modular inverse of e mod phi)
    def mod_inverse(e, phi) -> int | None:
        for d in range(2, phi):
            if (d * e) % phi == 1:
                return d
        return None

    d = mod_inverse(e, phi)

    return (n, e, d)
