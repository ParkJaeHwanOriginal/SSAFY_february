# lst = []
# print(2, end = ' ')
# cnt = 0
# for i in range(3, 1000000, 2) :
#     is_prime = 1
#     for l in lst :
#         a = i % l
#         if a == 0 :
#             is_prime = 0
#             break
#     if is_prime == 1 :
#         if i < 500000 :
#        	    lst.append(i)
#         cnt += 1
#         print(i, end = ' ')
# print(cnt)

lst = []
print(2, end = ' ')
cnt = 1
for i in range(3, 1000000, 2) :
    is_prime = 1
    for l in lst :
        a = i % l
        if a == 0 :
            is_prime = 0
            break
    if is_prime == 1 :
        cnt += 1
        if i < 1000 :
       	    lst.append(i)
        print(i, end = ' ')
print(cnt)
