import numpy as np
import cv2
import os
import glob
from os import listdir
path = '/mmfs1/data/ezhil/BC/segment-anything/benchmark_outputs/lucchi'
out = '/mmfs1/data/ezhil/BC/benchmark/lucchi_pp'
folders = sorted(glob.glob(f'{path}/*'))
print("Number of slices = ",len(folders))

def otsu(gray):
    pixel_number = len(gray)
    #pixel_number = gray.shape[0] * gray.shape[1]
    mean_weigth = 1.0/pixel_number
    his, bins = np.histogram(gray, np.array(range(0, 256)))
    final_thresh = -1
    final_value = -1
    for t in bins[1:-1]: # This goes from 1 to 254 uint8 range (Pretty sure wont be those values)
        Wb = np.sum(his[:t]) * mean_weigth
        Wf = np.sum(his[t:]) * mean_weigth

        mub = np.mean(his[:t])
        muf = np.mean(his[t:])

        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    return final_thresh

for i,folder in enumerate(folders):
    f1 = folders[i] 
    im_path = out + "/dataset/{img:04d}.png".format(img = i)
    data = cv2.imread(im_path)  
    files = sorted(glob.glob(f'{f1}/*.png'))
    image = cv2.imread(files[0])
    ins = np.zeros((image.shape),dtype=np.uint8)
    col = len(files)-1
    print(len(files))
    for j,f in enumerate(files):
        if j>len(files)-10:
            break
        image = cv2.imread(f)
        crop = image == 255 
        crop_size = np.count_nonzero(crop)
        if crop_size>image.size/4 or crop_size<10:
            continue
        if np.count_nonzero(ins[crop])< crop_size and np.count_nonzero(ins[crop])>10:
            continue
        thres = otsu(data[crop])
        if thres >135 or thres<115:
            continue
        # ave = np.mean(data[crop])
        # if ave>140 or ave<90:
        #     continue
        mask = np.logical_and(crop, ins == 0)
        ins[mask] = col
        col=col-1
    cv2.imwrite(out+"/otsu_cuts/{img:04d}.png".format(img = i), ins)