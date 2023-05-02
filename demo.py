## Exercise 1
def isPrime(n):
    if n<=1:
        return False;
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False;
    return True;

def nextPrime(n):
    if isPrime(n):
        n+=1
    while not isPrime(n):
        n+=1
    return n

## Exercise 2
def primeFact(p):
    factors = []
    d = 2
    while d*d <= p:
        while (p%d)==0:
            factors.append(d)
            p //=d
        d += 1
    if p>1:
        factors.append(p)
    return factors

def countFactors(factors):
    counts = {}
    for factor in factors:
        if factor in counts:
            counts[factor]+=1
        else:
            counts[factor]=1
    return [counts[factor] for factor in counts]

## Exercise 3
def printPrime(N):
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N, i):
                is_prime[j] = False
    for i in range(N):
        if is_prime[i]:
            print(i)
           
## Exercise 4
def get_primes(n):
    if n < 2:
        return []
    primes = [2]
    i = 3
    while i < n:
        is_prime = True
        j = 0
        while j < len(primes):
            if i % primes[j] == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            primes.append(i)
        i += 2
    return primes

## Exercise 5
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

## Exercise 6
def lcm(a, b):
    return (a * b) // gcd(a, b)

## Exercise 7
def base10tobase2(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n //= 2
    return result

print(base10tobase2(5))
print(base10tobase2(15))
print(base10tobase2(6))
print(base10tobase2(0))

## Exercise 8
def decimal_to_binary(n):
    binary = ''
    while n != 0:
        n *= 2
        if n >= 1:
            binary += '1'
            n -= 1
        else:
            binary += '0'
    return binary

## Exercise 9
def dec_to_hex(n):
    hex_digits = "0123456789ABCDEF"
    hex_num = ""
    while n > 0:
        rem = n % 16
        hex_num = hex_digits[rem] + hex_num
        n = n // 16
    return hex_num

## Exercise 10
def convertbase(a, base1, base2):
    # Convert the number to base 10
    num = 0
    for i in range(len(a)):
        num += a[i] * (base1 ** (len(a)-1-i))
    
    # Convert the number to base 2
    b = []
    while num > 0:
        b.insert(0, num % base2)
        num //= base2
    
    return b