import scipy
from scipy import io
import numpy as np

def loadmat(filename):
	'''
	this function should be called instead of direct spio.loadmat
	as it cures the problem of not properly recovering python dictionaries
	from mat files. It calls the function check keys to cure all entries
	which are still mat-objects
	'''
	def _check_keys(d):
		'''
		checks if entries in dictionary are mat-objects. If yes
		todict is called to change them to nested dictionaries
		'''
		for key in d:
			if isinstance(d[key], io.matlab.mio5_params.mat_struct):
				d[key] = _todict(d[key])
		return d

	def _todict(matobj):
		'''
		A recursive function which constructs from matobjects nested dictionaries
		'''
		d = {}
		for strg in matobj._fieldnames:
			elem = matobj.__dict__[strg]
			if isinstance(elem, io.matlab.mio5_params.mat_struct):
				d[strg] = _todict(elem)
			elif isinstance(elem, np.ndarray):
				d[strg] = _tolist(elem)
			else:
				d[strg] = elem
		return d

	def _tolist(ndarray):
		'''
		A recursive function which constructs lists from cellarrays
		(which are loaded as numpy ndarrays), recursing into the elements
		if they contain matobjects.
		'''
		elem_list = []
		for sub_elem in ndarray:
			if isinstance(sub_elem, io.matlab.mio5_params.mat_struct):
				elem_list.append(_todict(sub_elem))
			elif isinstance(sub_elem, np.ndarray):
				elem_list.append(_tolist(sub_elem))
			else:
				elem_list.append(sub_elem)
		return elem_list
		   
	
	data = scipy.io.loadmat(filename, struct_as_record=False, squeeze_me=True)
	return _check_keys(data)

mat = loadmat("alog_fold1.mat")
print mat['data'].keys()
#print mat['data']['test_ind']
#print mat['data']['test_vals']
#print mat['data']['Y']
print mat['data']['Y'].keys()
print len(mat['data']['Y']['vals'])
print len(mat['data']['Y']['subs'])
print mat['data']['Y']['vals'][3]
exit()
print len(mat['data']['test_ind'])
print len(mat['data']['Y'])
print len(mat['data']['test_vals'])
exit()
print mat['dt'].keys()
print mat['dt']['test']
print ("\n\n")
print mat['dt']['train']
exit()
print mat['data'].keys()
print mat['data']['test_vals']
print mat['data']['test_ind']
exit()
for item in mat['data']:
	print item
"""
	for inte in item:
		output_file.write(str(inte) + ', ')
	output_file.write('\n')
#print mat
"""
