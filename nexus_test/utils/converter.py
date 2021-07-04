from logging import getLogger

import cv2
import numpy as np
import PIL
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,
                                  PDFSyntaxError)

logger = getLogger('main logger')


def pdf_to_image(path: str) -> list:
    """
    :param path: Path to the pdf file
    :return: list of np.array images
    """
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


def pil_to_cv(pil_image: PIL.Image):
    """
    :param pil_image: Image in PIL Image format
    :return: cv2 image format (np.array)
    """
    return cv2.cvtColor(np.asarray(pil_image), cv2.COLOR_RGB2BGR)
