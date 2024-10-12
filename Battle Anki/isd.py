#                     Copyright © 2020-2022 Joseph Policarpio

#     Anki with Friends (previously Battle Anki) is an add-on for Anki,
#     a program for studying flash cards.

#     This file is part of Battle Anki
#
#     Battle Anki is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License (AGPL)
#     version 3 of the License, as published by the Free Software Foundation.
#                               AGPL-3.0-only.
#
#     Battle Anki is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_in_dis(object):
    def setupUi(self, Dialog_in_dis):
        Dialog_in_dis.setObjectName("Dialog_in_dis")
        Dialog_in_dis.resize(574, 498)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_in_dis.sizePolicy().hasHeightForWidth())
        Dialog_in_dis.setSizePolicy(sizePolicy)
        Dialog_in_dis.setMinimumSize(QtCore.QSize(574, 498))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        Dialog_in_dis.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_in_dis)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog_in_dis)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            50,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem)
        self.lab_text = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab_text.setFont(font)
        self.lab_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_text.setWordWrap(True)
        self.lab_text.setObjectName("lab_text")
        self.horizontalLayout.addWidget(self.lab_text)
        spacerItem1 = QtWidgets.QSpacerItem(
            50,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
        )
        self.verticalLayout_2.addItem(spacerItem2)
        self.lab_pid = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lab_pid.setFont(font)
        self.lab_pid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_pid.setWordWrap(True)
        self.lab_pid.setObjectName("lab_pid")
        self.verticalLayout_2.addWidget(self.lab_pid)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
        )
        self.verticalLayout_2.addItem(spacerItem3)
        self.lab_text_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_text_3.setFont(font)
        self.lab_text_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_text_3.setWordWrap(True)
        self.lab_text_3.setObjectName("lab_text_3")
        self.verticalLayout_2.addWidget(self.lab_text_3)
        self.lab_link = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lab_link.setFont(font)
        self.lab_link.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lab_link.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lab_link.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lab_link.setScaledContents(False)
        self.lab_link.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_link.setOpenExternalLinks(True)
        self.lab_link.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.lab_link.setObjectName("lab_link")
        self.verticalLayout_2.addWidget(self.lab_link)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(5, 4)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog_in_dis)
        QtCore.QMetaObject.connectSlotsByName(Dialog_in_dis)

    def retranslateUi(self, Dialog_in_dis):
        _translate = QtCore.QCoreApplication.translate
        Dialog_in_dis.setWindowTitle(
            _translate("Dialog_in_dis", "Anki Gamification Research Study")
        )
        self.lab_text.setText(
            _translate(
                "Dialog_in_dis",
                "You have successfully enrolled in the research study!!!\n"
                "\n"
                "Your participant ID is:",
            )
        )
        self.lab_pid.setText(_translate("Dialog_in_dis", "(not yet entered)"))
        self.lab_text_3.setText(
            _translate(
                "Dialog_in_dis",
                "For the current time period, gamification features are disabled...\n"
                "\n"
                "Please continue studying as usual, with your typical study routine.\n"
                "\n"
                "On 11/29/2021 at 12:01 AM, gamification features will be enabled, and a different window will appear instead of this one.\n"
                "",
            )
        )
        self.lab_link.setText(
            _translate(
                "Dialog_in_dis",
                '<html><head/><body><p><a href="https://battleanki.com/"><span style=" text-decoration: underline; color:#0000ff;">www.battleanki.com</span></a></p><p><a href="https://ankiweb.net/shared/info/613520216"><span style=" text-decoration: underline; color:#0000ff;">Battle Anki add-on page (Ankiweb)</span></a></p></body></html>',
            )
        )
