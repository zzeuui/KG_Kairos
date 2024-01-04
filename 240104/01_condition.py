##CONDITIONAL STATMENT#########################################

#a = int(input("num:"))
a = 13
if a%2==0:
    print("even")
else:
    print("odd")

print("even") if a%2==0 else print("odd")

money=2000
if money >= 5000:
    print("take taxi")
elif 1500 <= money < 3000:
    print("take a bus")
else:
    print("walk")

print("taxi") if money >= 5000 else print("bus") if 1500 <= money < 3000 else print("walk")

#n1 = int(input("num1:"))
#n2 = int(input("num2:"))
#n3 = int(input("num3:"))

n1, n2, n3 = 10, 20, 30
print(n1) if n1 >= n2 and n1 >= n3 else print(n2) if n2 >= n1 and n2 >= n3 else print(n3)

##QUIZ####################################################3

#1.
#num = input("id:").split('-')
num = '891010-1623192'.split('-')
num = [list(n) for n in num]
num = [int(n) for n in sum(num, [])]
#num = list(map(int, sum(num, [])))
x = [2,3,4,5,6,7,8,9,2,3,4,5]

ret = sum([i*j for i, j in zip(num[:-1], x)])%11
ret = 11 - ret

if ret == num[-1]:
    print("valid")
else:
    print("invalid")

#2.
#year = int(input("year:"))
year = 2024
if year % 4 == 0 and year % 100 != 0:
    print("leap year")
else:
    print("not leap year")

#3.
num = int(input("price:"))

discount = 5 if 10000 <= num < 50000 else 7.5 if 50000 <= num < 100000 else 10

print("price:", num)
print('rate of discount: {0}%'.format(discount))
print('amount of discount: {0:.0f}'.format(num*discount/100))
print('final price: {0:.0f}'.format(num-(num*discount/100)))
