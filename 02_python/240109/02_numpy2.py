import numpy as np

#check size
na1 = np.array([0,1,2,3,4,5,6,7,8,9])
na2 = np.array([[0,1,2],[3,4,5]])
na3 = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])

print(len(na1),len(na2),len(na3)) #10 2 2
print(len(na1),len(na2[0]),len(na3[1][0])) #10 3 3

print(na3.ndim) # dimension
print(na3.shape) # shape

# re-shape
na = np.arange(12)
print(na.reshape(3, 4))
print(na.reshape(3, -1))
print(na.reshape(2, 2, -1))

nb = na.reshape(3, 4)
print(nb)
print(nb.flatten())
print(nb.ravel())
print(nb.reshape(-1))

#create array
na = np.zeros(5)
print(na)
na = np.zeros((2, 3), dtype=int)
print(na)
na = np.zeros((2, 3, 4))
print(na)

na = np.zeros(5, dtype="U4") #U4: string
print(na)
na[0] = 'a'
na[1] = 'ab'
na[2] = 'abc'
na[3] = 'abcd'
print(na)

na = np.ones(5)
print(na)
na = np.ones((2,3), dtype='i')
print(na)

na = np.ones_like(na)
print(na)

na = np.empty((3,1))
print(na)

na = np.linspace(0, 100, 5, dtype=int)
print(na)

d = np.full(5, 15, np.float32)

arr = np.diag([1,2,3])
print(arr)

arr = np.identity(3, dtype=int)
print(arr)
arr = np.eye(4, dtype=int)
print(arr)

#practice
import cv2
image = np.zeros((768, 1024), np.uint8)
image.fill(200)      # 또는 image[:] = 200

cv2.imshow("Window title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
