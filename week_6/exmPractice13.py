nums = [3, 8, 12, 7, 5, 10]


def analyze(num): 
    even_sum = 0
    odd_count = 0
    for n in num: 
        if n%2 == 0: 
            even_sum += n
        else: 
            odd_count += 1
    return(even_sum,odd_count)
print(analyze(nums))
