import numpy as np
import cv2
import glob
path = '/mmfs1/data/ezhil/BC/benchmark/glycolytic_muscle/otsu_cuts'
files = sorted(glob.glob(f'{path}/*.png'))
l = len(files)
print(l)
image = cv2.imread(files[0])
seg = np.zeros((l,image.shape[0],image.shape[1]),dtype=np.uint8)
print(seg.shape)
for i,f in enumerate(files):
  im = cv2.imread(f)
  seg[i] = im[:,:,2]
np.save('otsu_muscle.npy',seg)