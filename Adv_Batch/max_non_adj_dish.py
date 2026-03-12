def max_dishes(N,A):
    if N == 0:
        return 0
    
    def to_int(ls):
        for i,x in enumerate(ls):
            ls[i] = int(x)
        return ls
    
    A = to_int(A)
    dic = {}
    dic[A[0]] = []
    st = str(A[0])
    last = A[0]
    for x in A[1::]:
        if x != last:
            if x not in dic:
                dic[last].append(st)
                dic[x] = []
                st = str(x)
                last = x
            else:
                dic[last].append(st)
                st = str(x)
                last = x
        else:
            st += str(x)
    dic[last].append(st)
    print(dic)
    
    def count(ls):
        n = 0
        for x in ls:
            c = len(x)
            if c % 2 == 0:
                n += c//2
            else:
                n += ((c//2) + 1) 
        return n

    for x in dic.keys():
        dic[x] = count(dic[x])
    res = max(dic, key=dic.get)
    return dic[res]


n_test_cases = int(input())
for i in range(n_test_cases):
    n_dishes = int(input())
    dishes = input().split()
    print(max_dishes(n_dishes,dishes))


#print(max_dishes(9,[1,2,2,1,2,1,1,1,1]))