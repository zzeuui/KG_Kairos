##OPERATE###################################

a=14
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)

#num = int(input())
num = 2955
dd = num // (60*24)
hh = (num %(60*24)) // 60
mm = num - dd * 60 *24 - hh * 60
print(dd, hh, mm)

##STRING######################################

a="python"
b="cpp"
print(a+b)
print(a*3)
print(len(a))

a="life is too short, you need python"
print(a[28:])
print(a[:4])

b="I am 30 years old"
print(b[5:7])

c="abababab"
print(c[1::2])

d=" python "
print(d[::-1])
print(d.count('o'))
print(','.join(d))
print(d.upper())
print(d.lstrip())
print(d.rstrip())
print(d.strip())

import random

#name=input("name:")
name="yjjung"
num = random.randint(100, 999)
print(name[:3]+str(num))

#url=input("url:")
url="https://naver.go.kr"
url=url.split('.')[0].split('//')[-1]
password = url[:3]+str(len(url))+str(url.count('e'))+'!'
print(password)

##BOOLEAN#####################################

print(bool(""))
print(1 < 2 < 3)

#num=int(input("num:"))
num = 13
if num%2==0:
    print("even")
else:
    print("odd")

n1 = int(input("num1:"))
n2 = int(input("num2:"))
n3 = int(input("num3:"))

if n1 > n2 and n1 > n3: 
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

num = input("id:")
num = int(num.split('-')[-1][1:3])
if 0 <= num <= 8:
    print('seoul')
else:
    print('not seoul')
