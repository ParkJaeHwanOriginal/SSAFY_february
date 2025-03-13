arr = ['a', 'b', 'c']
n = len(arr)
def get_sub(tar) :
    for i in range(n) :
        if tar & 0x1 :
            print(arr[i], end = '')
        tar >>= 1
for target in range(1 << n) :
    get_sub(target)
    print()