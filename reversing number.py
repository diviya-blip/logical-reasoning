# Get input from the user
num = int(input("Enter a number: "))

# Store the original number (optional)
original = num

# Convert to positive if negative
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Display the reversed number
print("Reversed number =", reverse)