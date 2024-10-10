import random

# Dictionary to hold counts of each character
counts = {
    'a': 0,
    'b': 0,
    'c': 0,
    'x': 0,
    '2': 0,
    '7': 0,
    '9': 0,
}

total = 0

# Array (you can change the size too if you want)
arr = [['' for _ in range(100)] for _ in range(100)]

# Random number generator
rand_num = random.Random()

# Map numbers to characters
char_map = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: '7',
    4: '9',
    5: 'x',
    6: '2'
}

# Populate the array with characters using random numbers
for row in range(len(arr)):
    for col in range(len(arr[row])):
        # Generate a random number from 0 to 6
        x = rand_num.randint(0, 6)

        # Assign character based on the random number
        char = char_map[x]
        arr[row][col] = char

        # Increment the count of the character
        counts[char] += 1
        total += 1

# # Print the array
# for row in arr:
#     print(' '.join(row))

# Print counts
print("\nCharacter counts:")
for char, count in counts.items():
    print(f"{char} count is {count}")

# Find the character with the highest count
max_char = max(counts, key=counts.get)
max_count = counts[max_char]

# Check if multiple characters have the highest count
if list(counts.values()).count(max_count) > 1:
    print("Multiple high amounts present!")
else:
    print(f"{max_char.upper()} has the highest count")
print(f"The total number is {total}")
