from itertools import combinations


def solution(numbers, target):
    answer = 0
    maxi = sum(numbers)
    minus = maxi - target
    for i in range(1, len(numbers)):
        combs = list(map(lambda x: x, combinations(numbers, i)))
        for comb in combs:
            if sum(comb)*2 == minus:
                answer += 1
    return answer
