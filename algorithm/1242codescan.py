import sys
sys.stdin = open('input.txt' , 'r')

tc = int(input())
for i in range(1, tc + 1) :
    n, m = map(int, input().split())
    arr = [ input() for _ in range(n) ]
    dict = {'0' : '0000',
            '1' : '0001',
            '2' : '0010',
            '3' : '0011',
            '4' : '0100',
            '5' : '0101',
            '6' : '0110',
            '7' : '0111',
            '8' : '1000',
            '9' : '1001',
            'A' : '1010',
            'B' : '1011',
            'C' : '1100',
            'D' : '1101',
            'E' : '1110',
            'F' : '1111'}
    code_dict = {'3211' : 0,
                 '2221' : 1,
                 '2122' : 2,
                 '1411' : 3,
                 '1132' : 4,
                 '1231' : 5,
                 '1114' : 6,
                 '1312' : 7,
                 '1213' : 8,
                 '3112' : 9}

    code_lst = []
    for l in arr :
        temp_s = 0
        temp_e = len(l) - 1
        while temp_s < len(l) and l[temp_s] == '0' :
            temp_s += 1
        while temp_e >= 0 and l[temp_e] == '0' :
            temp_e -= 1
        if temp_s < temp_e :
            code_lst.append(l[temp_s:temp_e+1])
    code_lst = list(set(code_lst))
    print(code_lst, len(code_lst))

    code_lst = sorted(code_lst)
    end = len(code_lst)
    for o in range(len(code_lst)) :
        for oo in code_lst[1:] :
            if code_lst[o] in oo :
                if end > o :
                    end = o
    code_lst = code_lst[:o]

    answer = 0

    for l in code_lst :
        b = ''
        for ll in l :
            b += dict[ll]
        # print(b, len(b), 'b')
    #     decode_lst.append(b)
    # print(decode_lst)

    # width = len(b) // 56
    # b = b[len(b)-(56*width):]

        width = len(b) // 56
        if len(b) > (width*56) + 23 :
            width += 1

        temp_e = 1
        while b[-temp_e] == '0' :
            temp_e += 1
        for _ in range(temp_e-1) :
            b = '0' + b[:-1]
        # print(b, len(b))

        if len(b) > (56*width) :
            b = b[len(b)-(56*width):]
        else :
            b = '0' * ((width * 56) -len(b)) + b
        print(b, len(b))


        sum = 0
        temp_answer = 0
        for k in range(8) :
            temp_ratio = ''
            target = b[(7*k)*width:(7*(k+1))*width]
            # print(target)
            temp_num = target[0]
            temp_cnt = 1
            for j in target[1:] :
                if j == temp_num :
                    temp_cnt += 1
                else :
                    temp_num = j
                    temp_ratio += str(int(temp_cnt/width))
                    temp_cnt = 1
            temp_ratio += str(int(temp_cnt/width))
            if k == 0 or k == 2 or k == 4 or k == 6 : # 홀수자리
                sum += code_dict[temp_ratio] * 3
            else :
                sum += code_dict[temp_ratio]
            temp_answer += code_dict[temp_ratio]
        # print(sum)
        if sum % 10 == 0 :
            answer += temp_answer

    print(f'#{i} {answer}')





# a = '000000001DB176C588D26EC000'
# b = ''
# dict = {'0' : '0000',
#         '1' : '0001',
#         '2' : '0010',
#         '3' : '0011',
#         '4' : '0100',
#         '5' : '0101',
#         '6' : '0110',
#         '7' : '0111',
#         '8' : '1000',
#         '9' : '1001',
#         'A' : '1010',
#         'B' : '1011',
#         'C' : '1100',
#         'D' : '1101',
#         'E' : '1110',
#         'F' : '1111'}
# for i in a :
#     b += dict[i]
# cut = len(b)-1
# while b[cut] == '0' :
#     cut -= 1
# print(b[cut-56+1:cut+1], len(b[cut-56+1:cut+1]))