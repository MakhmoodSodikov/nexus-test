from logging import getLogger

import regex as re

from .base import Postprocessor

logger = getLogger('main logger')


class TessOCRPostprocessor(Postprocessor):

    """
    Class of the baseline image postprocessor for PyTesseract pipeline
    """

    def __init__(self):
        super().__init__()

    def transform(self, text: str) -> str:
        """
        :param text: Text to be postprocessed
        :return: Postprocessed (denoised) text
        """
        denoised_text = self._redundant_symbols_deleter(text)
        return denoised_text

    @staticmethod
    def _redundant_symbols_deleter(text, filler='.....', tab='\n') -> list:
        """
        :param text: Text to be cleaned of redundant symbols
        :param filler: Replacement for noisy word, by default equals to dots
        :param tab: Tab symbol, e.g. could be empty string or \n, by default equals to \n
        :return: Returns text cleaned from redundant symbols

        Notion: rx variable is the regular expression for finding group of utterances with 3 or more repeating symbols
                It can be "thresholded" by changing parameter in curly brackets
        """

        rx = re.compile(r'(.)\1{2,}')

        logger.info('Deleting redundant symbols')

        new_text = []

        for line in text.split('\n'):
            new_line = []

            for word in line.split(' '):
                if word != '':
                    if not rx.search(word):
                        new_line.append(word)
                    else:
                        new_line.append(filler)
                else:
                    new_line.append(tab)
            new_line.append('\n')
            new_text.append(' '.join(new_line))

        return new_text
