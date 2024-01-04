##LIST#######################################################

list0 = []
list1 = [1, 2, 3, 4]
list2 = ['john', 'smith', 'bob']
list3 = [1, 2, 3, 'a', 'b', 4.5]
list4 = ['a','b', [1,2,3]]

print(list4)
print(list4[0])
print(list4[2][2])
print(list4[-1])
print(list4.index('a'))

list4.append(2)
list4.append(3)
print(list4)

list4.insert(1, '#')
print(list4)

list4.remove('#')
print(list4)

list4.pop(0)
print(list4)

list1.extend(list2)
print(list1)

print(list1+[7,8,9])

import random
menu=['a','b','c','d']
print(random.choice(menu))

print(dir(list))

list2.sort()
print(list2)

##TUPLE###################################################

t = ()
t1 = (1,)
t3 = (1)
print(type(t3))

t2 = (1, 2, 3, 'b')
print(t2)
print(t2[0])
print(t2[-1])
print(t2[1:3])
print(t1+t2)
print(len(t2))

t4 = tuple(range(1, 11))
print(t4)
l4 = list(range(1, 11))
print(l4)

print(1 in t2)
print(5 in t2)
print(1 not in t2)
print(5 not in t2)

a = [1, 2, 3]
b = a
c = a[:]
d = list(a)

todo = ['english', 'math', 'python']
print('To-Do List:')
for d in todo:
    print(f'- {d}')

#sub = input()
sub = 'math'
todo.remove(sub)

print('To-Do List:')
for d in todo:
    print(f'- {d}')

##DICT#############################################################333

dict0 = {'name': 'yjjung', 'phone':'000-0000-0000',
         'birth':'001122', 'birth':'112233'}
print(dict0)
print(dict0['name'])

dict0['name'] = 'jyjung'
print(dict0)

del dict0['name']
print(dict0)

print(dict0.keys())
print(type(dict0.values()))
print(dict0.items())

for k, v in dict0.items():
    print(k, v)

print(len(dict0))

print('phone' in dict0)
print('phone' not in dict0)

##QUIZ########################################################

d = dict()
while True:
    n = input("english:")
    if not n:
        break
    else:
        d[n] = input("korean:")

print('test')
corr = 0
for k, v in d.items():
    print(f'{k}:', end='')
    u = input()
    if v == u:
        corr += 1

print(f'correct/ totla: {corr} / {len(d)}')
