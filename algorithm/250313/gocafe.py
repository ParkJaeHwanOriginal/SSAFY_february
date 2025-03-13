arr = ['a', 'b', 'c', 'd', 'e']
n = len(arr)

# 1인 bit수를 반환하는 함수
def get_count(tar) :
    for i in range(n) :
        if (i << tar) &  0x1 :

# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
answer = 0
# 모든 부분 집합을 확인
for target in range(1 << n) :
    if get_count(target) >= 2 :


def get_sub(tar) :
    for i in range(n) :
        cnt = 0
        if tar & 0x1 :
            cnt += 1
        tar >>= 1
            if cnt >= 2 :
                print(arr[i], end = '')
for target in range(1 << n) :
    get_sub(target)
    print()