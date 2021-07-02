from abc import ABC, abstractmethod
import numpy as np


class OCR(ABC):

    @abstractmethod
    def transform(self, image: np.array) -> str:
        pass
