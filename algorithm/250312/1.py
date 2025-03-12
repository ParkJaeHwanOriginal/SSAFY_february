# def KFC(n) :
#     print(n)
#     KFC(n+1)
#     return "끝"
#
# KFC(0)
# print('진짜 끝')

def KFC(n) :
    # 1. 종료 조건
    if n == 5 :
        return "끝"
    # 2. 함수의 실행 로직 -> 재귀호출 전 실행
    print(n)
    # 3. 다음 재귀 호출 (매개변수 변경하며 전달)
    KFC(n+1)
    # 4. 돌아오면서 해야 할 로직 (리턴하는 마지막 함수에선 실행 x)
    print("종료 조건인 5는 찍히지 않겠죠?", n)

KFC(0)