import numpy as np

a = np.array([[1, 2],[1,2]])

print(np.mean(a,axis=0,dtype=np.float64).tolist())