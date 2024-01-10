import numpy as np

#stack
na1 = np.ones((2,3), dtype=int)
na2 = np.zeros((2,2), dtype=int)
print(na1)
print(na2)
print(np.hstack([na1, na2]))

na1 = np.ones((2,3), dtype=int)
na2 = np.zeros((3,3), dtype=int)
print(na1)
print(na2)
print(np.vstack([na1, na2]))

na1 = np.zeros(2, dtype=int)    # [0 0]
na2 = np.ones(2, dtype=int)     # [1 1]
na3 = np.full(2, 2,  dtype=int) # [2 2]
na = np.dstack([na1, na2])
print(na.shape) #(1, 2, 2)
print(na) #[[[0,1],[0,1]]]
na = np.dstack([na1, na2, na3])
print(na.shape) # (1, 2, 3)
print(na) #[[[0,1,2],[0,1,2]]]

na1 = np.zeros((2,3), dtype=int)   # [[0 0 0],[0 0 0]]
na2 = np.ones((2,3), dtype=int) 
na3 = np.full((2,3), 2,  dtype=int)
na = np.dstack([na1, na2])
print(na.shape)
print(na) #[[[0 1] [0 1] [0 1]] [[0 1] [0 1] [0 1]]]
na = np.dstack([na1, na2, na3])
print(na.shape)
print(na) #[[[0 1 2] [0 1 2] [0 1 2]] [[0 1 2] [0 1 2] [0 1 2]]]

na1 = np.zeros(2, dtype=int)    # [0 0]
na2 = np.ones(2, dtype=int)     # [1 1]
na3 = np.full(2, 2,  dtype=int) # [2 2]
na = np.stack([na1, na2])  # default: axis=0
print(na) # [[0 0] [1 1]]
print(na.shape)
na = np.stack([na1, na2], axis=1)
print(na) # [[0 1] [0 1]]
print(na.shape)

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
print( np.tile(a, 2) ) #[[0 1 2 0 1 2] [3 4 5 3 4 5]]
