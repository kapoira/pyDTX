# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetNavegacion.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetNavegacion(object):
    def setupUi(self, WidgetNavegacion):
        WidgetNavegacion.setObjectName("WidgetNavegacion")
        WidgetNavegacion.resize(1280, 720)
        self.gridLayout = QtWidgets.QGridLayout(WidgetNavegacion)
        self.gridLayout.setObjectName("gridLayout")
        self.imagenCancion = QtWidgets.QLabel(WidgetNavegacion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagenCancion.sizePolicy().hasHeightForWidth())
        self.imagenCancion.setSizePolicy(sizePolicy)
        self.imagenCancion.setMinimumSize(QtCore.QSize(600, 600))
        self.imagenCancion.setMaximumSize(QtCore.QSize(600, 600))
        self.imagenCancion.setText("")
        self.imagenCancion.setScaledContents(True)
        self.imagenCancion.setObjectName("imagenCancion")
        self.gridLayout.addWidget(self.imagenCancion, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.backButton = QtWidgets.QPushButton(WidgetNavegacion)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.upButton = QtWidgets.QPushButton(WidgetNavegacion)
        self.upButton.setObjectName("upButton")
        self.verticalLayout.addWidget(self.upButton)
        self.downButton = QtWidgets.QPushButton(WidgetNavegacion)
        self.downButton.setObjectName("downButton")
        self.verticalLayout.addWidget(self.downButton)
        self.selectButton = QtWidgets.QPushButton(WidgetNavegacion)
        self.selectButton.setObjectName("selectButton")
        self.verticalLayout.addWidget(self.selectButton)
        self.changedirButton = QtWidgets.QPushButton(WidgetNavegacion)
        self.changedirButton.setObjectName("changedirButton")
        self.verticalLayout.addWidget(self.changedirButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l1_Button = QtWidgets.QPushButton(WidgetNavegacion)
        self.l1_Button.setObjectName("l1_Button")
        self.horizontalLayout_2.addWidget(self.l1_Button)
        self.l2_Button = QtWidgets.QPushButton(WidgetNavegacion)
        self.l2_Button.setObjectName("l2_Button")
        self.horizontalLayout_2.addWidget(self.l2_Button)
        self.l3_Button = QtWidgets.QPushButton(WidgetNavegacion)
        self.l3_Button.setObjectName("l3_Button")
        self.horizontalLayout_2.addWidget(self.l3_Button)
        self.l4_Button = QtWidgets.QPushButton(WidgetNavegacion)
        self.l4_Button.setObjectName("l4_Button")
        self.horizontalLayout_2.addWidget(self.l4_Button)
        self.l5_Button = QtWidgets.QPushButton(WidgetNavegacion)
        self.l5_Button.setObjectName("l5_Button")
        self.horizontalLayout_2.addWidget(self.l5_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(WidgetNavegacion)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.speed_inc_Button = QtWidgets.QPushButton(WidgetNavegacion)
        self.speed_inc_Button.setObjectName("speed_inc_Button")
        self.horizontalLayout_3.addWidget(self.speed_inc_Button)
        self.speed_dec_Button = QtWidgets.QPushButton(WidgetNavegacion)
        self.speed_dec_Button.setObjectName("speed_dec_Button")
        self.horizontalLayout_3.addWidget(self.speed_dec_Button)
        self.speed_label = QtWidgets.QLabel(WidgetNavegacion)
        self.speed_label.setMinimumSize(QtCore.QSize(246, 0))
        self.speed_label.setObjectName("speed_label")
        self.horizontalLayout_3.addWidget(self.speed_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 4, 1)
        self.label_name = QtWidgets.QLabel(WidgetNavegacion)
        self.label_name.setMinimumSize(QtCore.QSize(246, 0))
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 1)
        self.label_dificulty = QtWidgets.QLabel(WidgetNavegacion)
        self.label_dificulty.setObjectName("label_dificulty")
        self.gridLayout.addWidget(self.label_dificulty, 2, 0, 1, 1)
        self.label_others = QtWidgets.QLabel(WidgetNavegacion)
        self.label_others.setObjectName("label_others")
        self.gridLayout.addWidget(self.label_others, 3, 0, 1, 1)

        self.retranslateUi(WidgetNavegacion)
        QtCore.QMetaObject.connectSlotsByName(WidgetNavegacion)

    def retranslateUi(self, WidgetNavegacion):
        _translate = QtCore.QCoreApplication.translate
        WidgetNavegacion.setWindowTitle(_translate("WidgetNavegacion", "Form"))
        self.backButton.setText(_translate("WidgetNavegacion", ".."))
        self.upButton.setText(_translate("WidgetNavegacion", "Up"))
        self.downButton.setText(_translate("WidgetNavegacion", "Down"))
        self.selectButton.setText(_translate("WidgetNavegacion", "Select"))
        self.changedirButton.setText(_translate("WidgetNavegacion", "Change directory"))
        self.l1_Button.setText(_translate("WidgetNavegacion", "PushButton"))
        self.l2_Button.setText(_translate("WidgetNavegacion", "PushButton"))
        self.l3_Button.setText(_translate("WidgetNavegacion", "PushButton"))
        self.l4_Button.setText(_translate("WidgetNavegacion", "PushButton"))
        self.l5_Button.setText(_translate("WidgetNavegacion", "PushButton"))
        self.speed_inc_Button.setText(_translate("WidgetNavegacion", "Speed +"))
        self.speed_dec_Button.setText(_translate("WidgetNavegacion", "Speed -"))
        self.speed_label.setText(_translate("WidgetNavegacion", "Speed"))
        self.label_name.setText(_translate("WidgetNavegacion", "Name:"))
        self.label_dificulty.setText(_translate("WidgetNavegacion", "Dificulty:"))
        self.label_others.setText(_translate("WidgetNavegacion", "Others"))
