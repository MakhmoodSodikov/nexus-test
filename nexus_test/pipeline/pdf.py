from .base import Pipeline
from logging import getLogger
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,
                                  PDFSyntaxError)


logger = getLogger('main logger')


class PDFPipeline(Pipeline):

    def __init__(self, preprocessor, ocr, postprocessor):
        super().__init__(preprocessor, ocr, postprocessor)


    @staticmethod
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

    def forward(self, pdf_path: str) -> list:
        logger.info('PDF Pipeline forwarding')
        text = []
        images = self.pdf_to_image(pdf_path)

        for image in images:
            text.append(self.ocr.transform(image))
            
        return text
