import math
from abc import ABC, abstractmethod
from logging import getLogger
from typing import Tuple, Union

import cv2
import numpy as np
from deskew import determine_skew

logger = getLogger('main logger')


class Preprocessor(ABC):

    # angle to rotate
    @staticmethod
    def get_skew_angle(image: np.array) -> np.array:
        return determine_skew(image)

    # rotation
    @staticmethod
    def rotate(
        image: np.array, angle: float, background: Union[int, Tuple[int, int,
                                                                    int]]
    ) -> np.ndarray:
        old_width, old_height = image.shape[:2]
        angle_radian = math.radians(angle)
        width = abs(np.sin(angle_radian) * old_height
                    ) + abs(np.cos(angle_radian) * old_width)
        height = abs(np.sin(angle_radian) * old_width
                     ) + abs(np.cos(angle_radian) * old_height)
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        rot_mat[1, 2] += (width-old_width) / 2
        rot_mat[0, 2] += (height-old_height) / 2
        return cv2.warpAffine(
            image, rot_mat, (int(round(height)), int(round(width))),
            borderValue=background
        )

    # get grayscale image
    @staticmethod
    def get_grayscale(image: np.array) -> np.array:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
    @staticmethod
    def remove_noise(image: np.array) -> np.array:
        return cv2.medianBlur(image, 5)

    # thresholding
    @staticmethod
    def thresholding(image: np.array) -> np.array:
        return cv2.threshold(
            image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

    # dilation
    @staticmethod
    def dilate(image: np.array, kernel=(5, 5)) -> np.array:

        if type(kernel) == int:
            kernel = (kernel, kernel)

        kernel = np.ones(kernel, np.uint8)
        return cv2.dilate(image, kernel, iterations=1)

    # erosion
    @staticmethod
    def erode(image: np.array, kernel=(5, 5)) -> np.array:

        if type(kernel) == int:
            kernel = (kernel, kernel)

        kernel = np.ones(kernel, np.uint8)
        return cv2.erode(image, kernel, iterations=1)

    # canny edge detection
    @staticmethod
    def canny(image: np.array, thresh1=100, thresh2=200) -> np.array:
        return cv2.Canny(image, thresh1, thresh2)

    # skew correction
    @abstractmethod
    def transform(self, image: np.array) -> np.array:
        pass
