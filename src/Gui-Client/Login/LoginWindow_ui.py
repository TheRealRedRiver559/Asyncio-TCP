from PySide6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, MainWindow : QtGui.QWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 505)
        MainWindow.setMinimumSize(530, 505)
        MainWindow.setMaximumSize(530, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.helpButton = QtWidgets.QToolButton(self.centralwidget)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout_53.addWidget(self.helpButton)
        self.settingsButton = QtWidgets.QToolButton(self.centralwidget)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout_53.addWidget(self.settingsButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_53, 0, 0, 1, 1)
        self.loginBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginBox.setFont(font)
        self.loginBox.setObjectName("loginBox")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.loginBox)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout()
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout()
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.label_27 = QtWidgets.QLabel(self.loginBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_68.addWidget(self.label_27)
        self.usernameText = QtWidgets.QLineEdit(self.loginBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameText.sizePolicy().hasHeightForWidth())
        self.usernameText.setSizePolicy(sizePolicy)
        self.usernameText.setClearButtonEnabled(True)
        self.usernameText.setObjectName("usernameText")
        self.verticalLayout_68.addWidget(self.usernameText)
        self.verticalLayout_67.addLayout(self.verticalLayout_68)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_67.addItem(spacerItem1)
        self.verticalLayout_69 = QtWidgets.QVBoxLayout()
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.label_28 = QtWidgets.QLabel(self.loginBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_69.addWidget(self.label_28)
        self.passwordText = QtWidgets.QLineEdit(self.loginBox)
        self.passwordText.setBaseSize(QtCore.QSize(0, 0))
        self.passwordText.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhPreferLatin|QtCore.Qt.InputMethodHint.ImhSensitiveData|QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.passwordText.setText("")
        self.passwordText.setMaxLength(32767)
        self.passwordText.setFrame(True)
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordText.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.passwordText.setClearButtonEnabled(True)
        self.passwordText.setObjectName("passwordText")
        self.verticalLayout_69.addWidget(self.passwordText)
        self.verticalLayout_67.addLayout(self.verticalLayout_69)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_67.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_67.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_67.addItem(spacerItem4)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.remeberMeRadio = QtWidgets.QRadioButton(self.loginBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.remeberMeRadio.setFont(font)
        self.remeberMeRadio.setObjectName("remeberMeRadio")
        self.horizontalLayout_54.addWidget(self.remeberMeRadio)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem5)
        self.resetPasswordButton = QtWidgets.QPushButton(self.loginBox)
        self.resetPasswordButton.setObjectName("resetPasswordButton")
        self.horizontalLayout_54.addWidget(self.resetPasswordButton)
        self.verticalLayout_67.addLayout(self.horizontalLayout_54)
        self.verticalLayout_66.addLayout(self.verticalLayout_67)
        self.signInButton = QtWidgets.QPushButton(self.loginBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.signInButton.setFont(font)
        self.signInButton.setObjectName("signInButton")
        self.verticalLayout_66.addWidget(self.signInButton)
        self.registerButton = QtWidgets.QPushButton(self.loginBox)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_66.addWidget(self.registerButton)
        self.gridLayout.addWidget(self.loginBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) # type: ignore
        self.helpButton.setText(_translate("MainWindow", "Help"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.loginBox.setTitle(_translate("MainWindow", "Login"))
        self.label_27.setText(_translate("MainWindow", "Username:"))
        self.label_28.setText(_translate("MainWindow", "Password:"))
        self.remeberMeRadio.setText(_translate("MainWindow", "Remeber login"))
        self.resetPasswordButton.setText(_translate("MainWindow", "Reset Password"))
        self.signInButton.setText(_translate("MainWindow", "Sign in"))
        self.registerButton.setText(_translate("MainWindow", "Register")) # type: ignore


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
