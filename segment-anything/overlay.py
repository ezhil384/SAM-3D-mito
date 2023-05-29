import skimage
import numpy as np
import cv2
import glob
path = '/mmfs1/data/ezhil/BC/benchmark/c_elegans'
files = sorted(glob.glob(f'{path}/dataset/*.png'))
print(len(files))
for i,f in enumerate(files):
  im = cv2.imread(f)
  res = skimage.color.rgb2gray(im)
  label = cv2.imread(path+'/c_elegans_mito/c_elegans_mito-{lab}.png'.format(lab=i))
  print(f)
  fin = skimage.color.label2rgb(label[:,:,0],image=res,alpha=0.15, bg_label=0, bg_color=(0, 0, 0))
  fin = fin*255
  cv2.imwrite("/mmfs1/data/ezhil/BC/benchmark/c_elegans/overlay/{img:04d}.png".format(img = i), fin)