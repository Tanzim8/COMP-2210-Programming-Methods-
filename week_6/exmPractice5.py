numbers = [12, 7, 18, 5, 20, 9]

def analyze_numbers(numbers):
    even_sum = 0
    odd_count = 0
    largerst = numbers[0]
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        elif num % 2 != 0:
            odd_count = odd_count + 1
        if num > largerst:
            largerst = num
    return even_sum, odd_count, largerst
print(analyze_numbers(numbers))