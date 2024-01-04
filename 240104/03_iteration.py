for i in [1,2,3,4,5]:
    print(i)

for i in ('a','b','c','d'):
    print(i)

for i in "python":
    print(i)

for i in range(100):
    print(i)

total = 0
for i in range(1, 101):
    total += i
print(total)

for i in [1,2,3,4]:
    for j in ['a','b']:
        print(i, j)

#n = int(input())
n=5
for i in range(1, 11):
    print(f'{i} * {n} = {i*n}')

apart = [[101,102], [201,202], [301,302]]

for floor in apart:
    for room in floor:
        print(f'{room} ho')

for i in range(8):
    print('*'*i)

for i in range(8)[::-1]:
    print('*'*i)

for i in range(8):
    print(f'{"*"*i:>8}')

for i in range(1, 14, 2):
    print(f'{"*"*i:^13}')

temp = list(range(1, 8, 2)) + list(range(1, 7, 2))[::-1]
for i in temp:
    print(f'{"*"*i:^7}')

for i in range(8):
    print(f'{" "*(8-i)}{"*"*i}')

for i in range(1, 14, 2):
    print(f'{" "*(13-i//2)}{"*"*i}{" "*(13-i//2)}')

for i in temp:
    print(f'{" "*(7-i//2)}{"*"*i}{" "*(7-i//2)}')
