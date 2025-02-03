def max_number(numbers):
    max_value= numbers[0]
    for number in numbers:
        if number > max_value:
            max_value= number
    return max_value

print(max_number(numbers = [2,5,3,99,4,5,2,3]))
