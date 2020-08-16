def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        next_phone = phone_book[i+1][:len(phone_book[i])]
        if phone_book[i] == next_phone:
            return False
    return True
