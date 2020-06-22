import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv)==1:
    print('usage: python thisScript.py filename')
    exit(0)
filename = sys.argv[1]
try:mat = plt.imread('test.jpg')
except: print('[error] cant open file {0}, abort.'.format(filename)); exit(1)

mat = np.mean(mat, axis=2)[..., np.newaxis]  # gray scale
mat = np.dstack([mat, mat, mat])/255  # correct dimensionality
alpha = np.mean(mat, axis=2)[..., np.newaxis]  # calculate alpha channel
mat_final = np.dstack([np.ones(mat.shape), alpha])  # pack

plt.imsave('{0}.obs.png'.format(filename), mat_final, format='png')
print('[log] finished.')

