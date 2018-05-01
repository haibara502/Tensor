import numpy as np
from scipy import io

mat = io.loadmat('alog_fold1.mat')
print(mat.keys())
#print(mat.values())
print(mat['data'].shape)

mat4py_load = 
mat_t = np.transpose(mat['data'])
#print mat_t

matt = mat_t.getfiled(tr, 'Base')

mat = np.matrix(mat_t)
#print mat_t
print ("2")
for item in mat:
	for subitem in item:
		for subbitem in subitem:
			print subbitem
exit()
with open("outputfile.txt", 'wb') as f:
	for line in mat_t:
		for subline in line:
			np.savetxt(f, subline, fmt='%d')
exit()

#print mat

mat_contents = scipy.io.loadmat('alog_fold1.mat', squeeze_me = True)
print mat_contents['data']

import json
#alist = json.loads(mat_contents['data'])
#print alist
