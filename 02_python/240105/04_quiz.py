import random

cnt = 0
for i in range(1, 51):
    time = random.randint(5, 50)
    if 5 <= time <= 15:
        print(f'[O] {i}th customer (time: {time}min)') 
        cnt += 1
    else:
        print(f'[ ] {i}th customer (time: {time}min)') 

print(f'total: {cnt}')
