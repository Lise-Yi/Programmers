def solution(genres, plays):
    answer = []
    total = {}
    many = {}
    for i, genre in enumerate(genres):
        if genre in total:
            total[genre] += plays[i]
            many[genre].append((plays[i],i))
        else:
            total[genre] = plays[i]
            many[genre] = [(plays[i],i)]
    total = sorted(total.items(), key = (lambda x:x[1]), reverse = True)
    for k,v in many.items() : many[k] = sorted(v, key = (lambda x:x[0]), reverse=True)[:2]
    for to in total : 
        for m in many[to[0]] : answer.append(m[1])
    return answer
