import struct as st
import numpy as np
import matplotlib.pyplot as plt

# Open the IDX file in readable binary mode
filename = {'images' : 'Artificial-Intelligence/Computer Vision projects/digit recognizer/data/train-images.idx3-ubyte' ,'labels' : 'Artificial-Intelligence/Computer Vision projects/digit recognizer/data/train-labels.idx1-ubyte'}
train_imagesfile = open(filename['images'],'rb')

# Read the magic number
train_imagesfile.seek(0)
magic = st.unpack('>4B',train_imagesfile.read(4))

# Read the dimensions of the Image data-set
num_img = st.unpack('>I',train_imagesfile.read(4))[0] #num of images
num_rows = st.unpack('>I',train_imagesfile.read(4))[0] #num of rows
num_col = st.unpack('>I',train_imagesfile.read(4))[0] #num of column

print(magic,num_img,num_col,num_rows)

# Declare Image NumPy array
# images_array = np.zeros((num_img,num_rows,num_col))

# Reading the Image data
nBytesTotal = num_img*num_rows*num_col*1 #since each pixel data is 1 byte
images_array = np.asarray(st.unpack('>'+'B'*nBytesTotal,train_imagesfile.read(nBytesTotal))).reshape((num_img,num_rows,num_col))
print(images_array.shape)
plt.imshow(images_array[1:3],cmap='gray')
plt.show()
