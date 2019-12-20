def isprime(n):
    if n <= 1:
        # if the number is (<= )and the return is false print (else) is not prime
        return False
    for x in range(2, n):
        # if the number is (% and == 0 )and the return is false print (else) is not prime
        if n % x == 0:
            return False
    else:
        # if the value is not in the above both conditions the nit is TRUE print (if) is prime
        return True


def List_primes():
    for n in range(1000):
        if isprime(n):
            # end= ' ' prints along (vertically) andthe flush to flush the memory once done
            print(n, end=' ', flush=True)
    print()  # Prints a new line


List_primes()
