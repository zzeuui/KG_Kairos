import numpy as np

#introduce to functions...
x = np.arange(15, dtype=np.int64)
x = x.reshape(3, 5)
print(x)

ret = x.max(axis=1)
print(ret)

rng = np.random.default_rng()
samples = rng.normal(size=2500)
print(samples)

#initialization of numpy array
a = [1,2,3,4,5]
b = np.array(a)
c = np.array([1, 3, 5])

print(a) #[1, 2, 3, 4, 5]
print(b) #[1 2 3 4 5]
print(c) #[1 3 5]

#operation
print(a*2)
print(b*2)
print(c+3)

#array type 
d = np.array([1, 3.0, 5])
print(c.dtype)
print(d.dtype)

na = np.array([0,1,2,3,4])
print(na)
print(na.dtype)

na = na.astype(np.float64)
print(na)
print(na.dtype)

#copy
a = np.array([1, 2, 3, 4, 5])
b = a
c = a.copy()
b[0] = 99
print(a)
print(b)
print(c)

#indexing
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[0])
print(a[0][2])

na1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(na1[2])
print(na1[1:3])
print(na1[::-1])
print('-'*20)

na2 = np.array([[0,1,2],[3,4,5]])
print(na2[0,0])
print(na2[-1,2])
print(na2[:,1])
print(na2[1,1:])
print('-'*20)

na3 = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])
print(na3[0,0])
print(na3[0,1,2])
print(na3[1,1:2,2])
