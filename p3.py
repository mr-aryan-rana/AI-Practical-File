# Print all prime numbers between 1 and 100
print("Name : Krishna \nRoll No : 1323215")

print("Prime numbers between 1 and 100 are:")

for num in range(2, 101):  # start from 2, since 1 is not prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # check divisibility up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
    
    if num == 41 :
        print("\n")
    
