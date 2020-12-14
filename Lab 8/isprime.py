def is_prime(number):
    prime = True
    for i in range(2, number//2+1):
        if number % i == 0:
            prime = False
    
    return prime

def print_primes_between(a, b):
  for i in range(a,b):
    if is_prime(i):
      print(i)