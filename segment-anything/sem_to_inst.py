import numpy as np
import cv2
import os
import glob
from os import listdir
path = '/mmfs1/data/ezhil/BC/segment-anything/benchmark_outputs/lucchi'
out = '/mmfs1/data/ezhil/BC/benchmark/lucchi_pp'
out2 = '/mmfs1/data/ezhil/BC/crops'
folders = sorted(glob.glob(f'{path}/*'))
print("Number of slices = ",len(folders))
for i,folder in enumerate(folders):
    f1 = folders[i]   
    files = sorted(glob.glob(f'{f1}/*.png'))
    image = cv2.imread(files[0])
    ins = np.zeros((image.shape),dtype=np.uint8)
    col = len(files)-1
    print(len(files))
    for j,f in enumerate(files):
        if j>=len(files)-10:
            break
        image = cv2.imread(f)
        crop = image == 255 
        crop_size = np.count_nonzero(crop)
        if crop_size>image.size/4 or crop_size<20:
            continue
        if np.count_nonzero(ins[crop])< crop_size and np.count_nonzero(ins[crop])>10:
            continue
        mask = np.logical_and(crop, ins == 0)
        ins[mask] = col
        col=col-1
    # ux,uc = np.unique(ins,return_counts=True)
    # for k in ux:
    #     if k==0:
    #         continue
    #     if np.count_nonzero(ins == k)>8000:
    #         ins[ins==k] = 0
    
    cv2.imwrite(out+"/raw_SAM/{img:04d}.png".format(img = i), ins)
    # cv2.imwrite(out2+"/high_res_SAM/{img:04d}.png".format(img = i), ins)