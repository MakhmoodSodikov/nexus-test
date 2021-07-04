import time
from logging import getLogger

import numpy as np
import pytesseract

from .base import OCR

logger = getLogger('main logger')


class PyTesseractOCR(OCR):

    """
    Basic PyTesseract OCR engine
    """

    def transform(self, image: np.array) -> str:
        """
        :param image: Image to be recognized
        :return: Recognized text by OCR model
        """
        start = time.time()
        logger.info(f'OCR started...')
        text = pytesseract.image_to_string(image)
        end = time.time()
        logger.info(f'OCR done!')
        timedelta = end - start
        logger.info(f'OCR took {timedelta:.2f} sec.')
        return text
