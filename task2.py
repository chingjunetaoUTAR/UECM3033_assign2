import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

# new picture Tree.tiff
img = mpimg.imread('tree.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.savefig('img.png')
plt.show()


#Decompose Red matrix by using SVD
Red_U, TempRed_S, Red_V = np.linalg.svd(r, full_matrices = True, compute_uv = True)

#Decompose Green matrix by using SVD
Green_U, TempGreen_S, Green_V = np.linalg.svd(g, full_matrices = True, compute_uv = True)

#Decompose Blue matrix by using SVD
Blue_U, TempBlue_S, Blue_V = np.linalg.svd(b, full_matrices = True, compute_uv = True)

# convert Sigma from vector to diagonal matrix
Red_S = np.zeros((800,1000))
Green_S = np.zeros((800,1000))
Blue_S = np.zeros((800,1000))

for i in range(800):
    Red_S[i][i] = TempRed_S[i]
    Green_S[i][i] = TempGreen_S[i]
    Blue_S[i][i] = TempBlue_S[i]

#create new image with lower resolution
Red_S_30 = np.zeros((800,1000))
Green_S_30 = np.zeros((800,1000))
Blue_S_30 = np.zeros((800,1000))

for i in range(30):
    Red_S_30[i][i] = Red_S[i][i]
    Green_S_30[i][i] = Green_S[i][i]
    Blue_S_30[i][i] = Blue_S[i][i]
    
#combine USV to single matrix
Red_30 = np.asmatrix(Red_U)* np.asmatrix(Red_S_30)*np.asmatrix(Red_V)
Green_30 = np.asmatrix(Green_U)* np.asmatrix(Green_S_30)*np.asmatrix(Green_V)
Blue_30 = np.asmatrix(Blue_U)* np.asmatrix(Blue_S_30)*np.asmatrix(Blue_V)    

#combine new RGB into new image
img_new = img
img_new[:,:,0] = Red_30
img_new[:,:,1] = Green_30
img_new[:,:,2] = Blue_30

#create new plot
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img_new)
ax2.imshow(Red_30, cmap = 'Reds')
ax3.imshow(Green_30, cmap = 'Greens')
ax4.imshow(Blue_30, cmap = 'Blues')
plt.savefig('new_img.png')

#save the new image
img_new2 = Image.fromarray(img_new,'RGB')
img_new2.save('lowResolution_Tree.jpg')
        
