import regex as re
from logging import getLogger
logger = getLogger('main logger')


class PostProcessor:
    def __init__(self):
        pass

    def forward(self, text):
        denoised_text = self.redundant_symbols_deleter(text)
        return denoised_text

    @staticmethod
    def redundant_symbols_deleter(text, filler='.....') -> list:
        logger.info('Deleting redundant symbols')
        splitted_text = text.split('\n')
        new_text = []
        # regexp for finding couple of repeating symbols
        # it can be "thresholded" by changing parameter in curly brackets
        rx = re.compile(r'(.)\1{2,}')

        for line in splitted_text:
            new_line = []
            for word in line.split(' '):
                if not rx.search(word):
                    new_line.append(word)
                else:
                    new_line.append(filler)
            new_text.append(' '.join(new_line))

        return new_text
