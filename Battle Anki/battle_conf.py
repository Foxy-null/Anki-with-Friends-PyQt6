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


class Ui_bat_conf_Dialog(object):
    def setupUi(self, bat_conf_Dialog):
        bat_conf_Dialog.setObjectName("bat_conf_Dialog")
        bat_conf_Dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        bat_conf_Dialog.resize(320, 300)
        bat_conf_Dialog.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        bat_conf_Dialog.setWindowIcon(icon)
        bat_conf_Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(bat_conf_Dialog)
        self.verticalLayout.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_dialog_text = QtWidgets.QLabel(bat_conf_Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lab_dialog_text.setFont(font)
        self.lab_dialog_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_dialog_text.setWordWrap(True)
        self.lab_dialog_text.setObjectName("lab_dialog_text")
        self.verticalLayout.addWidget(self.lab_dialog_text)
        self.buttonBox_conf_dialog = QtWidgets.QDialogButtonBox(bat_conf_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonBox_conf_dialog.sizePolicy().hasHeightForWidth()
        )
        self.buttonBox_conf_dialog.setSizePolicy(sizePolicy)
        self.buttonBox_conf_dialog.setAutoFillBackground(False)
        self.buttonBox_conf_dialog.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox_conf_dialog.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        self.buttonBox_conf_dialog.setCenterButtons(True)
        self.buttonBox_conf_dialog.setObjectName("buttonBox_conf_dialog")
        self.verticalLayout.addWidget(self.buttonBox_conf_dialog)

        self.retranslateUi(bat_conf_Dialog)
        self.buttonBox_conf_dialog.accepted.connect(bat_conf_Dialog.accept)
        self.buttonBox_conf_dialog.rejected.connect(bat_conf_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(bat_conf_Dialog)

    def retranslateUi(self, bat_conf_Dialog):
        _translate = QtCore.QCoreApplication.translate
        bat_conf_Dialog.setWindowTitle(
            _translate("bat_conf_Dialog", "Confirmation dialog")
        )
        self.lab_dialog_text.setText(
            _translate(
                "bat_conf_Dialog",
                "Multiplayer mode is now available!\n"
                "(up to 6 players per battle)\n"
                "\n"
                "Before clicking 'Send Request',\n"
                "highlight everyone you'd like to play with.\n"
                "\n"
                "Click Cancel to select more players, or\n"
                "\n"
                "Click OK to send the request\n"
                "to everyone highlighted...",
            )
        )
