import numpy as np
import cv2
import os
import h5py
d = 'lucchi_pp'
def readh5(filename, dataset=None):
    fid = h5py.File(filename, 'r')
    if dataset is None:
        # load the first dataset in the h5 file
        dataset = list(fid)[0]
    return np.array(fid[dataset])
gt_path = '/mmfs1/data/ezhil/BC/benchmark/'+d+'/'
img = cv2.imread(gt_path+d+'_mito/{n}.png'.format(n = 0))
n=165
gt_seg = np.zeros((n, img.shape[0], img.shape[1]), dtype=np.uint8)
pred_seg = np.zeros((n, img.shape[0], img.shape[1]), dtype=np.uint8)
print(gt_seg.shape)
for i in range(n):
  img = cv2.imread(gt_path+d+'_mito/{x}.png'.format(x = i))
  #img2 = cv2.imread(gt_path+'tracked/{x:04d}.png'.format(x = i))
  gt_seg[i] = img[:,:,0]
  #pred_seg[i] = img2[:,:,2]
# pred_seg = readh5("/mmfs1/data/ezhil/BC/imutil/test_elegans.h5")
# print(pred_seg.shape)
gt_ids, gt_c = np.unique(gt_seg, return_counts=True)
#pred_ids, pred_c = np.unique(pred_seg, return_counts=True)
gt_c = np.sort(gt_c)
#pred_c = np.sort(pred_c)
small_gt = gt_c[0]
#small_pred = pred_c[0]
tp = len(gt_ids-1)
print(small_gt, tp)
print(gt_c)
