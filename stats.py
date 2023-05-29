import skimage
import numpy as np
import cv2
import glob
path = '/mmfs1/data/ezhil/BC/benchmark/lucchi_pp'
files = sorted(glob.glob(f'{path}/lucchi_pp_mito/*.png'))
print(len(files))
maxi=0
mini = 65536
max_len = 0
tp=0
index=0
print(cv2.imread(files[0]).shape)
for i,f in enumerate(files):
  im = cv2.imread(f)
  ux, uc = np.unique(im[:,:,2], return_counts=True)    
  uc = np.sort(uc)
  tp = tp + np.sum(uc[:-1])
  h = uc[-2]
  if i==55:
    m=h
  l = uc[0]
  c = len(uc)
  print(uc)
  if h>maxi:
    maxi = h
    index=i
  if l<mini:
    mini = l
  if c>max_len :
    max_len = c
print("Maximum =",maxi)
print("Minimum =",mini)
print("Max instances =",max_len)
print("Positives =", tp)
print(m,index)