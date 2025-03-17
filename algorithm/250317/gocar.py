t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    answer = 0
    ga = 0
    for i in range(n) :
        str = input()
        if len(str) != 1 :
            a, b = str.split()
            if int(a) == 1 :
                ga += int(b)
            else :
                ga -= int(b) if ga >= int(b) else 0
        answer += ga
    print(f'#{tc} {answer}')