# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 538)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.appMenuBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.appMenuBtn.setObjectName("appMenuBtn")
        self.horizontalLayout.addWidget(self.appMenuBtn)
        self.saveImageLibraryBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.saveImageLibraryBtn.setObjectName("saveImageLibraryBtn")
        self.horizontalLayout.addWidget(self.saveImageLibraryBtn)
        self.addClassifyBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.addClassifyBtn.setObjectName("addClassifyBtn")
        self.horizontalLayout.addWidget(self.addClassifyBtn)
        self.removeClassifyBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.removeClassifyBtn.setObjectName("removeClassifyBtn")
        self.horizontalLayout.addWidget(self.removeClassifyBtn)
        self.searchClassifyBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.searchClassifyBtn.setObjectName("searchClassifyBtn")
        self.horizontalLayout.addWidget(self.searchClassifyBtn)
        self.searchClassifyHistoryCmb = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchClassifyHistoryCmb.sizePolicy().hasHeightForWidth())
        self.searchClassifyHistoryCmb.setSizePolicy(sizePolicy)
        self.searchClassifyHistoryCmb.setMinimumSize(QtCore.QSize(200, 0))
        self.searchClassifyHistoryCmb.setMaximumSize(QtCore.QSize(400, 16777215))
        self.searchClassifyHistoryCmb.setBaseSize(QtCore.QSize(400, 0))
        self.searchClassifyHistoryCmb.setEditable(True)
        self.searchClassifyHistoryCmb.setObjectName("searchClassifyHistoryCmb")
        self.horizontalLayout.addWidget(self.searchClassifyHistoryCmb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.classifyListView = QtWidgets.QListView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.classifyListView.sizePolicy().hasHeightForWidth())
        self.classifyListView.setSizePolicy(sizePolicy)
        self.classifyListView.setMinimumSize(QtCore.QSize(200, 0))
        self.classifyListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.classifyListView.setObjectName("classifyListView")
        self.verticalLayout_2.addWidget(self.classifyListView)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addImageBtn = QtWidgets.QToolButton(self.layoutWidget1)
        self.addImageBtn.setObjectName("addImageBtn")
        self.horizontalLayout_2.addWidget(self.addImageBtn)
        self.removeImageBtn = QtWidgets.QToolButton(self.layoutWidget1)
        self.removeImageBtn.setObjectName("removeImageBtn")
        self.horizontalLayout_2.addWidget(self.removeImageBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.imageScaleSlider = QtWidgets.QSlider(self.layoutWidget1)
        self.imageScaleSlider.setMaximumSize(QtCore.QSize(400, 16777215))
        self.imageScaleSlider.setMinimum(1)
        self.imageScaleSlider.setMaximum(8)
        self.imageScaleSlider.setPageStep(2)
        self.imageScaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.imageScaleSlider.setObjectName("imageScaleSlider")
        self.horizontalLayout_2.addWidget(self.imageScaleSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.imageListWidget = QtWidgets.QListWidget(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageListWidget.sizePolicy().hasHeightForWidth())
        self.imageListWidget.setSizePolicy(sizePolicy)
        self.imageListWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.imageListWidget.setStyleSheet("QListWidget::Item:hover{background:skyblue;padding-top:0px; padding-bottom:0px;}\n"
"QListWidget::item:selected{background:rgb(245, 121, 0); color:red;}")
        self.imageListWidget.setObjectName("imageListWidget")
        self.verticalLayout.addWidget(self.imageListWidget)
        self.horizontalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "识图图像库管理"))
        self.appMenuBtn.setText(_translate("MainWindow", "..."))
        self.saveImageLibraryBtn.setText(_translate("MainWindow", "..."))
        self.addClassifyBtn.setText(_translate("MainWindow", "..."))
        self.removeClassifyBtn.setText(_translate("MainWindow", "..."))
        self.searchClassifyBtn.setText(_translate("MainWindow", "..."))
        self.addImageBtn.setText(_translate("MainWindow", "..."))
        self.removeImageBtn.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
