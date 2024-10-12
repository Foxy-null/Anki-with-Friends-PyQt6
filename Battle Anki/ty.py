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


class Ui_Dialog_ty(object):
    def setupUi(self, Dialog_ty):
        Dialog_ty.setObjectName("Dialog_ty")
        Dialog_ty.resize(574, 498)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        Dialog_ty.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_ty)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            50,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem)
        self.lab_text = QtWidgets.QLabel(Dialog_ty)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lab_link = QtWidgets.QLabel(Dialog_ty)
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
        self.verticalLayout.addWidget(self.lab_link)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog_ty)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ty)

    def retranslateUi(self, Dialog_ty):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ty.setWindowTitle(
            _translate("Dialog_ty", "Battle Anki Version 3 Coming Soon!")
        )
        self.lab_text.setText(
            _translate(
                "Dialog_ty",
                "Battle Anki is currently running a research study...\n"
                "\n"
                "Unfortunately, the public version of Battle Anki will be unavailable during that time.\n"
                "\n"
                "IF YOU ARE ENROLLED IN THE STUDY, please check for an update on Sunday 11/7/2021 evening.\n"
                "\n"
                "\n"
                "For more information visit our website:",
            )
        )
        self.lab_link.setText(
            _translate(
                "Dialog_ty",
                '<html><head/><body><p><a href="https://battleanki.com/"><span style=" text-decoration: underline; color:#0000ff;">www.battleanki.com</span></a></p><p><br/></p><p><a href="https://ankiweb.net/shared/info/613520216"><span style=" text-decoration: underline; color:#0000ff;">Battle Anki add-on page (Ankiweb)</span></a></p></body></html>',
            )
        )
