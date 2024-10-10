arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [6, 7, 1, 2, 5],
    [6, 7, 8, 9, 0],
    [5, 4, 3, 2, 1]
]

for x in arr:
    for y in x:
        print(y, end=" ")
    print()

seven = 7
eight = 8
six = 6
twentyone = 21

count7 = 0
count8 = 0
count6 = 0
count21 = 0

for row in range(len(arr)):
    for col in range(len(arr[row])):
        if arr[row][col] == seven:
            count7 += 1
        elif arr[row][col] == eight:
            count8 += 1
        elif arr[row][col] == six:
            count6 += 1
        elif arr[row][col] == twentyone:
            count21 += 1

print()
print(f"The 7 value is: {count7}")
print(f"The 8 value is: {count8}")
print(f"The 6 value is: {count6}")
print(f"The 21 value is: {count21}")
