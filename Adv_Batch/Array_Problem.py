'''
Name : Yash Goyal
Enrollment : 0103IS231228
Batch : 17
Batch Time : 12:10PM to 1:50PM
'''

#Q1
def reverse(arr):
    return arr[::-1]

#Q2
def max_min(arr):
    max = arr[0]
    min = arr[0]
    for x in arr:
        if max < x:
            max = x
        if min > x:
            min = x
    return (max,min)

#Q3
def sum_ele(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum

#Q4
def scnd_max(arr):
    m = max(arr)
    n = 0
    for x in arr:
        if n < x and x != m:
            n = x
    return n

#Q5
def c_freq(arr):
    di = {}
    for x in arr:
        if x in di:
            di[x] += 1
        else:
            di[x] = 1
    return di

#Q6
def sorte(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

#Q7
def rotate(arr,k):
    for x in range(k):
        arr.insert(0,arr.pop())
    return arr

#Q8
def two_sum(arr,tar):
    for i,x in enumerate(arr):
        for y in arr[i+1::]:
            if x + y == tar:
                return (x,y)
    return 

#Q9
def rm_dupli(arr):
    ls = []
    for x in arr:
        if x in ls:
            continue
        else:
            ls.append(x)
    return ls

#Q10
def merge(arr1,arr2):
    i = 0
    j = 0
    res = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))
    while arr1:
        res.append(arr1.pop(0))
    while arr2:
        res.append(arr2.pop(0))
    return res

#Q11
def rm(arr,ele):
    arr.remove(ele)
    return arr

#Q12
def find_mis(arr,n):
    ls = [0] * n
    ans = []
    for x in arr:
        ls[x-1] = 1
    for i,x in enumerate(ls):
        if x == 0:
            ans.append(i+1)
    return ans

#Q13
def find_dupli(arr):
    temp = set()
    temp2 = set()
    for x in arr:
        if x in temp:
            temp2.add(x)
        else:
            temp.add(x)
    return temp2

#Q14
def inter(arr1,arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    return arr1.intersection(arr2)

#Q15
def uni(arr1,arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    return arr1.union(arr2)

#Q16
def equi(arr1,arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    n = len(arr1)
    if len(arr2) != n:
        return False
    else:
        for x in range(n):
            if arr1[i] != arr2[i]:
                return False
        return True

#Q17
def leader(arr):
    for i,x in enumerate(arr[:-1:]):
        found = True
        for y in arr[i+1::]:
            if x < y:
                found = False
                break
        if found:
            return x
    return None

#Q18
def move_zero(arr):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == 0:
            arr.append(arr.pop(i))
            n -= 1
        else:
            i += 1
    return arr

#Q19
def f_sub(arr,sum):
    arr = sorted(arr)
# to be done

#Q20
def rotate_lef(arr,k):
    for x in range(k):
        arr.insert(len(arr)-1,arr.pop(0))
    return arr

#Q21
def find_kth_smallest(arr,k):
    arr = sorted(arr)
    return arr[k-1]

#Q22
def all_subarrya(arr):
    return
# to be done

#Q23

#Q24
def rearrage_alt(arr):
    arr = sorted(arr)
    alt = True
    n = len(arr)
    i = 0
    while i < n:
        if alt:
            alt = False
            arr.insert(i,arr.pop())
            i += 1
        else:
            alt = True
            i += 1
    return arr

#Q25
def majority(arr):
    dic = {}
    for x in arr:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    max_v = 0
    max_k = 0
    for x in dic.items():
        if max_v < x[1]:
            max_v = x[1]
            max_k = x[0]
    return max_k if max_v > len(arr)/2 else None

#Q26
def peak(arr):
    n = len(arr) - 1
    for i,x in enumerate(arr):
        if i == 0:
            if arr[i] > arr[i+1]:
                return arr[i]
        if i == n:
            if arr[n] > arr[n-1]:
                return arr[n]
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return None

#Q27
#to be done

#Q28
def n_sort(arr):
    ls = [0]*3
    for x in arr:
        ls[x] += 1
    arr = [0]*ls[0]
    arr.extend([1]*ls[1])
    arr.extend([2]*ls[2])
    return arr

#Q29

#Q30
def n_array(arr):
    res = []
    for i,x in enumerate(arr):
        prod = 1
        for j,y in enumerate(arr):
            if i == j:
                continue
            prod *= y
        res.append(prod)
    return res

#Q31
def equili(arr):
    left_equili
    
print(n_array([1,1,1,1,2,2,2,2,2,10,11,4,5,2,3,4]))

