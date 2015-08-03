def genPrimes():
    last = 1
    primes = []
    while True:
        last += 1
        if not any(last % p == 0 for p in primes):
            primes.append(last)
            yield last
