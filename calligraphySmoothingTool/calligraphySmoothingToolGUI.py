import sys
import math
import cv2
import os
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from calligraphySmoothingTool.smoothmanuallymainwindow import Ui_MainWindow

from utils.Functions import getContourOfImage, removeBreakPointsOfContour, \
                            sortPointsOnContourOfImage, fitCurve, draw_cubic_bezier
from utils.contours_smoothed_algorithm import autoSmoothContoursOfCharacter


class SmoothManuallyGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(SmoothManuallyGUI, self).__init__()
        self.setupUi(self)

        # init GUI
        self.scene = GraphicsScene()
        self.scene.setBackgroundBrush(Qt.gray)
        self.contour_gview.setScene(self.scene)

        self.image_pix = QPixmap()
        self.temp_image_pix = QPixmap()

        self.contour_pix = QPixmap()
        self.temp_contour_pix = QPixmap()

        # data
        self.image_path = ""
        self.image_name = ""

        self.feature_points = []
        self.contour_segmentations = []
        self.smoothed_contour_points = []

        self.image_gray = None
        self.contour_gray = None

        # add listener
        self.open_btn.clicked.connect(self.openBtn)
        self.clear_btn.clicked.connect(self.clearBtn)
        self.contour_btn.clicked.connect(self.contourBtn)
        self.smooth_btn.clicked.connect(self.smoothBtn)
        self.autosmooth_btn.clicked.connect(self.autoSmoothBtn)
        self.save_btn.clicked.connect(self.saveBtn)
        self.exit_btn.clicked.connect(self.exitBtn)

    def openBtn(self):
        """
        Open button clicked!
        :return:
        """
        print("Open button clicked!")
        self.scene.clear()

        filename, _ = QFileDialog.getOpenFileName(None, "Open file", QDir.currentPath())
        if filename:
            # image file path and name
            self.image_path = filename
            self.image_name = os.path.splitext(os.path.basename(filename))[0]

            qimage = QImage(filename)
            if qimage.isNull():
                QMessageBox.information(self, "Image viewer", "Cannot not load %s." % filename)
                return
            # grayscale image
            img_ = cv2.imread(filename, 0)
            _, img_ = cv2.threshold(img_, 127, 255, cv2.THRESH_BINARY)
            self.image_gray = img_.copy()

            self.image_pix = QPixmap.fromImage(qimage)
            self.temp_image_pix = self.image_pix.copy()
            self.scene.addPixmap(self.image_pix)
            self.scene.update()
            self.statusbar.showMessage("Open image %s successed!" % self.image_name)

            # clean
            del img_, qimage

    def clearBtn(self):
        """
        Clear button clicked
        :return:
        """
        print("Clear button clicked")
        # clean data
        self.scene.points = []

        self.scene.addPixmap(self.image_pix)
        self.scene.update()
        self.statusbar.showMessage("Clear successed!")

    def contourBtn(self):
        """
        Obtain the contour of image
        :return:
        """
        print("Contour button clicked")
        contour_ = getContourOfImage(self.image_gray)

        # remove the break points
        contour_ = removeBreakPointsOfContour(contour_)

        self.contour_gray = contour_.copy()
        qimg = QImage(contour_.data, contour_.shape[1], contour_.shape[0], contour_.shape[1], QImage.Format_Indexed8)

        self.contour_pix = QPixmap.fromImage(qimg)
        self.temp_contour_pix = self.contour_pix.copy()
        self.scene.addPixmap(self.contour_pix)
        self.scene.update()
        self.statusbar.showMessage("Contour successed!")
        del contour_, qimg

    def smoothBtn(self):
        """
        Smooth button clicked!
        :return:
        """
        print("Smooth button clicked")
        if self.scene.points is None or len(self.scene.points) == 0:
            return
        # max Error
        max_error = int(self.maxerror_ledit.text())

        # new contour image
        contour_img = np.array(np.ones_like(self.contour_gray) * 255, dtype=np.uint8)

        # smooth the contour segmentations.
        contour_sorted = sortPointsOnContourOfImage(self.contour_gray.copy())

        feature_points = []
        for pt in self.scene.points:
            nearest_pt = None
            max_dist = 1000000
            for cpt in contour_sorted:
                dist_ = math.sqrt((pt[0]-cpt[0])**2 + (pt[1]-cpt[1])**2)
                if dist_ < max_dist:
                    max_dist = dist_
                    nearest_pt = cpt
            # select feature points
            feature_points.append(nearest_pt)
        # add first point as the last end point
        feature_points.append(feature_points[0])
        print(self.scene.points)
        print(feature_points)

        self.feature_points = feature_points.copy()

        # extract segmentations based on the feature points
        contour_segmentations = []
        for id in range(len(feature_points)-1):
            start_pt = feature_points[id]
            end_pt = feature_points[id+1]

            start_index = contour_sorted.index(start_pt)
            end_index = contour_sorted.index(end_pt)

            if start_index < end_index:
                segmentation = contour_sorted[start_index: end_index]
                if end_index == len(contour_sorted)-1:
                    segmentation.append(contour_sorted[0])
                else:
                    segmentation.append(contour_sorted[end_index+1])
            elif start_index >= end_index:
                segmentation = contour_sorted[start_index: len(contour_sorted)] + contour_sorted[0: end_index+1]

            contour_segmentations.append(segmentation)
        print("contour segmentation len: %d" % len(contour_segmentations))
        self.contour_segmentations = contour_segmentations.copy()

        # smooth contour segmentations
        smoothed_contour_points = []
        for id in range(len(self.contour_segmentations)):
            print("Line index: %d" % id)

            # smooth contour segmentation
            li_seg = np.array(self.contour_segmentations[id])

            beziers = fitCurve(li_seg, maxError=max_error)

            for bez in beziers:
                bezier_points = draw_cubic_bezier(bez[0], bez[1], bez[2], bez[3])

                for id in range(len(bezier_points) - 1):
                    start_pt = bezier_points[id]
                    end_pt = bezier_points[id+1]
                    cv2.line(contour_img, start_pt, end_pt, color=0, thickness=1)
                smoothed_contour_points += bezier_points

        qimg = QImage(contour_img.data, contour_img.shape[1], contour_img.shape[0], contour_img.shape[1], \
                      QImage.Format_Indexed8)

        contour_pix = QPixmap.fromImage(qimg)

        self.scene.addPixmap(contour_pix)
        self.scene.update()

        # clean data
        self.scene.points = []
        self.contour_gray = contour_img.copy()
        self.smoothed_contour_points = smoothed_contour_points.copy()

        # update status bar
        self.statusbar.showMessage("Smooth successed!")
        del contour_img, contour_pix, contour_segmentations, contour_sorted, smoothed_contour_points, \
            qimg, feature_points

    def autoSmoothBtn(self):
        """
        Auto-smooth button clicked
        :return:
        """
        print("Auto-smooth button clicked")

        # RDP eplison
        rdp_eplison = float(self.epsilon_ledit_2.text())
        # max Error
        max_error = float(self.maxerror_ledit.text())

        img_gray = self.image_gray.copy()

        img_smoothed = autoSmoothContoursOfCharacter(img_gray, bitmap_threshold=127, eplison=rdp_eplison, \
                                                     max_error=max_error)
        qimg = QImage(img_smoothed.data, img_smoothed.shape[1], img_smoothed.shape[0], img_smoothed.shape[1], \
                      QImage.Format_Indexed8)

        contour_pix = QPixmap.fromImage(qimg)

        self.scene.addPixmap(contour_pix)
        self.scene.update()

        self.contour_gray = img_smoothed.copy()
        self.statusbar.showMessage("Smooth successed!")

        del img_gray, contour_pix, img_smoothed, qimg

    def saveBtn(self):
        """
        Save button
        :return:
        """
        print("Save button clicked")

        # contour image
        contour_img = self.contour_gray.copy()

        # fill the contour with black color
        # smoothed_contour_points = self.smoothed_contour_points.copy()
        # smoothed_contour_points = np.array([smoothed_contour_points], "int32")
        #
        # fill_contour_smooth = np.ones(contour_img.shape) * 255
        # fill_contour_smooth = np.array(fill_contour_smooth, dtype=np.uint8)
        # fill_contour_smooth = cv2.fillPoly(fill_contour_smooth, smoothed_contour_points, 0)

        # save path
        fileName, _ = QFileDialog.getSaveFileName(self, "save file", QDir.currentPath())
        cv2.imwrite(fileName, contour_img)

        self.statusbar.showMessage("Save image successed!")

        del contour_img
        # del smoothed_contour_points
        # del fill_contour_smooth

    def exitBtn(self):
        """
        Exit
        :return:
        """
        qApp = QApplication.instance()
        sys.exit(qApp.exec_())


class GraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        # usually the points are sorted by user.
        self.points = []

    def setOption(self, opt):
        self.opt = opt

    def mousePressEvent(self, event):
        """
        Mouse press clicked!
        :param event:
        :return:
        """
        pen = QPen(Qt.red)
        brush = QBrush(Qt.red)

        x = event.scenePos().x()
        y = event.scenePos().y()

        # add point
        self.addEllipse(x, y, 3, 3, pen, brush)

        self.points.append((x, y))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = SmoothManuallyGUI()
    mainWindow.show()
    sys.exit(app.exec_())