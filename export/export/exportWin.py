# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 398)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 501, 400))
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.export2easydata = QtWidgets.QLabel(self.frame)
        self.export2easydata.setGeometry(QtCore.QRect(0, 0, 496, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.export2easydata.setFont(font)
        self.export2easydata.setObjectName("export2easydata")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 30, 501, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 330, 501, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 350, 501, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.cancle_button = QtWidgets.QPushButton(self.layoutWidget)
        self.cancle_button.setMinimumSize(QtCore.QSize(78, 38))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancle_button.setFont(font)
        self.cancle_button.setAutoDefault(False)
        self.cancle_button.setObjectName("cancle_button")
        self.horizontalLayout_8.addWidget(self.cancle_button)
        self.comfire_button = QtWidgets.QPushButton(self.layoutWidget)
        self.comfire_button.setMinimumSize(QtCore.QSize(78, 38))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comfire_button.setFont(font)
        self.comfire_button.setCheckable(False)
        self.comfire_button.setChecked(False)
        self.comfire_button.setAutoRepeat(False)
        self.comfire_button.setAutoExclusive(False)
        self.comfire_button.setAutoDefault(False)
        self.comfire_button.setDefault(False)
        self.comfire_button.setFlat(False)
        self.comfire_button.setObjectName("comfire_button")
        self.horizontalLayout_8.addWidget(self.comfire_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 481, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.file_source_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.file_source_label.setFont(font)
        self.file_source_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.file_source_label.setObjectName("file_source_label")
        self.gridLayout.addWidget(self.file_source_label, 0, 0, 1, 1)
        self.file_source_text = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.file_source_text.setMinimumSize(QtCore.QSize(300, 10))
        self.file_source_text.setMaximumSize(QtCore.QSize(435, 30))
        self.file_source_text.setObjectName("file_source_text")
        self.gridLayout.addWidget(self.file_source_text, 0, 1, 1, 1)
        self.ak_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ak_label.setMaximumSize(QtCore.QSize(16777215, 35))
        self.ak_label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ak_label.setFont(font)
        self.ak_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ak_label.setTextFormat(QtCore.Qt.AutoText)
        self.ak_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ak_label.setObjectName("ak_label")
        self.gridLayout.addWidget(self.ak_label, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.akLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.akLineEdit.setMinimumSize(QtCore.QSize(0, 26))
        self.akLineEdit.setText("")
        self.akLineEdit.setObjectName("akLineEdit")
        self.horizontalLayout_2.addWidget(self.akLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sk_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.sk_label.setFont(font)
        self.sk_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sk_label.setTextFormat(QtCore.Qt.AutoText)
        self.sk_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sk_label.setObjectName("sk_label")
        self.verticalLayout.addWidget(self.sk_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.skLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.skLineEdit.setMinimumSize(QtCore.QSize(0, 26))
        self.skLineEdit.setObjectName("skLineEdit")
        self.horizontalLayout.addWidget(self.skLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tips_label = QtWidgets.QLabel(self.layoutWidget1)
        self.tips_label.setMaximumSize(QtCore.QSize(418, 26))
        self.tips_label.setOpenExternalLinks(True)
        self.tips_label.setObjectName("tips_label")
        self.verticalLayout_2.addWidget(self.tips_label)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.import_type_label = QtWidgets.QLabel(self.layoutWidget1)
        self.import_type_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.import_type_label.setFont(font)
        self.import_type_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.import_type_label.setObjectName("import_type_label")
        self.gridLayout.addWidget(self.import_type_label, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.incremental_upload = QtWidgets.QRadioButton(self.layoutWidget1)
        self.incremental_upload.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.incremental_upload.setFont(font)
        self.incremental_upload.setCheckable(True)
        self.incremental_upload.setChecked(True)
        self.incremental_upload.setAutoRepeat(False)
        self.incremental_upload.setObjectName("incremental_upload")
        self.horizontalLayout_4.addWidget(self.incremental_upload)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.full_upload = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.full_upload.setFont(font)
        self.full_upload.setObjectName("full_upload")
        self.horizontalLayout_3.addWidget(self.full_upload)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.annotate_type_label = QtWidgets.QLabel(self.layoutWidget1)
        self.annotate_type_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.annotate_type_label.setFont(font)
        self.annotate_type_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.annotate_type_label.setObjectName("annotate_type_label")
        self.gridLayout.addWidget(self.annotate_type_label, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dataset_label = QtWidgets.QLabel(self.layoutWidget1)
        self.dataset_label.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dataset_label.setFont(font)
        self.dataset_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataset_label.setOpenExternalLinks(True)
        self.dataset_label.setObjectName("dataset_label")
        self.verticalLayout_4.addWidget(self.dataset_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem7)
        self.gridLayout.addLayout(self.verticalLayout_4, 5, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.dataset_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.dataset_comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.dataset_comboBox.setIconSize(QtCore.QSize(16, 16))
        self.dataset_comboBox.setObjectName("dataset_comboBox")
        self.horizontalLayout_7.addWidget(self.dataset_comboBox)
        self.version_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.version_comboBox.setObjectName("version_comboBox")
        self.horizontalLayout_7.addWidget(self.version_comboBox)
        self.crash_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.crash_button.setDefault(True)
        self.crash_button.setObjectName("crash_button")
        self.horizontalLayout_7.addWidget(self.crash_button)
        spacerItem8 = QtWidgets.QSpacerItem(40, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 3)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.create_label = QtWidgets.QLabel(self.layoutWidget1)
        self.create_label.setMaximumSize(QtCore.QSize(65, 26))
        self.create_label.setOpenExternalLinks(True)
        self.create_label.setObjectName("create_label")
        self.verticalLayout_3.addWidget(self.create_label)
        self.gridLayout.addLayout(self.verticalLayout_3, 5, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 9)

        self.dataset_comboBox.setPlaceholderText("请选择数据集")
        self.version_comboBox.setPlaceholderText("请选择版本")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", ""))
        self.export2easydata.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">导出到EasyData</span></p></body></html>"))
        self.cancle_button.setText(_translate("Dialog", "取消"))
        self.comfire_button.setText(_translate("Dialog", "确认"))
        self.file_source_label.setText(_translate("Dialog", "文件来源"))
        self.ak_label.setText(_translate("Dialog", "AK"))
        self.sk_label.setText(_translate("Dialog", "SK"))
        self.tips_label.setText(_translate("Dialog", "<html><head/><body><p><font color=\"#FF9900\">提示：注册并登录</font><a href=\"https://ai.baidu.com/easydata/\"><span style=\" text-decoration: underline; color:#0000ff;\">EasyData</span></a><font color=\"#FF9900\">平台，即可从右上角个人中心复制密钥</font></p></body></html>"))
        self.import_type_label.setText(_translate("Dialog", "导入方式"))
        self.incremental_upload.setText(_translate("Dialog", "增量导入"))
        self.label_2.setToolTip(_translate("Dialog", "<html><head/><body><p>若此前已完成上传的图片，在标注信息未修改的情况下，本次不再重复上传</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">？</span></p></body></html>"))
        self.full_upload.setText(_translate("Dialog", "全量导入"))
        self.label_3.setToolTip(_translate("Dialog", "<html><head/><body><p>所选文件夹下的标注图片将全部覆盖上传</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">？</span></p></body></html>"))
        self.annotate_type_label.setText(_translate("Dialog", "标注类型"))
        self.label.setText(_translate("Dialog", "物体检测"))
        self.dataset_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:13pt;\">数据集</span></p></body></html>"))
        self.dataset_comboBox.setToolTip(_translate("Dialog", "<html><head/><body><p>请选择数据集</p></body></html>"))
        self.dataset_comboBox.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.version_comboBox.setToolTip(_translate("Dialog", "<html><head/><body><p>请选择版本</p></body></html>"))
        self.crash_button.setText(_translate("Dialog", "刷新列表"))
        self.create_label.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://ai.baidu.com/easydata/app/dataset/list\"><span style=\" text-decoration: underline; color:#0000ff;\">创建数据集</span></a></p></body></html>"))