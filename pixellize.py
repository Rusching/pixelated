import cv2
import numpy as np

def close_multi_inc(num, base):
    # return the difference from input num and its closest multiple of base
    # for example, input 4, 3, output 2 becase 4 + 2 = 6 is 2 times 3

    assert num > 0
    if num % base == 0:
        return 0
    else:
        return base - num % base


def resize_image(origin_image, base):
    # first read the height, then width
    height, width, _ = origin_image.shape

    # only pad top and right
    top_pad = close_multi_inc(height, base)
    right_pad = close_multi_inc(width, base)
    pad_image = cv2.copyMakeBorder(origin_image, top_pad, 0, 0, right_pad, cv2.BORDER_CONSTANT)
    return pad_image


def down_sampling(input_image, base):
    height, width, dim = input_image.shape
    
    row_iters = int(height / base)
    col_iters = int(width / base)
    

    small_image = np.zeros((row_iters, col_iters, dim))
    for i in range(row_iters):
        for j in range(col_iters):
            small_rigid = input_image[i * base: (i + 1) * base - 1, j * base: (j + 1) * base - 1]
            small_image[i][j][0] = np.max(small_rigid[:,:,0])
            small_image[i][j][1] = np.max(small_rigid[:,:,1])
            small_image[i][j][2] = np.max(small_rigid[:,:,2])
    
    return small_image


def perform_compress(input_image, base):
    return


image1 = cv2.imread("7.png")
canny = cv2.imread("canny.png", cv2.IMREAD_GRAYSCALE)
print(image1.shape)
height, width, dim = image1.shape
# for i in range(height):
    # for j in range(width):
        # if canny


# base = 3
# pad_image = resize_image(image1, base)
# small_image = down_sampling(pad_image, base)
# cv2.imwrite('7.png', small_image)




