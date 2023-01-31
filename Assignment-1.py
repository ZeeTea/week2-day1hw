#Cube Number Test... Print out all cubed numbers up to the total value 1000. 
#Meaning that if the cubed number is over 1000 break the loop.

n = 1
while n**3 < 1000:
    print(n**3)
    n += 1

#Get first prime numbers up to 100

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for num in range(2, 101):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)

#Take in a users input for their age,
# if they are younger than 18 print kids,
# if they're 18 to 65 print adults, else print seniors

age = int(input("How old are you? "))

if age < 18:
    print("Kid")
elif age >= 18 and age <= 65:
    print("Adult")
else:
    print("Senior")