
num = int(input("Enter a number: "))

# Convert to positive if negative
num = abs(num)

# Calculate the sum of digits
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

# Display the result
print("Sum of digits =", sum_digits)