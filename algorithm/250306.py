def todec(str, bit) : # bit str을 10진수로 -> 16진수 17을 10진수로 바꾸기
    value = 0
    for c in str :
        if c.isdigit():
            value = (value * bit) + int(c)
        else :
            value = (value*bit) + ord(c) - ord('A') + 10

    return value

def decto(n, bit) : # n을 bit진수로 바꾸기 -> 10을 16진수로 바꾸기
    result = ''
    while n :
        remain = n % bit
        n = n // bit
        if remain < 10 : # 16진수 변환 고려
            result = str(remain) + result
        else :
            # 'A' ~ 'F'
            result = chr(ord('A') + (remain - 10)) + result

    return result

print(todec('333', 10))
print(todec('17', 16))

print(decto(22, 2))
print(decto(10, 16))
print(todec('47FE',16))
print(decto(7774,2))