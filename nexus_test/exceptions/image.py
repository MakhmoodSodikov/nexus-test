import os
from logging import getLogger

logger = getLogger('main logger')


class EmptyImageError(Exception):

    """
    Exception raised for errors with empty image.

    Attributes:
    image_path -- path to the image which is empty and caused the error
    """

    def __init__(self, image_path):
        self.path = image_path
        message = f"Input image at {self.path} is empty and can not be opened or processed."
        logger.error(message)
        super().__init__(message)


class InputFormatError(Exception):

    """
    Exception raised for errors with empty image.

    Attributes:
    image_path -- path to the image which is empty and caused the error
    """

    def __init__(self, image_path):
        self.path = image_path
        image_format = os.path.splitext(image_path)[1]
        message = f"Input image at {self.path} wrong format. Should be .pdf/.png/.jpg/.jpeg but {image_format} found."
        logger.error(message)
        super().__init__(message)
