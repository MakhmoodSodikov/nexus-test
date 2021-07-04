import math
from abc import ABC, abstractmethod
from logging import getLogger
from typing import Tuple, Union

import cv2
import numpy as np
from deskew import determine_skew

logger = getLogger('main logger')


class Preprocessor(ABC):

    """
    Abstract class (interface) for any Preprocessor class
    """

    # angle to rotate
    @staticmethod
    def get_skew_angle(image: np.array) -> np.array:
        """
        :param image: The image for which we need to calculate the rotation angle
        :return: Calculated angle for right rotation
        """
        return determine_skew(image)

    # rotation
    @staticmethod
    def rotate(
        image: np.array, angle: float, background: Union[int, Tuple[int, int,
                                                                    int]]
    ) -> np.ndarray:
        """
        :param image: Image to be rotated
        :param angle: Angle to be rotated
        :param background: Background color of empty sides after rotation, white by default
        :return: Rotated image
        """
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
        """
        :param image: Image to be grayscaled
        :return: Grayscaled image
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
    @staticmethod
    def remove_noise(image: np.array) -> np.array:
        """
        :param image: Image to be blurred for noise removal
        :return: Denoised (blurred) image
        """
        return cv2.medianBlur(image, 5)

    # thresholding
    @staticmethod
    def thresholding(image: np.array) -> np.array:
        """
        :param image: Grayscale image to be thresholded
        :return: Thresholded image
        """
        return cv2.threshold(
            image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

    # dilation
    @staticmethod
    def dilate(image: np.array, kernel=(5, 5)) -> np.array:
        """
        :param image: Image to be dilated
        :param kernel: Dilation kernel size
        :return: Dilated image
        """
        if type(kernel) == int:
            kernel = (kernel, kernel)

        kernel = np.ones(kernel, np.uint8)
        return cv2.dilate(image, kernel, iterations=1)

    # erosion
    @staticmethod
    def erode(image: np.array, kernel=(5, 5)) -> np.array:
        """
        :param image: Image to be eroded
        :param kernel: Erosion kernel size
        :return: Eroded image
        """
        if type(kernel) == int:
            kernel = (kernel, kernel)

        kernel = np.ones(kernel, np.uint8)
        return cv2.erode(image, kernel, iterations=1)

    # canny edge detection
    @staticmethod
    def canny(image: np.array, thresh1=100, thresh2=200) -> np.array:
        """
        :param image: Image for canny edges selection
        :param thresh1: Threshold 1
        :param thresh2: Threshold 2
        :return: Cannied image
        """
        return cv2.Canny(image, thresh1, thresh2)

    # skew correction
    @abstractmethod
    def transform(self, image: np.array) -> np.array:
        """
        :param image: Image to be transformed
        :return: Transformed image
        """
        pass


class Postprocessor(ABC):

    """
    Abstract class for any Postprocessor class
    """

    @abstractmethod
    def transform(self, image: np.array) -> np.array:
        """
        :param image: Image to be transformed
        :return: Transformed image
        """
        pass
