import neuroglancer
import numpy as np
import imageio
import h5py

ip = 'localhost' #or public IP of the machine for sharable display
port = 9997 #change to an unused port number
neuroglancer.set_server_bind_address(bind_address=ip,bind_port=port)
viewer=neuroglancer.Viewer()

D1='/mmfs1/data/ezhil/BC/imutil/'
D0='/mmfs1/data/ezhil/BC/pytorch_connectomics/'

res = neuroglancer.CoordinateSpace(
        names=['z', 'y', 'x'],
        units=['nm', 'nm', 'nm'],
        scales=[60, 15, 15])

print('load im and gt segmentation')
with h5py.File(D1+'test_elegans.h5', 'r') as fl:
    gt = np.array(fl['main'])
with h5py.File(D0+'elegans_image.h5', 'r') as fl:
    im = np.array(fl['main'])
print(im.shape,gt.shape)

def ngLayer(data,res,oo=[0,0,0],tt='segmentation'):
    return neuroglancer.LocalVolume(data,dimensions=res,volume_type=tt,voxel_offset=oo)

with viewer.txn() as s:
    s.layers.append(name='im',layer=ngLayer(im,res,tt='image'))
    s.layers.append(name='gt',layer=ngLayer(gt,res,tt='segmentation'))

print(viewer)