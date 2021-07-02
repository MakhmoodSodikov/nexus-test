from logging import getLogger

import cv2

from .base import Pipeline

logger = getLogger('main logger')


class ImagePipeline(Pipeline):

    def __init__(self, preprocessor, ocr, postprocessor):
        super().__init__(preprocessor, ocr, postprocessor)

    def forward(self, image_path: str) -> list:
        text = []
        img = cv2.imread(image_path)
        preprocessed_image = self.preprocessor.transform(img)
        text.append(self.ocr.transform(preprocessed_image))
        return text
