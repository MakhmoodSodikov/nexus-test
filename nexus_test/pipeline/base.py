from abc import ABC, abstractmethod
from logging import getLogger

logger = getLogger('main logger')


class Pipeline(ABC):

    def __init__(self, preprocessor, ocr, postprocessor):
        self.preprocessor = preprocessor
        self.ocr = ocr
        self.postprocessor = postprocessor

    def __call__(self, data_path: str):
        self.forward(data_path)

    @abstractmethod
    def forward(self, data_path: str) -> str:
        pass
