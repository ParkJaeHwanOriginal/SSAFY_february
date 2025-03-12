# [0, 1, 2] 3개의 카드가 존재
# 2개를 뽑을 예정

path = []
def recur(cnt, cnt_card) :
    # 카드를 2개 뽑으면 종료
    if cnt == 2 :
        print(*path)
        return

    # 1. 1개의 카드를 뽑는다 2. 다음 재귀 호출 (뽑은 카드가 1개 추가되었다)
    for num in range(cnt_card) :
        path.append(num)
        recur(cnt + 1, cnt_card)
        path.pop()


# 제일 처음 호출 시점
# 초기값 전달하며 시작

recur(0, 3)