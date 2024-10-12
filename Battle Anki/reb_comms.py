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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 150)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        Dialog.setWindowIcon(icon)
        self.buttonBox_reb_comms = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox_reb_comms.setGeometry(QtCore.QRect(40, 100, 161, 32))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonBox_reb_comms.sizePolicy().hasHeightForWidth()
        )
        self.buttonBox_reb_comms.setSizePolicy(sizePolicy)
        self.buttonBox_reb_comms.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox_reb_comms.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Help
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.buttonBox_reb_comms.setCenterButtons(True)
        self.buttonBox_reb_comms.setObjectName("buttonBox_reb_comms")
        self.lab_reb_comms_title = QtWidgets.QLabel(Dialog)
        self.lab_reb_comms_title.setGeometry(QtCore.QRect(40, 20, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_reb_comms_title.sizePolicy().hasHeightForWidth()
        )
        self.lab_reb_comms_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lab_reb_comms_title.setFont(font)
        self.lab_reb_comms_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_reb_comms_title.setObjectName("lab_reb_comms_title")

        self.retranslateUi(Dialog)
        self.buttonBox_reb_comms.accepted.connect(Dialog.accept)
        self.buttonBox_reb_comms.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Information"))
        self.lab_reb_comms_title.setText(
            _translate("Dialog", "They accepted!\n" "\n" "The game has started!")
        )
