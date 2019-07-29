def binary_array_to_number(arr):
    number = 0
    for index in range(len(arr)):
        last = -(index + 1)
        number += arr[last] * (2 ** index)
    return number


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 1]))
print(binary_array_to_number([0, 1, 0, 1]))
print(binary_array_to_number([1, 0, 0, 1]))
