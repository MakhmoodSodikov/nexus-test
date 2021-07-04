from abc import ABC, abstractmethod

import numpy as np


class OCR(ABC):

    """
    Inteface (abstract method) for OCR models
    """

    @abstractmethod
    def transform(self, image: np.array) -> str:
        """
        :param image: Image to be recognized
        :return: Recognized text by OCR model
        """
        pass
