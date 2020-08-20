def solution(brown, yellow):
    total = brown + yellow
    answer = []
    nums = list(range(3, int(total//3)+1))
    for num in nums:
        ans = []
        if total % num == 0:
            ans.append(num)
            ans.append(int(total/num))
            answer.append(ans)
    if len(answer) == 1:
        return answer[0]
    answer = answer[len(answer)//2:]
    for ans in answer:
        if yellow/(ans[0]-2) == ans[1]-2:
            return ans
