# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/client_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    # TODO: Init the client
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 387)
        stylesheet = open("stylesheet.css", "r")
        MainWindow.setStyleSheet(stylesheet.read())
        stylesheet.close()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 401, 331))
        self.groupBox.setObjectName("groupBox")
        self.incoming_message_view = QtWidgets.QListView(self.groupBox)
        self.incoming_message_view.setGeometry(QtCore.QRect(10, 30, 381, 291))
        self.incoming_message_view.setObjectName("incoming_message_view")
        self.send_message_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_btn.setGeometry(QtCore.QRect(550, 260, 101, 71))
        self.send_message_btn.setObjectName("send_message_btn")
        self.message_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message_input.setGeometry(QtCore.QRect(430, 40, 221, 211))
        self.message_input.setObjectName("message_input")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(670, 20, 341, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 21))
        self.label.setObjectName("label")
        self.server_ip_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.server_ip_input.setGeometry(QtCore.QRect(150, 40, 181, 31))
        self.server_ip_input.setObjectName("server_ip_input")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.label_3.setObjectName("label_3")
        self.buffer_size_input = QtWidgets.QSpinBox(self.groupBox_2)
        self.buffer_size_input.setGeometry(QtCore.QRect(150, 160, 181, 31))
        self.buffer_size_input.setMinimum(100)
        self.buffer_size_input.setMaximum(3000)
        self.buffer_size_input.setObjectName("buffer_size_input")
        self.port_number_input = QtWidgets.QSpinBox(self.groupBox_2)
        self.port_number_input.setGeometry(QtCore.QRect(150, 90, 181, 31))
        self.port_number_input.setMinimum(1)
        self.port_number_input.setMaximum(8000)
        self.port_number_input.setObjectName("port_number_input")
        self.connect_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.connect_btn.setGeometry(QtCore.QRect(10, 230, 141, 71))
        self.connect_btn.setObjectName("connect_btn")
        self.disconnect_and_exit_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.disconnect_and_exit_btn.setGeometry(QtCore.QRect(170, 230, 151, 71))
        self.disconnect_and_exit_btn.setObjectName("disconnect_and_exit_btn")
        self.clear_messages_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_messages_btn.setGeometry(QtCore.QRect(430, 260, 111, 71))
        self.clear_messages_btn.setObjectName("clear_messages_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 10, 241, 331))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.send_message_btn.raise_()
        self.message_input.raise_()
        self.groupBox_2.raise_()
        self.clear_messages_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionExport)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def connect_button_click(self):
        # TODO: Implement Button Click
        pass

    def dissconnect_button_click(self):
        # TODO: Implement Button Click
        pass

    def clear_button_click(self):
        # TODO: Implement Button Click
        pass

    def send_button_click(self):
        # TODO: Implement Button Click
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Incoming Messages"))
        self.send_message_btn.setText(_translate("MainWindow", "Send Message"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Connection Configurations"))
        self.label.setText(_translate("MainWindow", "Server IP Address"))
        self.label_2.setText(_translate("MainWindow", "Port Number"))
        self.label_3.setText(_translate("MainWindow", "Reading Buffer Size"))
        self.connect_btn.setText(_translate("MainWindow", "Connect To Server"))
        self.disconnect_and_exit_btn.setText(_translate("MainWindow", "Disconnect And Exit"))
        self.clear_messages_btn.setText(_translate("MainWindow", "Clear Messages"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Message Pane"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport.setText(_translate("MainWindow", "Export "))
        self.actionAbout.setText(_translate("MainWindow", "About SimpleChatClient"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

