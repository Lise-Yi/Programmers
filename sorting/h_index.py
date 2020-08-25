def solution(citations):
    citations.sort(reverse=True)
    possible_index = sorted(list(range(0,len(citations)+1)), reverse = True)
    for index in possible_index:
        over = 0 
        for citation in citations:
            if citation >= index: 
                over += 1
            else:
                break
        if over >= index : return index
