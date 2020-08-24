from itertools import permutations

def solution(numbers):
    primary = set()
    for i in range(1,len(numbers)+1):
        nums = set(map(lambda x : int(''.join(x)), permutations(numbers,i))) 
        for num in nums:
            if is_primary(num): primary.add(num)
    return len(primary)

def is_primary(number):
    if number <= 1: return False
    for i in range(2,number):
        if number % i == 0 : return False
    return True