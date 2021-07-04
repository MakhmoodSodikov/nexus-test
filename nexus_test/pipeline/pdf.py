from logging import getLogger

from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,
                                  PDFSyntaxError)

from .base import Pipeline

logger = getLogger('main logger')


class PDFPipeline(Pipeline):

    """
    Implementation of Pipeline container for the basic Pytesseract PDF recognition pipeline
    """

    def __init__(self, preprocessor, ocr, postprocessor):
        """
        :param preprocessor: Implemented Preprocessor to be used in PDF pipeline
        :param ocr: Implemented OCR-engine to be used in PDF pipeline
        :param postprocessor: Implemented text Postprocessor to be used in PDF pipeline
        """
        super().__init__(preprocessor, ocr, postprocessor)

    @staticmethod
    def pdf_to_image(path: str) -> list:
        """
        :param path: Path to the pdf-file to be converted to cv2 images list
        :return: Images list
        """
        images = []

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
        """
        :param pdf_path: Path to the pdf-file to be processed in pipeline
        :return: Recognized text from pdf file
        """
        logger.info('PDF Pipeline forwarding')
        text = []
        images = self.pdf_to_image(pdf_path)
        logger.info(f'Received {len(images)} images from PDF sheets')

        for i, image in enumerate(images):
            logger.info(f'Processing image {i} of {len(images)} ')
            text.append(self.ocr.transform(image))
        logger.info('PDF Pipeline is done')
        return text
