from logging import getLogger

import numpy as np

from .base import Preprocessor

logger = getLogger('main logger')


class TessOCRPreprocessor(Preprocessor):

    """
    Class of the baseline image preprocessor for PyTesseract pipeline
    """

    def __init__(self):
        super().__init__()

    def transform(self, image: np.array) -> np.array:
        """
        :param image: cv2 image to be transformed in basic TesseractOCR preprocessing pipeline
        :return: Input image after transforming pipeline
        """
        logger.info('Transforming image')
        image = self.thresholding(self.get_grayscale(image))
        angle_to_rotate = self.get_skew_angle(image)
        rotated_image = self.rotate(
            image, angle_to_rotate, background=(255, 255, 255)
        )
        return rotated_image
