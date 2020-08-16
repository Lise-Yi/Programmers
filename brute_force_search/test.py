def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    scores = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            scores[1]+=1
        if answers[i] == second[i%len(second)]:
            scores[2]+=1
        if answers[i] == third[i%len(third)]:
            scores[3]+=1
    maxi = scores[1]
    for num, score in scores.items():
        if maxi == score:
            answer.append(num)
        if maxi < score:
            answer = [num]
            maxi = score
    return answer
