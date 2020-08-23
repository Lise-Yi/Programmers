def solution(prices):
    answer = []
    for i,price in enumerate(prices):
        answer.append(len(prices)-i-1)
        for i2 in range(i+1, len(prices)):
            if prices[i2] < price : 
                answer.pop()
                answer.append(i2-i)
                break
    return answer