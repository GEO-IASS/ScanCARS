# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowMAIN.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1512, 995)
        MainWindow.setStyleSheet("/*\n"
"    Copyright 2013 Emanuel Claesson\n"
"\n"
"    Licensed under the Apache License, Version 2.0 (the \"License\");\n"
"    you may not use this file except in compliance with the License.\n"
"    You may obtain a copy of the License at\n"
"\n"
"        http://www.apache.org/licenses/LICENSE-2.0\n"
"\n"
"    Unless required by applicable law or agreed to in writing, software\n"
"    distributed under the License is distributed on an \"AS IS\" BASIS,\n"
"    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
"    See the License for the specific language governing permissions and\n"
"    limitations under the License.\n"
"*/\n"
"\n"
"/*\n"
"    COLOR_DARK     = #191919\n"
"    COLOR_MEDIUM   = #353535\n"
"    COLOR_MEDLIGHT = #5A5A5A\n"
"    COLOR_LIGHT    = #DDDDDD\n"
"    COLOR_ACCENT   = #3D7848\n"
"*/\n"
"\n"
"* {\n"
"    background: #191919;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #191919;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #353535;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#353535;\n"
"    border: 1px solid #5A5A5A;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3D7848;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #353535;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #191919;\n"
"    border: 1px solid #5A5A5A;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #5A5A5A;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3D7848;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #353535;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_start_acq = QtWidgets.QPushButton(self.centralwidget)
        self.Main_start_acq.setGeometry(QtCore.QRect(30, 20, 141, 34))
        self.Main_start_acq.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.Main_start_acq.setObjectName("Main_start_acq")
        self.Main_shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.Main_shutdown.setGeometry(QtCore.QRect(1340, 20, 141, 34))
        self.Main_shutdown.setStyleSheet("QPushButton {\n"
"    background: #4a1b15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #62221b;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #762720;     \n"
"}")
        self.Main_shutdown.setObjectName("Main_shutdown")
        self.Main_status = QtWidgets.QLineEdit(self.centralwidget)
        self.Main_status.setGeometry(QtCore.QRect(190, 20, 1131, 34))
        self.Main_status.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_status.setReadOnly(True)
        self.Main_status.setObjectName("Main_status")
        self.group_CameraTemp = QtWidgets.QGroupBox(self.centralwidget)
        self.group_CameraTemp.setGeometry(QtCore.QRect(1340, 70, 141, 151))
        self.group_CameraTemp.setObjectName("group_CameraTemp")
        self.CameraTemp_temp_text = QtWidgets.QLineEdit(self.group_CameraTemp)
        self.CameraTemp_temp_text.setGeometry(QtCore.QRect(10, 30, 51, 32))
        self.CameraTemp_temp_text.setStyleSheet("border: 0")
        self.CameraTemp_temp_text.setFrame(True)
        self.CameraTemp_temp_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CameraTemp_temp_text.setReadOnly(True)
        self.CameraTemp_temp_text.setObjectName("CameraTemp_temp_text")
        self.CameraTemp_temp_req = QtWidgets.QLineEdit(self.group_CameraTemp)
        self.CameraTemp_temp_req.setGeometry(QtCore.QRect(60, 30, 71, 32))
        self.CameraTemp_temp_req.setAlignment(QtCore.Qt.AlignCenter)
        self.CameraTemp_temp_req.setObjectName("CameraTemp_temp_req")
        self.CameraTemp_cooler_on = QtWidgets.QPushButton(self.group_CameraTemp)
        self.CameraTemp_cooler_on.setGeometry(QtCore.QRect(10, 70, 121, 34))
        self.CameraTemp_cooler_on.setObjectName("CameraTemp_cooler_on")
        self.CameraTemp_temp_actual = QtWidgets.QLineEdit(self.group_CameraTemp)
        self.CameraTemp_temp_actual.setGeometry(QtCore.QRect(10, 110, 121, 32))
        self.CameraTemp_temp_actual.setAlignment(QtCore.Qt.AlignCenter)
        self.CameraTemp_temp_actual.setReadOnly(True)
        self.CameraTemp_temp_actual.setObjectName("CameraTemp_temp_actual")
        self.group_SpectraWin = QtWidgets.QGroupBox(self.centralwidget)
        self.group_SpectraWin.setGeometry(QtCore.QRect(1340, 240, 141, 121))
        self.group_SpectraWin.setObjectName("group_SpectraWin")
        self.SpectraWin_single_track = QtWidgets.QPushButton(self.group_SpectraWin)
        self.SpectraWin_single_track.setGeometry(QtCore.QRect(10, 30, 121, 34))
        self.SpectraWin_single_track.setObjectName("SpectraWin_single_track")
        self.SpectraWin_sum_track = QtWidgets.QPushButton(self.group_SpectraWin)
        self.SpectraWin_sum_track.setGeometry(QtCore.QRect(10, 70, 121, 34))
        self.SpectraWin_sum_track.setObjectName("SpectraWin_sum_track")
        self.group_Grating = QtWidgets.QGroupBox(self.centralwidget)
        self.group_Grating.setGeometry(QtCore.QRect(1340, 380, 141, 171))
        self.group_Grating.setObjectName("group_Grating")
        self.Grating_150 = QtWidgets.QRadioButton(self.group_Grating)
        self.Grating_150.setGeometry(QtCore.QRect(10, 30, 121, 22))
        self.Grating_150.setChecked(True)
        self.Grating_150.setObjectName("Grating_150")
        self.Grating_600 = QtWidgets.QRadioButton(self.group_Grating)
        self.Grating_600.setGeometry(QtCore.QRect(10, 60, 121, 22))
        self.Grating_600.setObjectName("Grating_600")
        self.Grating_lambda_text = QtWidgets.QLineEdit(self.group_Grating)
        self.Grating_lambda_text.setGeometry(QtCore.QRect(10, 90, 71, 32))
        self.Grating_lambda_text.setStyleSheet("border: 0")
        self.Grating_lambda_text.setReadOnly(True)
        self.Grating_lambda_text.setObjectName("Grating_lambda_text")
        self.Grating_wavelength = QtWidgets.QLineEdit(self.group_Grating)
        self.Grating_wavelength.setGeometry(QtCore.QRect(80, 90, 51, 32))
        self.Grating_wavelength.setAlignment(QtCore.Qt.AlignCenter)
        self.Grating_wavelength.setObjectName("Grating_wavelength")
        self.Grating_update = QtWidgets.QPushButton(self.group_Grating)
        self.Grating_update.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.Grating_update.setObjectName("Grating_update")
        self.group_EventLogger = QtWidgets.QGroupBox(self.centralwidget)
        self.group_EventLogger.setGeometry(QtCore.QRect(30, 700, 401, 231))
        self.group_EventLogger.setObjectName("group_EventLogger")
        self.EventLogger_box = QtWidgets.QPlainTextEdit(self.group_EventLogger)
        self.EventLogger_box.setGeometry(QtCore.QRect(10, 20, 381, 201))
        self.EventLogger_box.setReadOnly(True)
        self.EventLogger_box.setObjectName("EventLogger_box")
        self.group_CameraOptions = QtWidgets.QGroupBox(self.centralwidget)
        self.group_CameraOptions.setGeometry(QtCore.QRect(30, 560, 401, 131))
        self.group_CameraOptions.setObjectName("group_CameraOptions")
        self.CameraOptions_track1lower_text = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track1lower_text.setGeometry(QtCore.QRect(30, 30, 91, 21))
        self.CameraOptions_track1lower_text.setStyleSheet("border: 0")
        self.CameraOptions_track1lower_text.setFrame(True)
        self.CameraOptions_track1lower_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CameraOptions_track1lower_text.setReadOnly(True)
        self.CameraOptions_track1lower_text.setObjectName("CameraOptions_track1lower_text")
        self.CameraOptions_track1lower = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track1lower.setGeometry(QtCore.QRect(130, 30, 51, 21))
        self.CameraOptions_track1lower.setAlignment(QtCore.Qt.AlignCenter)
        self.CameraOptions_track1lower.setObjectName("CameraOptions_track1lower")
        self.CameraOptions_track1upper_text = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track1upper_text.setGeometry(QtCore.QRect(30, 60, 91, 21))
        self.CameraOptions_track1upper_text.setStyleSheet("border: 0")
        self.CameraOptions_track1upper_text.setFrame(True)
        self.CameraOptions_track1upper_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CameraOptions_track1upper_text.setReadOnly(True)
        self.CameraOptions_track1upper_text.setObjectName("CameraOptions_track1upper_text")
        self.CameraOptions_track1upper = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track1upper.setGeometry(QtCore.QRect(130, 60, 51, 21))
        self.CameraOptions_track1upper.setAlignment(QtCore.Qt.AlignCenter)
        self.CameraOptions_track1upper.setObjectName("CameraOptions_track1upper")
        self.CameraOptions_track2lower_text = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track2lower_text.setGeometry(QtCore.QRect(220, 30, 91, 21))
        self.CameraOptions_track2lower_text.setStyleSheet("border: 0")
        self.CameraOptions_track2lower_text.setFrame(True)
        self.CameraOptions_track2lower_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CameraOptions_track2lower_text.setReadOnly(True)
        self.CameraOptions_track2lower_text.setObjectName("CameraOptions_track2lower_text")
        self.CameraOptions_track2upper = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track2upper.setGeometry(QtCore.QRect(320, 60, 51, 21))
        self.CameraOptions_track2upper.setAlignment(QtCore.Qt.AlignCenter)
        self.CameraOptions_track2upper.setObjectName("CameraOptions_track2upper")
        self.CameraOptions_track2upper_text = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track2upper_text.setGeometry(QtCore.QRect(220, 60, 91, 21))
        self.CameraOptions_track2upper_text.setStyleSheet("border: 0")
        self.CameraOptions_track2upper_text.setFrame(True)
        self.CameraOptions_track2upper_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CameraOptions_track2upper_text.setReadOnly(True)
        self.CameraOptions_track2upper_text.setObjectName("CameraOptions_track2upper_text")
        self.CameraOptions_track2lower = QtWidgets.QLineEdit(self.group_CameraOptions)
        self.CameraOptions_track2lower.setGeometry(QtCore.QRect(320, 30, 51, 21))
        self.CameraOptions_track2lower.setAlignment(QtCore.Qt.AlignCenter)
        self.CameraOptions_track2lower.setObjectName("CameraOptions_track2lower")
        self.CameraOptions_update = QtWidgets.QPushButton(self.group_CameraOptions)
        self.CameraOptions_update.setGeometry(QtCore.QRect(30, 90, 151, 21))
        self.CameraOptions_update.setObjectName("CameraOptions_update")
        self.CameraOptions_openimage = QtWidgets.QPushButton(self.group_CameraOptions)
        self.CameraOptions_openimage.setGeometry(QtCore.QRect(220, 90, 151, 21))
        self.CameraOptions_openimage.setObjectName("CameraOptions_openimage")
        self.group_SpectralAcq = QtWidgets.QGroupBox(self.centralwidget)
        self.group_SpectralAcq.setGeometry(QtCore.QRect(450, 560, 541, 131))
        self.group_SpectralAcq.setObjectName("group_SpectralAcq")
        self.SpectralAcq_time_text = QtWidgets.QLineEdit(self.group_SpectralAcq)
        self.SpectralAcq_time_text.setGeometry(QtCore.QRect(20, 30, 131, 21))
        self.SpectralAcq_time_text.setStyleSheet("border: 0")
        self.SpectralAcq_time_text.setFrame(True)
        self.SpectralAcq_time_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SpectralAcq_time_text.setReadOnly(True)
        self.SpectralAcq_time_text.setObjectName("SpectralAcq_time_text")
        self.SpectralAcq_actual_time = QtWidgets.QLineEdit(self.group_SpectralAcq)
        self.SpectralAcq_actual_time.setGeometry(QtCore.QRect(160, 60, 71, 21))
        self.SpectralAcq_actual_time.setAlignment(QtCore.Qt.AlignCenter)
        self.SpectralAcq_actual_time.setObjectName("SpectralAcq_actual_time")
        self.SpectralAcq_actual_time_text = QtWidgets.QLineEdit(self.group_SpectralAcq)
        self.SpectralAcq_actual_time_text.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.SpectralAcq_actual_time_text.setStyleSheet("border: 0")
        self.SpectralAcq_actual_time_text.setFrame(True)
        self.SpectralAcq_actual_time_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SpectralAcq_actual_time_text.setReadOnly(True)
        self.SpectralAcq_actual_time_text.setObjectName("SpectralAcq_actual_time_text")
        self.SpectralAcq_update_time = QtWidgets.QPushButton(self.group_SpectralAcq)
        self.SpectralAcq_update_time.setGeometry(QtCore.QRect(20, 90, 211, 21))
        self.SpectralAcq_update_time.setObjectName("SpectralAcq_update_time")
        self.SpectralAcq_darkfield = QtWidgets.QLineEdit(self.group_SpectralAcq)
        self.SpectralAcq_darkfield.setGeometry(QtCore.QRect(450, 30, 71, 21))
        self.SpectralAcq_darkfield.setAlignment(QtCore.Qt.AlignCenter)
        self.SpectralAcq_darkfield.setObjectName("SpectralAcq_darkfield")
        self.SpectralAcq_darkfield_text = QtWidgets.QLineEdit(self.group_SpectralAcq)
        self.SpectralAcq_darkfield_text.setGeometry(QtCore.QRect(280, 30, 161, 21))
        self.SpectralAcq_darkfield_text.setStyleSheet("border: 0")
        self.SpectralAcq_darkfield_text.setFrame(True)
        self.SpectralAcq_darkfield_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SpectralAcq_darkfield_text.setReadOnly(True)
        self.SpectralAcq_darkfield_text.setObjectName("SpectralAcq_darkfield_text")
        self.SpectralAcq_frame_text = QtWidgets.QLineEdit(self.group_SpectralAcq)
        self.SpectralAcq_frame_text.setGeometry(QtCore.QRect(280, 60, 161, 21))
        self.SpectralAcq_frame_text.setStyleSheet("border: 0")
        self.SpectralAcq_frame_text.setFrame(True)
        self.SpectralAcq_frame_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SpectralAcq_frame_text.setReadOnly(True)
        self.SpectralAcq_frame_text.setObjectName("SpectralAcq_frame_text")
        self.SpectralAcq_frames = QtWidgets.QLineEdit(self.group_SpectralAcq)
        self.SpectralAcq_frames.setGeometry(QtCore.QRect(450, 60, 71, 21))
        self.SpectralAcq_frames.setAlignment(QtCore.Qt.AlignCenter)
        self.SpectralAcq_frames.setObjectName("SpectralAcq_frames")
        self.SpectralAcq_start = QtWidgets.QPushButton(self.group_SpectralAcq)
        self.SpectralAcq_start.setGeometry(QtCore.QRect(280, 90, 241, 21))
        self.SpectralAcq_start.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.SpectralAcq_start.setObjectName("SpectralAcq_start")
        self.SpectralAcq_time_req = QtWidgets.QDoubleSpinBox(self.group_SpectralAcq)
        self.SpectralAcq_time_req.setGeometry(QtCore.QRect(160, 30, 71, 21))
        self.SpectralAcq_time_req.setAlignment(QtCore.Qt.AlignCenter)
        self.SpectralAcq_time_req.setDecimals(3)
        self.SpectralAcq_time_req.setSingleStep(0.01)
        self.SpectralAcq_time_req.setProperty("value", 0.05)
        self.SpectralAcq_time_req.setObjectName("SpectralAcq_time_req")
        self.Main_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.Main_progress.setGeometry(QtCore.QRect(1010, 900, 471, 30))
        self.Main_progress.setProperty("value", 0)
        self.Main_progress.setObjectName("Main_progress")
        self.group_HyperAcq = QtWidgets.QGroupBox(self.centralwidget)
        self.group_HyperAcq.setGeometry(QtCore.QRect(450, 700, 541, 231))
        self.group_HyperAcq.setObjectName("group_HyperAcq")
        self.HyperAcq_time_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_time_text.setGeometry(QtCore.QRect(20, 30, 131, 21))
        self.HyperAcq_time_text.setStyleSheet("border: 0")
        self.HyperAcq_time_text.setFrame(True)
        self.HyperAcq_time_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_time_text.setReadOnly(True)
        self.HyperAcq_time_text.setObjectName("HyperAcq_time_text")
        self.HyperAcq_darkfield_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_darkfield_text.setGeometry(QtCore.QRect(280, 30, 161, 21))
        self.HyperAcq_darkfield_text.setStyleSheet("border: 0")
        self.HyperAcq_darkfield_text.setFrame(True)
        self.HyperAcq_darkfield_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_darkfield_text.setReadOnly(True)
        self.HyperAcq_darkfield_text.setObjectName("HyperAcq_darkfield_text")
        self.HyperAcq_darkfield = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_darkfield.setGeometry(QtCore.QRect(450, 30, 71, 21))
        self.HyperAcq_darkfield.setAlignment(QtCore.Qt.AlignCenter)
        self.HyperAcq_darkfield.setObjectName("HyperAcq_darkfield")
        self.HyperAcq_xpixel_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_xpixel_text.setGeometry(QtCore.QRect(80, 80, 61, 21))
        self.HyperAcq_xpixel_text.setStyleSheet("border: 0")
        self.HyperAcq_xpixel_text.setFrame(True)
        self.HyperAcq_xpixel_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_xpixel_text.setReadOnly(True)
        self.HyperAcq_xpixel_text.setObjectName("HyperAcq_xpixel_text")
        self.HyperAcq_xpixel = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_xpixel.setGeometry(QtCore.QRect(140, 80, 51, 21))
        self.HyperAcq_xpixel.setAlignment(QtCore.Qt.AlignCenter)
        self.HyperAcq_xpixel.setObjectName("HyperAcq_xpixel")
        self.HyperAcq_ypixel_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_ypixel_text.setGeometry(QtCore.QRect(80, 110, 61, 21))
        self.HyperAcq_ypixel_text.setStyleSheet("border: 0")
        self.HyperAcq_ypixel_text.setFrame(True)
        self.HyperAcq_ypixel_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_ypixel_text.setReadOnly(True)
        self.HyperAcq_ypixel_text.setObjectName("HyperAcq_ypixel_text")
        self.HyperAcq_ypixel = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_ypixel.setGeometry(QtCore.QRect(140, 110, 51, 21))
        self.HyperAcq_ypixel.setAlignment(QtCore.Qt.AlignCenter)
        self.HyperAcq_ypixel.setObjectName("HyperAcq_ypixel")
        self.HyperAcq_zpixel_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_zpixel_text.setGeometry(QtCore.QRect(80, 140, 61, 21))
        self.HyperAcq_zpixel_text.setStyleSheet("border: 0")
        self.HyperAcq_zpixel_text.setFrame(True)
        self.HyperAcq_zpixel_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_zpixel_text.setReadOnly(True)
        self.HyperAcq_zpixel_text.setObjectName("HyperAcq_zpixel_text")
        self.HyperAcq_zpixel = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_zpixel.setGeometry(QtCore.QRect(140, 140, 51, 21))
        self.HyperAcq_zpixel.setAlignment(QtCore.Qt.AlignCenter)
        self.HyperAcq_zpixel.setObjectName("HyperAcq_zpixel")
        self.HyperAcq_xystep_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_xystep_text.setGeometry(QtCore.QRect(240, 80, 121, 21))
        self.HyperAcq_xystep_text.setStyleSheet("border: 0")
        self.HyperAcq_xystep_text.setFrame(True)
        self.HyperAcq_xystep_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_xystep_text.setReadOnly(True)
        self.HyperAcq_xystep_text.setObjectName("HyperAcq_xystep_text")
        self.HyperAcq_zstep_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_zstep_text.setGeometry(QtCore.QRect(240, 110, 111, 21))
        self.HyperAcq_zstep_text.setStyleSheet("border: 0")
        self.HyperAcq_zstep_text.setFrame(True)
        self.HyperAcq_zstep_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_zstep_text.setReadOnly(True)
        self.HyperAcq_zstep_text.setObjectName("HyperAcq_zstep_text")
        self.HyperAcq_zstep = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_zstep.setGeometry(QtCore.QRect(390, 110, 71, 21))
        self.HyperAcq_zstep.setAlignment(QtCore.Qt.AlignCenter)
        self.HyperAcq_zstep.setObjectName("HyperAcq_zstep")
        self.HyperAcq_xystep = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_xystep.setGeometry(QtCore.QRect(390, 80, 71, 21))
        self.HyperAcq_xystep.setAlignment(QtCore.Qt.AlignCenter)
        self.HyperAcq_xystep.setObjectName("HyperAcq_xystep")
        self.SpectralAcq_time_req_8 = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.SpectralAcq_time_req_8.setGeometry(QtCore.QRect(390, 140, 71, 21))
        self.SpectralAcq_time_req_8.setAlignment(QtCore.Qt.AlignCenter)
        self.SpectralAcq_time_req_8.setReadOnly(True)
        self.SpectralAcq_time_req_8.setObjectName("SpectralAcq_time_req_8")
        self.HyperAcq_est_time_text = QtWidgets.QLineEdit(self.group_HyperAcq)
        self.HyperAcq_est_time_text.setGeometry(QtCore.QRect(240, 140, 141, 21))
        self.HyperAcq_est_time_text.setStyleSheet("border: 0")
        self.HyperAcq_est_time_text.setFrame(True)
        self.HyperAcq_est_time_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HyperAcq_est_time_text.setReadOnly(True)
        self.HyperAcq_est_time_text.setObjectName("HyperAcq_est_time_text")
        self.HyperAcq_start = QtWidgets.QPushButton(self.group_HyperAcq)
        self.HyperAcq_start.setGeometry(QtCore.QRect(20, 190, 501, 21))
        self.HyperAcq_start.setStyleSheet("QPushButton {\n"
"    background: #323e30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #3e5f41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #537f57;     \n"
"}")
        self.HyperAcq_start.setObjectName("HyperAcq_start")
        self.HyperAcq_time_req = QtWidgets.QDoubleSpinBox(self.group_HyperAcq)
        self.HyperAcq_time_req.setGeometry(QtCore.QRect(160, 30, 71, 21))
        self.HyperAcq_time_req.setAlignment(QtCore.Qt.AlignCenter)
        self.HyperAcq_time_req.setDecimals(3)
        self.HyperAcq_time_req.setSingleStep(0.01)
        self.HyperAcq_time_req.setProperty("value", 0.05)
        self.HyperAcq_time_req.setObjectName("HyperAcq_time_req")
        self.Main_specwin = PlotWidget(self.centralwidget)
        self.Main_specwin.setGeometry(QtCore.QRect(30, 70, 1291, 481))
        self.Main_specwin.setObjectName("Main_specwin")
        self.Main_imagewin = ImageView(self.centralwidget)
        self.Main_imagewin.setGeometry(QtCore.QRect(1010, 570, 471, 331))
        self.Main_imagewin.setObjectName("Main_imagewin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1512, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScanCARS"))
        self.Main_start_acq.setText(_translate("MainWindow", "Start Acquisition"))
        self.Main_shutdown.setText(_translate("MainWindow", "Shut Down"))
        self.group_CameraTemp.setTitle(_translate("MainWindow", "Camera Temp."))
        self.CameraTemp_temp_text.setText(_translate("MainWindow", "Temp:"))
        self.CameraTemp_temp_req.setText(_translate("MainWindow", "-80"))
        self.CameraTemp_cooler_on.setText(_translate("MainWindow", "Cooler On"))
        self.group_SpectraWin.setTitle(_translate("MainWindow", "Spectral Windows"))
        self.SpectraWin_single_track.setText(_translate("MainWindow", "Single Tracks"))
        self.SpectraWin_sum_track.setText(_translate("MainWindow", "Sum"))
        self.group_Grating.setTitle(_translate("MainWindow", "Spectral Grating"))
        self.Grating_150.setText(_translate("MainWindow", "&150 lines/mm"))
        self.Grating_600.setText(_translate("MainWindow", "&600 lines/mm"))
        self.Grating_lambda_text.setText(_translate("MainWindow", "Center λ:"))
        self.Grating_wavelength.setText(_translate("MainWindow", "682"))
        self.Grating_update.setText(_translate("MainWindow", "Update"))
        self.group_EventLogger.setTitle(_translate("MainWindow", "Event Logger"))
        self.group_CameraOptions.setTitle(_translate("MainWindow", "Camera Options"))
        self.CameraOptions_track1lower_text.setText(_translate("MainWindow", "Track 1 Lower:"))
        self.CameraOptions_track1lower.setText(_translate("MainWindow", "165"))
        self.CameraOptions_track1upper_text.setText(_translate("MainWindow", "Track 1 Upper:"))
        self.CameraOptions_track1upper.setText(_translate("MainWindow", "198"))
        self.CameraOptions_track2lower_text.setText(_translate("MainWindow", "Track 2 Lower:"))
        self.CameraOptions_track2upper.setText(_translate("MainWindow", "244"))
        self.CameraOptions_track2upper_text.setText(_translate("MainWindow", "Track 2 Upper:"))
        self.CameraOptions_track2lower.setText(_translate("MainWindow", "211"))
        self.CameraOptions_update.setText(_translate("MainWindow", "Update Tracks"))
        self.CameraOptions_openimage.setText(_translate("MainWindow", "View CCD Tracks"))
        self.group_SpectralAcq.setTitle(_translate("MainWindow", "Spectral Acquisition"))
        self.SpectralAcq_time_text.setText(_translate("MainWindow", "Acquisition Time (s):"))
        self.SpectralAcq_actual_time.setText(_translate("MainWindow", "0.005"))
        self.SpectralAcq_actual_time_text.setText(_translate("MainWindow", "Actual Acq. Time (s):"))
        self.SpectralAcq_update_time.setText(_translate("MainWindow", "Update Time"))
        self.SpectralAcq_darkfield.setText(_translate("MainWindow", "100"))
        self.SpectralAcq_darkfield_text.setText(_translate("MainWindow", "Dark Field (no. of frames):"))
        self.SpectralAcq_frame_text.setText(_translate("MainWindow", "No. of frames required:"))
        self.SpectralAcq_frames.setText(_translate("MainWindow", "300"))
        self.SpectralAcq_start.setText(_translate("MainWindow", "Start Spectral Acquisition"))
        self.group_HyperAcq.setTitle(_translate("MainWindow", "Hyperspectral Image Acquisition"))
        self.HyperAcq_time_text.setText(_translate("MainWindow", "Acquisition Time (s):"))
        self.HyperAcq_darkfield_text.setText(_translate("MainWindow", "Dark Field (no. of frames):"))
        self.HyperAcq_darkfield.setText(_translate("MainWindow", "100"))
        self.HyperAcq_xpixel_text.setText(_translate("MainWindow", "X Pixels:"))
        self.HyperAcq_xpixel.setText(_translate("MainWindow", "50"))
        self.HyperAcq_ypixel_text.setText(_translate("MainWindow", "Y Pixels:"))
        self.HyperAcq_ypixel.setText(_translate("MainWindow", "10"))
        self.HyperAcq_zpixel_text.setText(_translate("MainWindow", "Z Pixels:"))
        self.HyperAcq_zpixel.setText(_translate("MainWindow", "1"))
        self.HyperAcq_xystep_text.setText(_translate("MainWindow", "XY Step Size (μm):"))
        self.HyperAcq_zstep_text.setText(_translate("MainWindow", "Z Step Size (μm):"))
        self.HyperAcq_zstep.setText(_translate("MainWindow", "0.5"))
        self.HyperAcq_xystep.setText(_translate("MainWindow", "0.3"))
        self.SpectralAcq_time_req_8.setText(_translate("MainWindow", "0.00"))
        self.HyperAcq_est_time_text.setText(_translate("MainWindow", "Estimated Time (min):"))
        self.HyperAcq_start.setText(_translate("MainWindow", "Start HSI Acquisition"))

from pyqtgraph import ImageView, PlotWidget
