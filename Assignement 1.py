num = int(input("Enter a number: "))

sum = 0

t = num # Temporary variable to store the original number

# Loop to calculate the sum of the cubes of the digits
while t > 0:
    digit = t % 10
    sum += digit ** 3
    t //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")