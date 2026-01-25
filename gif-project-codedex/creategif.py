import imageio.v3 as iio
filenames = ['IMG_6788.jpg', 'IMG_6789.jpg','IMG_6790.jpg', 'IMG_6791.jpg','IMG_6792.jpg', 'IMG_6793.jpg','IMG_6794.jpg', 'IMG_6794.jpg','IMG_6795.jpg', 'IMG_6797.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('dinosaur.gif', images, duration = 400, loop = 2)

