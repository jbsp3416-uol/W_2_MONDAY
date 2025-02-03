def even_list(input_str)
    input_str = input('Enter numbers separated by commas:')
    number_str = input_str.split(',')
    numbers = [int(num.strip()) for num in number_str]
    even_num=[]
    for num in numbers:
    if num%2 == 0:
        even_num.append(num)
    return 'The even numbers are:', even_num

print(even_list(input_str))
