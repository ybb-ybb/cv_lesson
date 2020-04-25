from skimage import io
import numpy as np

image = io.imread('dog.jpg', as_gray=True)
kernel = np.array(
[
    [1,0,1],
    [0,0,0],
    [1,0,0]
])
Hi, Wi = image.shape
Hk, Wk = kernel.shape
out = np.zeros((Hi, Wi))
pad_H = (Hk - 1) // 2
pad_W = (Wk - 1) // 2
img = np.pad(image, [(pad_H, pad_H), (pad_W, pad_W)], 'constant')
col = np.zeros((Hk,Wk,Hi,Wi))
for y in range(Hk):
    y_max=y+Hi
    for x in range(Wk):
        x_max=x+Wi
        col[y,x,:,:]=img[y:y_max,x:x_max]
col=col.reshape(Hk*Wk,-1)
col_kernel=kernel.reshape(-1)
out=np.dot(col.T,col_kernel).reshape(Hi,-1)
print(out.shape)