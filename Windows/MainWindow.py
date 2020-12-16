#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging
log = logging.getLogger(__name__)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QStyle, QStyleFactory, QStatusBar)
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow, QPalette):

    def __init__(self, title):
        super().__init__()

        log.info("Initializing " + title + " window")
        self.setWindowTitle(title)

        self.mainLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.initUI()

        self.setMinimumSize(self.sizeHint())
        self.center()

    def center(self):
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, self.size(), QDesktopWidget().availableGeometry()))

    def setSize(self, size=None):
        if size is None:
            size = self.sizeHint()
        self.setMinimumSize(size)
        self.center()

    def initUI(self):
        """ To implement in child """
        return

    @staticmethod
    def setAppStyle(app):
        if "Fusion" in [st for st in QStyleFactory.keys()]:
            app.setStyle(QStyleFactory.create("Fusion"))
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)

            app.setPalette(dark_palette)
            app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        elif sys.platform == "win32":
            app.setStyle(QStyleFactory.create("WindowsVista"))
        elif sys.platform == "linux":
            app.setStyle(QStyleFactory.create("gtk"))
        elif sys.platform == "darwin":
            app.setStyle(QStyleFactory.create("macintosh"))