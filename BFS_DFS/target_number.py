from itertools import combinations 

def solution(numbers, target):
    answer = 0
    mini = (-1)*sum(numbers)
    maxi = sum(numbers)
    if target == mini or target == maxi : return 1
    if target < mini or target > maxi : return 0 
    minus = maxi - target
    for i in range(1, len(numbers)):
        combs = list(map(lambda x : x, combinations(numbers,i)))
        for comb in combs : 
            if sum(comb)*2 == minus: answer += 1
    return answer

