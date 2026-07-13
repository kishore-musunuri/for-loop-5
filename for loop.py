

# 1. Print each number and its square
print("1. Number and its Square")

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print("Number:", num, "Square:", num ** 2)

print("\n-------------------------")

# 2. Print each character with its index
print("2. Character with Index")

def print_characters(text):
    for index in range(len(text)):
        print("Index:", index, "Character:", text[index])

print_characters("Python")

print("\n-------------------------")

# 3. Sum of all even numbers in a list
print("3. Sum of Even Numbers")

numbers = [10, 15, 20, 25, 30, 35, 40]

total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of Even Numbers:", total)

print("\n-------------------------")

# 4. Print Dictionary Key-Value Pairs
print("4. Dictionary Key-Value Pairs")

student = {
    "Name": "Kishore",
    "Age": 20,
    "Course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

print("\n-------------------------")

# 5. Generate numbers from 1 to 100 and print numbers divisible by 3 or 5
print("5. Numbers Divisible by 3 or 5")

numbers = []

# Generate list
for i in range(1, 101):
    numbers.append(i)

# Print numbers divisible by 3 or 5
for num in numbers:
    if num % 3 == 0 or num % 5 == 0:
        print(num, end=" ")

print()
