# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './WidgetPuntuacion.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetPuntuacion(object):
    def setupUi(self, WidgetPuntuacion):
        WidgetPuntuacion.setObjectName("WidgetPuntuacion")
        WidgetPuntuacion.resize(342, 214)
        self.gridLayout = QtWidgets.QGridLayout(WidgetPuntuacion)
        self.gridLayout.setObjectName("gridLayout")
        self.title_text_label = QtWidgets.QLabel(WidgetPuntuacion)
        self.title_text_label.setObjectName("title_text_label")
        self.gridLayout.addWidget(self.title_text_label, 0, 0, 1, 1)
        self.perfect_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.perfect_Label.setMinimumSize(QtCore.QSize(246, 0))
        self.perfect_Label.setObjectName("perfect_Label")
        self.gridLayout.addWidget(self.perfect_Label, 1, 0, 1, 1)
        self.perfect_text_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.perfect_text_Label.setObjectName("perfect_text_Label")
        self.gridLayout.addWidget(self.perfect_text_Label, 1, 1, 1, 1)
        self.perfect_per_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.perfect_per_Label.setObjectName("perfect_per_Label")
        self.gridLayout.addWidget(self.perfect_per_Label, 1, 2, 1, 1)
        self.great_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.great_Label.setMinimumSize(QtCore.QSize(246, 0))
        self.great_Label.setObjectName("great_Label")
        self.gridLayout.addWidget(self.great_Label, 2, 0, 1, 1)
        self.great_text_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.great_text_Label.setObjectName("great_text_Label")
        self.gridLayout.addWidget(self.great_text_Label, 2, 1, 1, 1)
        self.great_per_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.great_per_Label.setObjectName("great_per_Label")
        self.gridLayout.addWidget(self.great_per_Label, 2, 2, 1, 1)
        self.good_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.good_Label.setMinimumSize(QtCore.QSize(246, 0))
        self.good_Label.setObjectName("good_Label")
        self.gridLayout.addWidget(self.good_Label, 3, 0, 1, 1)
        self.good_text_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.good_text_Label.setObjectName("good_text_Label")
        self.gridLayout.addWidget(self.good_text_Label, 3, 1, 1, 1)
        self.good_per_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.good_per_Label.setObjectName("good_per_Label")
        self.gridLayout.addWidget(self.good_per_Label, 3, 2, 1, 1)
        self.poor_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.poor_Label.setMinimumSize(QtCore.QSize(246, 0))
        self.poor_Label.setObjectName("poor_Label")
        self.gridLayout.addWidget(self.poor_Label, 4, 0, 1, 1)
        self.poor_text_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.poor_text_Label.setObjectName("poor_text_Label")
        self.gridLayout.addWidget(self.poor_text_Label, 4, 1, 1, 1)
        self.poor_per_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.poor_per_Label.setObjectName("poor_per_Label")
        self.gridLayout.addWidget(self.poor_per_Label, 4, 2, 1, 1)
        self.miss_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.miss_Label.setMinimumSize(QtCore.QSize(246, 0))
        self.miss_Label.setObjectName("miss_Label")
        self.gridLayout.addWidget(self.miss_Label, 5, 0, 1, 1)
        self.miss_text_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.miss_text_Label.setObjectName("miss_text_Label")
        self.gridLayout.addWidget(self.miss_text_Label, 5, 1, 1, 1)
        self.miss_per_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.miss_per_Label.setObjectName("miss_per_Label")
        self.gridLayout.addWidget(self.miss_per_Label, 5, 2, 1, 1)
        self.dificulty_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.dificulty_Label.setMinimumSize(QtCore.QSize(246, 0))
        self.dificulty_Label.setObjectName("dificulty_Label")
        self.gridLayout.addWidget(self.dificulty_Label, 7, 0, 1, 1)
        self.max_combo_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.max_combo_Label.setObjectName("max_combo_Label")
        self.gridLayout.addWidget(self.max_combo_Label, 6, 0, 1, 1)
        self.max_combo_text_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.max_combo_text_Label.setObjectName("max_combo_text_Label")
        self.gridLayout.addWidget(self.max_combo_text_Label, 6, 1, 1, 1)
        self.max_combo_per_Label = QtWidgets.QLabel(WidgetPuntuacion)
        self.max_combo_per_Label.setObjectName("max_combo_per_Label")
        self.gridLayout.addWidget(self.max_combo_per_Label, 6, 2, 1, 1)

        self.retranslateUi(WidgetPuntuacion)
        QtCore.QMetaObject.connectSlotsByName(WidgetPuntuacion)

    def retranslateUi(self, WidgetPuntuacion):
        _translate = QtCore.QCoreApplication.translate
        WidgetPuntuacion.setWindowTitle(_translate("WidgetPuntuacion", "Form"))
        self.title_text_label.setText(_translate("WidgetPuntuacion", "Title"))
        self.perfect_Label.setText(_translate("WidgetPuntuacion", "Perfect:"))
        self.perfect_text_Label.setText(_translate("WidgetPuntuacion", "0"))
        self.perfect_per_Label.setText(_translate("WidgetPuntuacion", "%"))
        self.great_Label.setText(_translate("WidgetPuntuacion", "Great"))
        self.great_text_Label.setText(_translate("WidgetPuntuacion", "0"))
        self.great_per_Label.setText(_translate("WidgetPuntuacion", "%"))
        self.good_Label.setText(_translate("WidgetPuntuacion", "Good"))
        self.good_text_Label.setText(_translate("WidgetPuntuacion", "0"))
        self.good_per_Label.setText(_translate("WidgetPuntuacion", "%"))
        self.poor_Label.setText(_translate("WidgetPuntuacion", "Poor"))
        self.poor_text_Label.setText(_translate("WidgetPuntuacion", "0"))
        self.poor_per_Label.setText(_translate("WidgetPuntuacion", "%"))
        self.miss_Label.setText(_translate("WidgetPuntuacion", "Miss"))
        self.miss_text_Label.setText(_translate("WidgetPuntuacion", "0"))
        self.miss_per_Label.setText(_translate("WidgetPuntuacion", "%"))
        self.dificulty_Label.setText(_translate("WidgetPuntuacion", "Dificulty"))
        self.max_combo_Label.setText(_translate("WidgetPuntuacion", "Max Combo"))
        self.max_combo_text_Label.setText(_translate("WidgetPuntuacion", "0"))
        self.max_combo_per_Label.setText(_translate("WidgetPuntuacion", "%"))
