import logging

import click
from exceptions.image import InputFormatError
from ocr_engine.pytess import PyTesseractOCR
from pipeline.image import ImagePipeline
from pipeline.pdf import PDFPipeline
from transforms.postprocessing import PostProcessor
from transforms.preprocessing import TessOCRPreprocessor
from utils.constants import (LOGGER_NAME, SUPPORTED_EXTENSIONS,
                             SUPPORTED_FILE_EXTENSIONS,
                             SUPPORTED_IMG_EXTENSIONS)
from utils.other import get_extension, write_lines_to_file

logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.INFO)

logger.info("Starting new session")


@click.command()
@click.option('--input_path', help='Input file path', required=True)
@click.option('--output_path', help='Output file path', required=True)
@click.option('--verbose', help='Verbose mode')
def main(output_path, input_path, verbose):
    input_extension = get_extension(input_path)
    print(input_path)
    print(input_extension)
    if input_extension not in SUPPORTED_EXTENSIONS:
        raise InputFormatError

    logger.info("Checked extension")

    if not verbose:
        logging.basicConfig(
            filename='logs.txt',
            format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    preprocessor = TessOCRPreprocessor()
    ocr = PyTesseractOCR()
    postprocessor = PostProcessor()
    pipe = None
    logger.info("Created processors")

    if input_extension in SUPPORTED_IMG_EXTENSIONS:
        pipe = ImagePipeline(preprocessor, ocr, postprocessor)

    if input_extension in SUPPORTED_FILE_EXTENSIONS:
        pipe = PDFPipeline(preprocessor, ocr, postprocessor)
    logger.info("Pipeline selected")

    data = pipe.forward(input_path)
    logger.info("Pipeline forward")

    write_lines_to_file(data, output_path)
    logger.info("Writing to the output file...")
    logger.info("DONE!")


if __name__ == '__main__':
    main()
