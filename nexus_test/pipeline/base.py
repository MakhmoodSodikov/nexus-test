from abc import ABC, abstractmethod
from logging import getLogger

logger = getLogger('main logger')


class Pipeline(ABC):

    """
    Implementation of Pipeline interface.
    """

    def __init__(self, preprocessor, ocr, postprocessor):
        """
        :param preprocessor: Preprocessor class for raw images and other files preprocessing,
                             should inherit Preprocessor interface
        :param ocr: OCR-engine class to recognize characters from input file,
                    should inherit OCR interface
        :param postprocessor: PostProcessor,

        """
        self.preprocessor = preprocessor
        self.ocr = ocr
        self.postprocessor = postprocessor

    def __call__(self, data_path: str):
        self.forward(data_path)

    @abstractmethod
    def forward(self, data_path: str) -> str:
        pass
