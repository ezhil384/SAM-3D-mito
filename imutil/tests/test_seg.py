import os,sys
from imu.seg import *
from imu.io import writeH5
import numpy as np
import cv2
import glob
def test_seg_track(seg, iou_thres=0.2):
    from imu.seg import predToSeg2d,seg2dToIoU
    seg3d_naive = predToSeg2d(seg, [-1])
    del seg
    matches = seg2dToIoU(seg3d_naive, iou_thres)
    seg3d = seg2dTo3d(seg3d_naive, matches)
    return seg3d


if __name__ == "__main__":
    import numpy as np
    path = '/mmfs1/data/ezhil/BC/benchmark/c_elegans/otsu_cuts'
    files = sorted(glob.glob(f'{path}/*.png'))
    l = len(files)
    print(l)
    image = cv2.imread(files[0])
    seg = np.zeros((l,image.shape[0],image.shape[1]),dtype=np.uint8)
    print(seg.shape)
    for i,f in enumerate(files):
        im = cv2.imread(f)
        seg[i] = im[:,:,2]
    out = test_seg_track(seg)
    print(out.shape)
    writeH5('otsu_elegans.h5', out)
