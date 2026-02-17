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
def c_freq(arr)
print(scnd_max([1,23,4,5,4]))