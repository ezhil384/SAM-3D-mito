import numpy as np
import skimage
import cv2
import glob
dataset = 'glycolytic_muscle'
path = '/mmfs1/data/ezhil/BC/benchmark/'+dataset
files = sorted(glob.glob(f'{path}/otsu_cuts/*.png'))
l = len(files)
print(l)
int_sum = 0
union_sum=0
for i,f in enumerate(files):
  pred = cv2.imread(f)
  path2 = path+'/'+dataset+'_mito/'+dataset+'_mito-{n}.png'.format(n = i)
  print("Processing1: ",path2)
  print("Processing2: ",f)
  target = cv2.imread(path2)
  intersect = np.count_nonzero(np.logical_and(pred[:,:,2] > 0, target[:,:,2]>0))
  union = np.count_nonzero(np.logical_or(pred[:,:,2] > 0, target[:,:,2]>0))
  int_sum = int_sum + intersect
  union_sum = union_sum + union
print("Intersecion and union",int_sum, union_sum)
iou = (int_sum + 1e-5) / (union_sum + 1e-5)
print("IoU", iou)
