numbers = [12, 7, 18, 25, 30, 9, 42, 15]

def calculate_even_average(numbers):
    even_num = 0
    even_num_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_num += number
            even_num_count+=1
    average = even_num/even_num_count
    return average
print(calculate_even_average(numbers))

def calculate_odd(numbers):
    odd_num_count = 0
    for number in numbers:
        if number % 2 != 0:
            odd_num_count+=1
    return odd_num_count
print(calculate_odd(numbers))