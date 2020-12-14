def is_prime(number):
    prime = True
    for i in range(2, number//2+1):
        if number % i == 0:
            prime = False
    
    return prime

print(is_prime(11))
