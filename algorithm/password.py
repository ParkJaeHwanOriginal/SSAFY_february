import sys
sys.stdin = open("input.txt","r")

tc = int(input())
for i in range(1, tc+1) :
    n, m = map(int,input().split())
    password = ''
    for l in range(n) :
        str = input()
        for ll in str :
            if ll == '1' :
                password = str

    cnt = 0
    for l in password[::-1] :
        if l == '1' :
            break
        cnt += 1

    num_dict = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
    num = ''
    code = 0
    valid = 0
    tri = 3
    for k in password[m-56-cnt:m-cnt]:
        if len(num) != 7 :
            num += k
        if len(num) == 7 :
            code += num_dict[num]
            valid += tri * num_dict[num]
            num = ''
        if tri != 3 :
            tri = 3
        else :
            tri = 1

    if valid % 10 == 0 :
        print(f'#{i} {code}')
    else :
        print(f'#{i} 0')
