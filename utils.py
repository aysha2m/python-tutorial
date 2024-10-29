def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > max:
            maximum = number
    return maximum