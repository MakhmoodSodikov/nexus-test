from logging import getLogger
import cv2
import numpy as np
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,
                                  PDFSyntaxError)

logger = getLogger('main logger')


def pdf_to_image(path):
    images = None

    try:
        images = convert_from_path(path)
    except PDFSyntaxError as e:
        logger.error('Invalid PDF syntax')
    except PDFPageCountError as e:
        logger.error('Invalid page counter')
    except PDFInfoNotInstalledError as e:
        logger.error('PDF info not installed')

    return images


def pil_to_cv(pil_image):
    return cv2.cvtColor(np.asarray(pil_image), cv2.COLOR_RGB2BGR)
