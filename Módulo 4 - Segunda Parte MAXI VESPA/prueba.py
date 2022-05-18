import numpy as np               #version 1.14.3
import matplotlib.pyplot as plt 
from skimage import io           #scikit image version 0.13.1
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12

def gammma(x, r):
    """
Gamma correction y=255*(x/255) 
x Input image
r Gamma correction coefficient
    """
    x = np.float64(x)
    y = x/255.
    y = y **(1/r)
    return np.uint8(255*y)
# Also create a function to create and display a histogram for each RGB. (Reinventing the wheel ... omitted below)

def hist_rgb(img):
    #Function to create a histogram of rgb
    #The variable res that stores the result[brightness, channel]
    res = np.zeros([256, 3])   
    for channel in range(3):
        #Extract a channel
        img_tmp = img[:,:,channel]
        #Make the image one-dimensional
        img_tmp =img_tmp.reshape(img_tmp.size)
        for i in img_tmp:
            res[i, channel] += 1
    return res

def mat_hist_rgb(hist, ylim = 0.06):
    #hist_Display the histogram calculated by the function of rgb
    x = np.arange(hist.shape[0])
    #Specify the color of the histogram
    colors = ["red", "green", "blue"]
    for i, color in enumerate(colors):
        plt.bar(x,hist[:, i], color=color, alpha=0.3, width=1.0)
    plt.xlabel("Brightness")
    plt.ylabel("Frequency")
    plt.xlim(0, 255)
    plt.yticks([])
    plt.show()
img_lena = io.imread("bote.jpg")
hist_lena = hist_rgb(img_lena)
mat_hist_rgb(hist_lena)
img_gamma = gammma(img_lena, r=2.0) ### aca le podes cambiar el valor del gamma en el r=
io.imsave("r05.png ", img_gamma)
mat_hist_rgb(hist_rgb(img_gamma))
