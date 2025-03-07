'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(t) :                  # 전위 순회, 방문한 정점 (부모) 먼저 처리
    if t :                          # 0이 아니면 ( 존재하는 정점이면 )
        print(t)                    # visit(t) t에서 할 일 처리
        pre_order(left[t])          # 왼쪽 자식 (서브 트리) 로 이동
        pre_order(right[t])         # 오른쪽 자식 (서브 트리) 로 이동

def in_order(t) :                   # 중위 순회
    if t :                          # 0이 아니면 ( 존재하는 정점이면 )
        in_order(left[t])           # 왼쪽 자식 (서브 트리) 로 이동
        print(t)                    # visit(t) t에서 할 일 처리
        in_order(right[t])          # 오른쪽 자식 (서브 트리) 로 이동

def post_order(t) :                 # 후위 순회
    if t :                          # 0이 아니면 ( 존재하는 정점이면 )
        post_order(left[t])         # 왼쪽 자식 (서브 트리) 로 이동
        post_order(right[t])        # 오른쪽 자식 (서브 트리) 로 이동
        print(t)                    # visit(t) t에서 할 일 처리

N = int(input())
E = N - 1
arr = list(map(int, input().split()))
cnt = 0

left = [0] * (N + 1)        # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (N + 1)       # 부모를 인덱스로 오른쪽 자식 저장
par = [0] * (N + 1)         # 자식을 인덱스로 부모 저장

for i in range(E) :         
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p              # 자식을 인덱스로 부모 저장

    if left[p] == 0 :       # 왼쪽 자식이 아직 없으면
        left[p] = c
    else :
        right[p] = c
print(left, right)
pre_order(3)

# 루트 찾기
root = 1
for i in range(1, N+1) :
    if par[i] == 0 :
        root = i
        break
