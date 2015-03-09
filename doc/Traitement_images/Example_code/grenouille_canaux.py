from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
im = Image.open('../data/grenouille.jpg') 
rouge, vert, bleu = im.split()
rouge = np.array(rouge)
vert  = np.array(vert)
bleu  = np.array(bleu)

fig = plt.figure(0) # On cree une figure
plt.clf()
ax1 =fig.add_subplot(3,1,1)
plt.imshow(rouge, origin = "upper")
plt.xticks([])
plt.yticks([])
plt.grid()
cbar = plt.colorbar()
cbar.set_label("Pixel value")
plt.ylabel("Rouge")
plt.title("Canaux")
ax2 =  fig.add_subplot(3,1,2)
plt.imshow(vert,  origin = "upper")
plt.xticks([])
plt.yticks([])
plt.grid()
cbar = plt.colorbar()
cbar.set_label("Pixel value")
plt.ylabel("Vert")
ax3 = fig.add_subplot(3,1,3)
plt.imshow(bleu,  origin = "upper")
plt.xticks([])
plt.yticks([])
plt.grid()
cbar = plt.colorbar()
cbar.set_label("Pixel value")
plt.ylabel("Bleu")
plt.show()
