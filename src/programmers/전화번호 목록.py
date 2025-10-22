def solution(phone_book):
    hash_c = {}
    for i in phone_book:
        hash_c[i] = 1
    for i in hash_c:
        array = ""
        for j in i:
            array += j
            if array in hash_c and array != i:
                return False
    return True
