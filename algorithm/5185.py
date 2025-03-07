# import sys
# sys.stdin = open("input.txt", "r")
#
# tc = int(input())
# def hextobi(n) :
#     if not n.isdigit() :
#         n = 10 + (ord(n) - ord('A'))
#     n = int(n)
#     value = ''
#     for i in range(4) :
#         if n > 0 :
#             value = repr(n % 2) + value
#             n = n // 2
#         else :
#             value = '0' + value
#     return value
#
# for i in range(1, tc+1) :
#     n, str = input().split()
#     answer = ''
#     for l in str :
#         answer += hextobi(l)
#
#     print(f'#{i} {answer}')


print(1*2**-1)