# Photo-Editor

## Overview

This is a basic image editor built using PyQt and OpenCV. The application provides a simple interface to perform basic image editing tasks such as loading images, applying filters, and saving the edited images.

## Features

- Load images from your filesystem
- Display images using a PyQt interface
- Apply basic image processing operations (e.g., grayscale, blur, edge detection)
- Save edited images

## Requirements

- Python 3.6+
- PyQt5
- OpenCV

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/pyqt-image-editor.git
    cd pyqt-image-editor
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Load an image:**
    - Use the "Open" button to load an image from your filesystem.

3. **Apply filters:**
    - Use the provided buttons or menu options to apply various filters and image processing operations.

4. **Save the edited image:**
    - Use the "Save" button to save your edited image.

## Folder Structure
pyqt-image-editor/
│
├── main.py # Main application file
├── requirements.txt # List of required packages
├── README.md # This readme file
├── images/ # Sample images
└── src/
├── ui/ # UI-related files
└── utils/ # Utility functions and modules


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License



## Acknowledgements

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [OpenCV Documentation](https://docs.opencv.org/)

