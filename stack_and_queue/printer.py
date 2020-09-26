def solution(priorities, location):
    answer = 0
    std = sorted(priorities, reverse = True)
    for i, pr in enumerate(priorities) : priorities[i] = (i, pr)
    for s in std: 
        for ip in priorities:
            if ip[1] == s :
                answer += 1
                if ip[0] == location : return answer
                priorities = priorities[1:]
                break
            else: 
                priorities = priorities[1:] + [priorities[0]]