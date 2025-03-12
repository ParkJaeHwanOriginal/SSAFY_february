def preorder(root,dict) :
    answer = ''
    stack = []
    answer += root
    stack.append(root)
    stack.append(root)
    while stack :
        if dict[root][0] != '.' or dict[root][0] != 1 :
            temp = dict[root][0]
            dict[root][0] = 1
            root = temp
            stack.append(root)
            answer += root
            continue
        elif dict[root][1] != '.' or dict[root][1] != 1 :
            temp = dict[root][0]
            dict[root][0] = 1
            root = temp
            stack.append(root)
            answer += root
            continue
        else :
            root = stack.pop()
        print(answer, stack, root)
    return answer
def inorder(dict) :
    pass
def postorder(dict) :
    pass

n = int(input())
dict = dict()
for l in range(n) :
    parent, child_1, child_2 = list(input().split())
    dict[parent] = [child_1, child_2]

print(preorder('A', dict))
# inorder(root)
# postorder(root)


# dict = {'a' : [1,2]}
# print(dict['a'], dict['a'][0])
# dict['a'][0] = 4
# print(dict['a'], dict['a'][0])