import numpy as np
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation



def RGB_convolve(im1, kern):
    im2 = np.empty_like(im1)
    for dim in range(im1.shape[-1]):  # loop over rgb channels
        im2[:, :, dim] = sp.signal.convolve2d(im_data[:, :, dim],
                                              kern,
                                              mode="same",
                                              boundary="symm")
    return im2

plt.rcParams["figure.figsize"] = (12, 7)

FNAME = "coronary1.jpg"

KERNELS = {"Edge Detection 3x3": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
           "Sharpen 3x3": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
            "Blur": np.array([[0.0625,0.125,0.0625], [0.125,0.25,0.125], [0.0625, 0.125,0.0625]]),
            "BottomSobel": np.array([[-1,-2,-1],[0,0,0],[1,2,1]])}

# kernel_name = "Sharpen 3x3"
# kernel_name = "Edge Detection 3x3"
kernel_name = "Edge Detection 3x3"
kernel = KERNELS[kernel_name]

im_data = plt.imread(FNAME)
# im_data = plt.imread(FNAME)
im_filtered = RGB_convolve(im_data, kernel)
# im_filtered[:, :, -1] = 1

# im_display = np.copy(im_data)

# im_filtered[:,:,:-1] -= np.min(np.sum(im_filtered[:,:,:-1], axis = 2))

# Normalise to white
# im_filtered[:,:,:-1] -= np.min(im_filtered[:,:,:-1])
# im_filtered[:,:,:-1] /= 1/3 * np.max(np.sum(im_filtered[:,:,:-1], axis = 2))

# Normalise to individual RGB

# im_filtered[:,:,:-1] -= np.min(im_filtered[:,:,:-1])
# im_filtered[:,:,:-1] /= np.max(im_filtered[:,:,:-1])

fig, (axL, axR) = plt.subplots(ncols=2, constrained_layout=True)
fig.suptitle(kernel_name)

plt.imshow((im_data * 255).astype(np.uint8))
plt.imshow(im_filtered)



# indices = list(it.product(
#     range(im_filtered.shape[0]), range(im_filtered.shape[1])))

# Ninc = np.int(len(indices) / (FTOTAL))  # increment


# def init_plot():
#     # imR.set_data(im_data)
#     return (imL,imR)


# def update_plot(frame):
#     for i in range(frame, frame + Ninc):
#         if i >= len(indices):
#             break
#         idx_x, idx_y = indices[i]
#         im_display[idx_x, idx_y, :] = im_filtered[idx_x, idx_y, :]

#     imR.set_data(im_display)
#     return (imR,)


# if __name__ == "__main__":

#     ani = FuncAnimation(fig, func=update_plot, init_func=init_plot, interval=1000/FPS,
#                         frames=range(0, len(indices), Ninc), repeat=False, blit=True)
#     plt.show()