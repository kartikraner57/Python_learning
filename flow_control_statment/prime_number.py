######## Wap to cheack whether the given number is prime number (or)not

# n = int(input('Enter any number: '))  # Take input from the user



n = int(input('Enter any number: '))  # Take input from the user

if n <= 1:
    print(n, 'is not a prime number')  # Numbers <=1 are not prime
else:
    is_prime = True  # Assume the number is prime
    for i in range(2,n//2+1): # Iterate from 2 to n//2
        if n % i == 0:  # Check if the number is divisible by i
            is_prime = False
            break  # Exit loop if a factor is found
    
    if is_prime:
        print(n, 'is a prime number')  # If no factors found, it's prime
    else:
        print(n, 'is not a prime number')  # Otherwise, it's not prime
