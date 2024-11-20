```markdown
# Image Segmentation Using OpenCV

This project demonstrates basic image segmentation techniques using OpenCV in Python. It applies Otsu's thresholding method and performs basic image cleaning using erosion and dilation.

## Project Overview

The project performs the following steps:

1. **Grayscale Conversion**: Converts the image to grayscale.
2. **Thresholding**: Uses Otsu's method to threshold the image into binary (black and white) form.
3. **Image Cleaning**: Performs erosion and dilation to clean up the thresholded image.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- OpenCV
- Numpy

You can install the required dependencies using `pip`:

```bash
pip install opencv-python numpy
```

## How to Use

1. Place the image (e.g., `apple.jpg`) you want to segment in the same directory as the Python script.
2. Run the script:

```bash
python segmentation.py
```

3. The script will display the following images:
   - **Original Image**: The original image you provided.
   - **Thresholded Image**: The binary image after applying Otsu's thresholding.
   - **Eroded Image**: The image after applying erosion.
   - **Dilated Image**: The image after applying dilation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```