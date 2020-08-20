def solution(clothes):
    kv = {}
    for cloth in clothes:
        if cloth[1] in kv : 
            kv[cloth[1]] += 1
        else:
            kv[cloth[1]] = 2
    if len(kv) == 1 : return len(clothes)
    else :
        values = list(kv.values())
        answer = 1
        for value in values : answer *= value
        return answer-1

