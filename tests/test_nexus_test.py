import cv2
from PIL import Image

from nexus_test import __version__
from nexus_test.transforms.base import Preprocessor
from nexus_test.transforms.preprocessing import TessOCRPreprocessor


def test_version():
    assert __version__ == '0.1.0'


def smoke_preprocessor():
    image_path = '/Users/makhmood/PycharmProjects/nexus-test/nexus_test/samples/82251504.png'
    img = cv2.imread(image_path)
    pipe = TessOCRPreprocessor()

    assert pipe.canny(img) is not None
    assert pipe.dilate(img) is not None
    assert pipe.erode(img) is not None
    assert pipe.get_grayscale(img) is not None


smoke_preprocessor()
