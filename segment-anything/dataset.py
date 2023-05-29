import numpy as np
import cv2
import os
import glob
from os import listdir
path = '/mmfs1/data/ezhil/BC/benchmark/lucchi_pp/lucchi_pp_em'
out = '/mmfs1/data/ezhil/BC/benchmark/lucchi_pp/dataset'
files = sorted(glob.glob(f'{path}/*'))
print("Number of slices = ",len(files)/2)
for f in files:
  image = cv2.imread(f)
  fil = f.split('/')[-1]
  n = fil.split('-')[-1].split('.')[0]
  print(n)
  cv2.imwrite(out+"/{img:04d}.png".format(img = int(n)), image)
