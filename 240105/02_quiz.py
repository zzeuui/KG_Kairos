k, n = list(map(int, input().split()))
cnt = 0
while True:
    k -= n
    if k >= 0:
        cnt += 1
        k += 1
    else:
        break

print(cnt)
