from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsForm(object):
    def setupUi(self, SettingsForm):
        SettingsForm.setObjectName("SettingsForm")
        SettingsForm.resize(466, 398)
        SettingsForm.setMinimumSize(QtCore.QSize(466, 398))
        SettingsForm.setMaximumSize(QtCore.QSize(466, 398))
        self.gridLayout = QtWidgets.QGridLayout(SettingsForm)
        self.gridLayout.setObjectName("gridLayout")
        self.settingsBox = QtWidgets.QGroupBox(SettingsForm)
        self.settingsBox.setObjectName("settingsBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingsBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveSettingsButton = QtWidgets.QPushButton(self.settingsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveSettingsButton.sizePolicy().hasHeightForWidth())
        self.saveSettingsButton.setSizePolicy(sizePolicy)
        self.saveSettingsButton.setObjectName("saveSettingsButton")
        self.horizontalLayout_2.addWidget(self.saveSettingsButton)
        self.cancelSettingsButton = QtWidgets.QPushButton(self.settingsBox)
        self.cancelSettingsButton.setObjectName("cancelSettingsButton")
        self.horizontalLayout_2.addWidget(self.cancelSettingsButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.ThemeBox = QtWidgets.QGroupBox(self.settingsBox)
        self.ThemeBox.setObjectName("ThemeBox")
        self.themeComboBox = QtWidgets.QComboBox(self.ThemeBox)
        self.themeComboBox.setGeometry(QtCore.QRect(10, 30, 69, 22))
        self.themeComboBox.setObjectName("themeComboBox")
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.ThemeBox)
        self.label_2.setGeometry(QtCore.QRect(130, 80, 211, 16))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.ThemeBox, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.settingsBox)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.certPath = QtWidgets.QLineEdit(self.groupBox)
        self.certPath.setText("")
        self.certPath.setObjectName("certPath")
        self.horizontalLayout.addWidget(self.certPath)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.settingsBox, 0, 0, 1, 1)

        self.retranslateUi(SettingsForm)
        QtCore.QMetaObject.connectSlotsByName(SettingsForm)

    def retranslateUi(self, SettingsForm):
        _translate = QtCore.QCoreApplication.translate
        SettingsForm.setWindowTitle(_translate("SettingsForm", "Settings"))
        self.settingsBox.setTitle(_translate("SettingsForm", "Settings"))
        self.saveSettingsButton.setText(_translate("SettingsForm", "Save"))
        self.cancelSettingsButton.setText(_translate("SettingsForm", "Cancel"))
        self.ThemeBox.setTitle(_translate("SettingsForm", "Theme"))
        self.themeComboBox.setItemText(0, _translate("SettingsForm", "Light"))
        self.themeComboBox.setItemText(1, _translate("SettingsForm", "Dark"))
        self.themeComboBox.setItemText(2, _translate("SettingsForm", "Yami"))
        self.label_2.setText(_translate("SettingsForm", "WIP will add more later"))
        self.groupBox.setTitle(_translate("SettingsForm", "Misc"))
        self.label.setText(_translate("SettingsForm", "SSL Cert Path: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsForm = QtWidgets.QDialog()
    ui = Ui_SettingsForm()
    ui.setupUi(SettingsForm)
    SettingsForm.show()
    sys.exit(app.exec())