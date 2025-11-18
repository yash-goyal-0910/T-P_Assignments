'''
Name : Yash Goyal
Enrollment : 0103IS231228
Batch : 5
Batch Time : 10:30AM to 12:10PM
'''

# Conditional Statement

# Baise If-Else Problems

# Q1
num = int(input())
if num > 0:
    print("num is +ive")
elif num == 0:
    print("num is zero")
else:
    print("num is -ive")

# Q2
num = int(input())
if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")

# Q3
year = int(input())
if (year%400 == 0 or year%100 != 0) and year%4 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} isn't leap year")

# Q4
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(f"{num1} is greater")
elif num1 < num2:
    print(f"{num2} is greater")
else:
    print(f"both num is equal")

# Q5
age = int(input())
if age >= 18:
    print("eligible for voting")

# Q6
char = input()
vowel = ['a','e','i','o','u']
if char in vowel:
    print("char is vowel")
else:
    print("char isn't vowel")

# Q7
num = int(input())
if num%5 == 0:
    print("num is divided by 5")

# Q8
num = str(int(input()))
if len(num) == 1:
    print("num is single digit")
elif len(num) == 2:
    print("num is double digit")
else:
    print("num is more than two digit")

# Q9
marks = int(input())
if marks >= 40:
    print("student is passed")
else:
    print("studetn is failed")

# Q10
num = int(input())
if num%3 and num%7:
    print("num is multiple of both")

# Ladder If & Nested If

# Q1
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2:
    if num1 > num3:
        print("num1 is greatest")
    else:
        print("num3 is greatest")
else:
    if num2 > num3:
        print("num2 is greates")
    else:
        print("num3 is greatest")

# Q2
age = int(input())
if age < 13:
    print('person is child')
elif age < 20:
    print("person is Teenager")
elif age < 60:
    print("person is Adult")
else:
    print("person is Senior")

# Q3
marks = int(input())
if marks < 35:
    print('Fail')
elif marks < 50:
    print("D")
elif marks < 75:
    print("C")
elif marks < 90:
    print("B")
elif marks < 101:
    print("A")

# Q4
s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1 == s2:
    if s1 == s3:
        print("equilateral")
    else:
        print("isosceles")
else:
    if s1 == s3 or s2 == s3:
        print("isosceles")
    else:
        print("scalene")

# Q5
char = input()
if char.isdigit():
    print('digits')
elif char.islower():
    print('Lower case')
elif char.isupper():
    print('upper case')
elif (not char.isalnum()) and char.isascii():
    print('special characters')

# Q6
units = int(input())
cost = 0
if units > 200:
    cost = ((units-200)*10) + 700 + 500
elif units > 100:
    cost = ((units-100)*7) + 500
else:
    cost = units * 5
print(cost)

# Q7
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("num1 is greatest")
        else:
            print("num4 is greatest")
    else:
        if num3 > num4:
            print("num3 is greatest")
        else:
            print("num4 is greatest")
else:
    if num2 > num3:
        if num2 > num4:
            print("num2 is greatest")
        else:
            print("num4 is greatest")
    else:
        if num3 > num4:
            print("num3 is greatest")
        else:
            print("num4 is greatest")

# Q8
year = int(input())
if (year%400 == 0 or year%100 != 0) and year%4 == 0:
    if year%100 == 0:
        print(f"{year} is leap year and century year")

# Q9
weight = int(input())
height = int(input())
height *= height
BMI = weight/height
if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")

# Q10
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 < num2:
    if num1 < num3:
        print("num1 is smallest")
    else:
        print("num3 is smallest")
else:
    if num2 < num3:
        print("num2 is smallest")
    else:
        print("num3 is smallest")

# For loop Problems

# Q1
for i in range(100,1000):
    x = str(i)
    sum = 0
    for y in x:
        sum += int(y) ** 3
    if sum == i:
        print(i)

# Q2
n = int(input())
for i in range(2,n):
    if i == 2:
        print(i)
    for j in range(2,i):
        if j > i/2:
            print(i)
            break
        if i%j == 0:
            break
    
# Q3
for i in range(500):
    if i % 3 != 0:
        continue
    x = str(i)
    sum = 0
    for y in x:
        sum += int(y)
    if sum < 11:
        print(i)

# Q4
n = int(input())
for i in range(n):
    print((n - i)  * ' ' + (i*2+1) * '*')

# Q5
inputstr = input()
inputstr = set(inputstr)
if len(inputstr) == 26:
    print('pangram')

# Q6
prime = []
for i in range(2,101):
    if i == 2:
        print(i)
    for j in range(2,i):
        if j > i/2:
            prime.append(i)
            break
        if i%j == 0:
            break
for i in range(99):
    if i in prime and i+2 in prime:
        print(i,i+2)

# Q7
num = int(input())
x = str(num)
sum = 0
for y in x:
    sum += int(y)
if num%sum == 0:
    print('Harshad')

# Q8
numRows = int((input()))
if numRows == 1:
    print( [[1]] )
x = [[1],[1,1]]
if numRows == 2:
    print(x)
i = 2
while(i < numRows):
    i += 1
    a = x[-1]
    l = [1]
    for y in range(len(a)-1):
        l.append(a[y] + a[y+1])
    l.append(1)
    x.append(l)
print(x)

# Q9
num = int(input())
sum = 0
for i in range(1,num+1):
    sum += i ** 2
print(sum)

# Q10
num = int(input())
x = str(num)
sum = 0
for i in x:
    if i == '0':
        sum += 1
    mul = 1
    for j in range(1,int(i)+1):
        mul *= j
    sum += mul
if sum == num:
    print('strong num')

# Whle loop problems

# Q11
num = int(input()[::-1])
i = 1
prime = True
while prime and i < num:
    i += 1
    if num % i == 0:
        prime = False
if prime:
    print(prime)

# Q12
sum = 0 
while sum < 101:
    num = int(input())
    sum += num

# Q13
num = input()
Duck = False
i = 0
while not Duck and i < (len(num) - 1):
    i += 1
    if num[i] == '0':
        Duck = True
        print('Duck')

# Q14
num = input()
i = -1
while i < len(num)-1:
    pass
    for x in num:
        pass