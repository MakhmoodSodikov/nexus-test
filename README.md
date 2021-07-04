# PyTesseract OCR Library

This library implements command-line tool for extracting text from images and pdf-files.

This library accepts following input formats:

* PNG
* JPG, JPEG
* PDF

### Quick report:


The quality of the work on the example pdf was very high. This is so because the conversion to image from pdf is done in high resolution.

However, the final model response depends very much on the DPI of the original image. 

However, the pipelining involving the postprocessing of the Tesseract model response has been greatly improved. Contextual screening of repeating characters was used for postprocessing.

Different transformation hypotheses for preprocessing were tested, but sequential thresholding and grayscaling proved to be the best. Too complex preprocessing degrades the quality of the algorithm.

I noticed unique symbols in the pdf file, like diamonds or spades. On these, the behavior of the model is random, as it does not support additional symbols. 

### Further improvement of the project

I designed the architecture of the project so that I could easily replace the components of the current solution. 

Thus, I would suggest changing the model itself (instead of tesseract use another better model, e.g. pretrained CRNN).

### Installation

To install run these commands in root directory:

* `git clone https://github.com/MakhmoodSodikov/nexus-test.git`
* `pip install poetry`
* `cd nexus-test`
* `poetry shell`
* `poetry add pyproject.toml`

### Usage

From main directory run 

`python nexus_test/main.py --input_path='input/path.jpg' --output_path='output/path'`

If you want verbosed logging, use `--verbose` flag.


