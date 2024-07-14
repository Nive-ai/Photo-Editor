import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt Image Editor')
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 780, 540)

        openButton = QPushButton('Open', self)
        openButton.setGeometry(10, 560, 80, 30)
        openButton.clicked.connect(self.openImage)

        saveButton = QPushButton('Save', self)
        saveButton.setGeometry(100, 560, 80, 30)
        saveButton.clicked.connect(self.saveImage)

        grayButton = QPushButton('Grayscale', self)
        grayButton.setGeometry(190, 560, 80, 30)
        grayButton.clicked.connect(self.toGrayscale)

    def openImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)", options=options)
        if fileName:
            self.image = cv2.imread(fileName)
            self.displayImage()

    def saveImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Image File", "", "PNG Files (*.png);;JPG Files (*.jpg);;BMP Files (*.bmp)", options=options)
        if fileName:
            cv2.imwrite(fileName, self.image)

    def toGrayscale(self):
        if hasattr(self, 'image'):
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.displayImage()

    def displayImage(self):
        qformat = QImage.Format_Indexed8 if len(self.image.shape) == 2 else QImage.Format_RGB888
        img = QImage(self.image.data, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img = img.rgbSwapped() if qformat == QImage.Format_RGB888 else img
        self.label.setPixmap(QPixmap.fromImage(img))
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())
