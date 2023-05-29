import numpy as np
import cv2
import os
import h5py
def readh5(filename, dataset=None):
    fid = h5py.File(filename, 'r')
    if dataset is None:
        # load the first dataset in the h5 file
        dataset = list(fid)[0]
    return np.array(fid[dataset])
def segToRgb(seg):
    # convert to 24 bits
    return np.stack([seg//65536, seg//256, seg%256],axis=2).astype(np.uint8)

seg = readh5('/mmfs1/data/ezhil/BC/imutil/otsu_elegans.h5')
print(seg.shape)
unique_id = np.unique(seg)
unique_id = np.sort(unique_id)
print("Initial number of labels: ",len(unique_id)-1)
lab = 1
for id in unique_id:
    if id==0:
        continue
    mask = seg == id
    if np.count_nonzero(mask)<1000:
        print(np.count_nonzero(mask))
        seg[mask] = 0
        continue
    if lab%256==0:
        lab=lab+1
    seg[mask] = lab
    lab=lab+1
print("Labels made: ",lab-1) 
ux,uc = np.unique(seg,return_counts=True)
uc=np.sort(uc)
print("Unique lables in seg: ",len(ux))
print("Smallest instance: ",uc[0])
for j in range(seg.shape[0]):
    y=seg[j,:,:]
    cv2.imwrite("/mmfs1/data/ezhil/BC/benchmark/c_elegans/otsu_cuts/{sg:04d}.png".format(sg = j),segToRgb(y))
