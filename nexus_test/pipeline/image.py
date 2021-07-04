from logging import getLogger

import cv2

from .base import Pipeline

logger = getLogger('main logger')


class ImagePipeline(Pipeline):

    """
    Implementation of Pipeline container for the basic Pytesseract image recognition pipeline
    """

    def __init__(self, preprocessor, ocr, postprocessor):
        super().__init__(preprocessor, ocr, postprocessor)

    def forward(self, image_path: str) -> list:
        """
        :param image_path: Path to the image to be processed in pipeline
        :return: Recognized text from image file
        """
        img = cv2.imread(image_path)
        preprocessed_image = self.preprocessor.transform(img)
        predicted_text = self.ocr.transform(preprocessed_image)
        processed_text = self.postprocessor.transform(predicted_text)
        return processed_text
