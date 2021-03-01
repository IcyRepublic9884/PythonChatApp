# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/server_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 426)
        stylesheet = open("stylesheet.css", "r")
        MainWindow.setStyleSheet(stylesheet.read())
        stylesheet.close()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 351, 211))
        self.groupBox.setObjectName("groupBox")
        self.port_number_input = QtWidgets.QLineEdit(self.groupBox)
        self.port_number_input.setGeometry(QtCore.QRect(160, 40, 171, 31))
        self.port_number_input.setObjectName("port_number_input")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label_2.setObjectName("label_2")
        self.client_wait_list_edit = QtWidgets.QSpinBox(self.groupBox)
        self.client_wait_list_edit.setGeometry(QtCore.QRect(160, 90, 171, 31))
        self.client_wait_list_edit.setMaximum(100)
        self.client_wait_list_edit.setObjectName("client_wait_list_edit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 121, 31))
        self.label_3.setObjectName("label_3")
        self.buffer_size_edit = QtWidgets.QSpinBox(self.groupBox)
        self.buffer_size_edit.setGeometry(QtCore.QRect(160, 151, 171, 31))
        self.buffer_size_edit.setMinimum(500)
        self.buffer_size_edit.setMaximum(3000)
        self.buffer_size_edit.setObjectName("buffer_size_edit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 541, 371))
        self.groupBox_2.setObjectName("groupBox_2")
        self.client_list_view = QtWidgets.QListView(self.groupBox_2)
        self.client_list_view.setGeometry(QtCore.QRect(10, 30, 521, 331))
        self.client_list_view.setObjectName("client_list_view")
        self.start_server_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_server_button.setGeometry(QtCore.QRect(10, 240, 171, 61))
        self.start_server_button.setObjectName("start_server_button")
        self.clear_clients_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_clients_button.setGeometry(QtCore.QRect(10, 310, 341, 61))
        self.clear_clients_button.setObjectName("clear_clients_button")
        self.stop_server_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_server_button.setGeometry(QtCore.QRect(190, 240, 171, 61))
        self.stop_server_button.setObjectName("stop_server_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 26))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionAboit = QtWidgets.QAction(MainWindow)
        self.actionAboit.setObjectName("actionAboit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFIle.addAction(self.actionExport)
        self.menuHelp.addAction(self.actionAboit)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Configure Server Settings"))
        self.label.setText(_translate("MainWindow", "Port Number"))
        self.label_2.setText(_translate("MainWindow", "Client Wait List"))
        self.label_3.setText(_translate("MainWindow", "Buffer Size (in bytes)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Client List"))
        self.start_server_button.setText(_translate("MainWindow", "Start Server"))
        self.clear_clients_button.setText(_translate("MainWindow", "Clear Client List"))
        self.stop_server_button.setText(_translate("MainWindow", "Stop Server"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionAboit.setText(_translate("MainWindow", "About SimpleChatServer"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

