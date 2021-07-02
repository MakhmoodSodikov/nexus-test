import cv2
import matplotlib.pyplot as plt



def display(im_path: str) -> None:
    """
    :param im_path: Path of the input image to be displayed
    :return: Inline image in Jupyter Notebook with actual size
    """

    dpi = 80
    im_data = plt.imread(im_path)

    height, width = im_data.shape[:2]

    figsize = width / float(dpi), height / float(dpi)

    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    ax.axis('off')

    ax.imshow(im_data, cmap='gray')

    plt.show()


def black_and_white(img):
    """
    :param img: Image (PIL Image object) to be transformed into B2W
    :return: Black-and-white image
    """
    inverted_image = cv2.bitwise_not(img)
    return inverted_image
