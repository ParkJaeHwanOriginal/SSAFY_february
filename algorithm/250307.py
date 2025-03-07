print(7&5)
print(7|5)

# 1. 이진수로 변환
# 2. 각 자리를 AND, OR로 연산한다.




arr = [1,2,3,4]
n = len(arr)

for i in range(1 << n) :
    for j in range(n) :
        if i & (1 << j) :
            print(arr[j], end = " ")
    print()
