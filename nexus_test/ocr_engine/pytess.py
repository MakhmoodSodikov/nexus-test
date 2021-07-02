import time
from logging import getLogger

import numpy as np
import pytesseract

from .base import OCR

logger = getLogger('main logger')


class PyTesseractOCR(OCR):

    def transform(self, image: np.array) -> str:
        start = time.time()
        logger.info(f'OCR started at {start}...')
        text = pytesseract.image_to_string(image)
        end = time.time()
        logger.info(f'OCR done at {end}...')
        timedelta = end - start
        logger.info(f'OCR took {timedelta} sec.')
        return text
