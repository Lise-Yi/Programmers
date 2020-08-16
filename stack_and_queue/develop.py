def solution(progresses, speeds):
    answer = []
    if (100-progresses[0])%speeds[0] == 0:
        maxi = (100-progresses[0])//speeds[0]
    else:
        maxi = (100-progresses[0])//speeds[0]+1
    cnt = 1
    for i in range(1,len(speeds)):
        if (100-progresses[i])%speeds[i] == 0:
            std = (100-progresses[i])//speeds[i]
        else:
            std = (100-progresses[i])//speeds[i]+1
        if std <= maxi : 
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            maxi = std
    answer.append(cnt)
    return answer
