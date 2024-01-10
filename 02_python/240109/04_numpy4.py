import numpy as np

#operation
na1 = np.array([[0,0,0],[1,1,1]], dtype=int)
print(na1)
print(na1.T) # [[0 1] [0 1] [0 1]]

x = np.arange(1,10)
y = np.arange(11, 20)
z = x + y
print(z) #[12 14 15 18 20 22 24 26 28]

a = np.array([1,2,3])
b = np.array([10,20,30])
print(2*a + b)

print(a == 2) #[F T F]
print(b > 10) #[F T T]
print((a == 2) & (b > 10)) #[F T F]

#practice
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(x[x%3==0]) # [3 6 .. 15 18]
print(x[x%4==1]) # [1 5 .. 13 17]
print(x[(x%3==0) & (x%4==1)]) # [9]

#boardcasting
x1 = np.arange(0,5)
x1 = x1.reshape(-1,1)
x2 = x1 + 1
x3 = x2 + 1
arr = np.hstack([x1,x2,x3])
print(arr + x1)
y = np.arange(0,3)
print(arr + y)

p = np.array([100, 80, 50])
n = np.array([3, 4, 5])

total = np.sum(p * n)
total = p @ n #dot product
print(f'total: {total}')

#fancy indexing
arr = np.arange(10)
idx = np.array([True, False, True, False, True,
                False, True, False, True, False])
print(arr[idx])
print(arr % 2)
print(arr % 2 == 0)
print(arr[arr % 2 == 0])

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr[:, [True,False,False, True]])
print(arr[[2,0,1], :])

