def pre_order(n) :          # 완전이진트리의 전위순회
    if n <= N :             # 실존하는 정점이면
        print(n)            # visit(n)
        pre_order(n*2)
        pre_order(n*2+1)

N = 9           # 완전 이진 트리 정점 수
tree = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19]

pre_order(1)