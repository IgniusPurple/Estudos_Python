def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd

print(check_numbers([1,2,4,6,5,7,11,20,35,37,29,33,28,12,18,16,75,6,2,63,4,3,39,33]))