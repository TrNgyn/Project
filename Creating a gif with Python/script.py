import imageio.v3 as iio
import os 

# Define the folder path and the filenames
folder_path = r'C:\Users\ntmt1\OneDrive\Máy tính\Project\Creating a gif with Python'
filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []

# Load the images
for filename in filenames:
    images.append(iio.imread(os.path.join(folder_path,filename)))

# Create the gif and stored the gif inside the original folder
gif_path = os.path.join(folder_path, 'nyan_cat.gif')
iio.imwrite(gif_path, images, duration=500, loop = 0)
