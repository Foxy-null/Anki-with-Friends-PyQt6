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


class Ui_AskDialog(object):
    def setupUi(self, AskDialog):
        AskDialog.setObjectName("AskDialog")
        AskDialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        AskDialog.resize(500, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AskDialog.sizePolicy().hasHeightForWidth())
        AskDialog.setSizePolicy(sizePolicy)
        AskDialog.setMinimumSize(QtCore.QSize(500, 600))
        AskDialog.setMaximumSize(QtCore.QSize(500, 600))
        AskDialog.setBaseSize(QtCore.QSize(500, 600))
        font = QtGui.QFont()
        font.setPointSize(13)
        AskDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        AskDialog.setWindowIcon(icon)
        AskDialog.setStyleSheet("")
        AskDialog.setSizeGripEnabled(False)
        self.back_label = QtWidgets.QLabel(AskDialog)
        self.back_label.setGeometry(QtCore.QRect(0, 0, 500, 600))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_label.sizePolicy().hasHeightForWidth())
        self.back_label.setSizePolicy(sizePolicy)
        self.back_label.setText("")
        self.back_label.setObjectName("back_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(AskDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            80,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            100,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout_10.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lab_ask_bd_title_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_ask_bd_title_8.sizePolicy().hasHeightForWidth()
        )
        self.lab_ask_bd_title_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Edwardian Script ITC")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.lab_ask_bd_title_8.setFont(font)
        self.lab_ask_bd_title_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_ask_bd_title_8.setObjectName("lab_ask_bd_title_8")
        self.horizontalLayout_10.addWidget(self.lab_ask_bd_title_8)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem2)
        self.lab_logo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_logo.sizePolicy().hasHeightForWidth())
        self.lab_logo.setSizePolicy(sizePolicy)
        self.lab_logo.setMinimumSize(QtCore.QSize(50, 50))
        self.lab_logo.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lab_logo.setFont(font)
        self.lab_logo.setText("")
        self.lab_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_logo.setObjectName("lab_logo")
        self.horizontalLayout_10.addWidget(self.lab_logo)
        spacerItem3 = QtWidgets.QSpacerItem(
            15,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lab_ask_bd_title_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_ask_bd_title_9.setFont(font)
        self.lab_ask_bd_title_9.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom
            | QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.lab_ask_bd_title_9.setIndent(0)
        self.lab_ask_bd_title_9.setObjectName("lab_ask_bd_title_9")
        self.verticalLayout_4.addWidget(self.lab_ask_bd_title_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lab_ask_bd_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_ask_bd_name.sizePolicy().hasHeightForWidth()
        )
        self.lab_ask_bd_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lab_ask_bd_name.setFont(font)
        self.lab_ask_bd_name.setAutoFillBackground(False)
        self.lab_ask_bd_name.setStyleSheet("")
        self.lab_ask_bd_name.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.lab_ask_bd_name.setScaledContents(False)
        self.lab_ask_bd_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_ask_bd_name.setWordWrap(True)
        self.lab_ask_bd_name.setObjectName("lab_ask_bd_name")
        self.horizontalLayout_11.addWidget(self.lab_ask_bd_name)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.lab_ask_bd_title_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_ask_bd_title_10.sizePolicy().hasHeightForWidth()
        )
        self.lab_ask_bd_title_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_ask_bd_title_10.setFont(font)
        self.lab_ask_bd_title_10.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.lab_ask_bd_title_10.setWordWrap(True)
        self.lab_ask_bd_title_10.setIndent(0)
        self.lab_ask_bd_title_10.setObjectName("lab_ask_bd_title_10")
        self.verticalLayout_4.addWidget(self.lab_ask_bd_title_10)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(
            1,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem4)
        self.val_decksize = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_decksize.sizePolicy().hasHeightForWidth())
        self.val_decksize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.val_decksize.setFont(font)
        self.val_decksize.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.val_decksize.setWordWrap(True)
        self.val_decksize.setIndent(0)
        self.val_decksize.setObjectName("val_decksize")
        self.horizontalLayout_2.addWidget(self.val_decksize)
        self.val_cardtype = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_cardtype.sizePolicy().hasHeightForWidth())
        self.val_cardtype.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.val_cardtype.setFont(font)
        self.val_cardtype.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.val_cardtype.setWordWrap(True)
        self.val_cardtype.setIndent(10)
        self.val_cardtype.setObjectName("val_cardtype")
        self.horizontalLayout_2.addWidget(self.val_cardtype)
        self.lab_cards = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_cards.sizePolicy().hasHeightForWidth())
        self.lab_cards.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_cards.setFont(font)
        self.lab_cards.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_cards.setWordWrap(True)
        self.lab_cards.setIndent(10)
        self.lab_cards.setObjectName("lab_cards")
        self.horizontalLayout_2.addWidget(self.lab_cards)
        spacerItem5 = QtWidgets.QSpacerItem(
            1,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(
            1,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_13.addItem(spacerItem6)
        self.lab_that_Are = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_that_Are.sizePolicy().hasHeightForWidth())
        self.lab_that_Are.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_that_Are.setFont(font)
        self.lab_that_Are.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_that_Are.setWordWrap(True)
        self.lab_that_Are.setIndent(0)
        self.lab_that_Are.setObjectName("lab_that_Are")
        self.horizontalLayout_13.addWidget(self.lab_that_Are)
        self.val_today_only = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.val_today_only.sizePolicy().hasHeightForWidth()
        )
        self.val_today_only.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.val_today_only.setFont(font)
        self.val_today_only.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.val_today_only.setWordWrap(True)
        self.val_today_only.setIndent(8)
        self.val_today_only.setObjectName("val_today_only")
        self.horizontalLayout_13.addWidget(self.val_today_only)
        self.lab_due_today = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_due_today.sizePolicy().hasHeightForWidth()
        )
        self.lab_due_today.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_due_today.setFont(font)
        self.lab_due_today.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_due_today.setWordWrap(True)
        self.lab_due_today.setIndent(8)
        self.lab_due_today.setObjectName("lab_due_today")
        self.horizontalLayout_13.addWidget(self.lab_due_today)
        spacerItem7 = QtWidgets.QSpacerItem(
            0,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 3, -1, 3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem8 = QtWidgets.QSpacerItem(
            1,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_12.addItem(spacerItem8)
        self.lab_which_will = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_which_will.sizePolicy().hasHeightForWidth()
        )
        self.lab_which_will.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_which_will.setFont(font)
        self.lab_which_will.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_which_will.setWordWrap(True)
        self.lab_which_will.setIndent(0)
        self.lab_which_will.setObjectName("lab_which_will")
        self.horizontalLayout_12.addWidget(self.lab_which_will)
        self.val_resched = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_resched.sizePolicy().hasHeightForWidth())
        self.val_resched.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.val_resched.setFont(font)
        self.val_resched.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.val_resched.setWordWrap(True)
        self.val_resched.setIndent(8)
        self.val_resched.setObjectName("val_resched")
        self.horizontalLayout_12.addWidget(self.val_resched)
        self.lab_be_rescheduled = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_be_rescheduled.sizePolicy().hasHeightForWidth()
        )
        self.lab_be_rescheduled.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_be_rescheduled.setFont(font)
        self.lab_be_rescheduled.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_be_rescheduled.setWordWrap(True)
        self.lab_be_rescheduled.setIndent(8)
        self.lab_be_rescheduled.setObjectName("lab_be_rescheduled")
        self.horizontalLayout_12.addWidget(self.lab_be_rescheduled)
        spacerItem9 = QtWidgets.QSpacerItem(
            1,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_12.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.lab_basedonanswers = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_basedonanswers.sizePolicy().hasHeightForWidth()
        )
        self.lab_basedonanswers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_basedonanswers.setFont(font)
        self.lab_basedonanswers.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.lab_basedonanswers.setWordWrap(True)
        self.lab_basedonanswers.setIndent(0)
        self.lab_basedonanswers.setObjectName("lab_basedonanswers")
        self.verticalLayout_3.addWidget(self.lab_basedonanswers)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout.addItem(spacerItem10)
        self.lab_ask_bd_title_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_ask_bd_title_11.sizePolicy().hasHeightForWidth()
        )
        self.lab_ask_bd_title_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lab_ask_bd_title_11.setFont(font)
        self.lab_ask_bd_title_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_ask_bd_title_11.setWordWrap(True)
        self.lab_ask_bd_title_11.setIndent(0)
        self.lab_ask_bd_title_11.setObjectName("lab_ask_bd_title_11")
        self.verticalLayout.addWidget(self.lab_ask_bd_title_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, 10, 50, 10)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.but_yes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_yes.sizePolicy().hasHeightForWidth())
        self.but_yes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.but_yes.setFont(font)
        self.but_yes.setStyleSheet("")
        self.but_yes.setObjectName("but_yes")
        self.horizontalLayout_3.addWidget(self.but_yes)
        self.but_no = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_no.sizePolicy().hasHeightForWidth())
        self.but_no.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.but_no.setFont(font)
        self.but_no.setStyleSheet("")
        self.but_no.setObjectName("but_no")
        self.horizontalLayout_3.addWidget(self.but_no)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(
            20,
            90,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout.addItem(spacerItem11)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 5)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(
            60,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem12)

        self.retranslateUi(AskDialog)
        self.but_yes.clicked.connect(AskDialog.accept)
        self.but_no.clicked.connect(AskDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AskDialog)

    def retranslateUi(self, AskDialog):
        _translate = QtCore.QCoreApplication.translate
        AskDialog.setWindowTitle(_translate("AskDialog", "Battle Anki Request"))
        self.lab_ask_bd_title_8.setText(_translate("AskDialog", "Greetings,"))
        self.lab_ask_bd_title_9.setText(_translate("AskDialog", "Your colleague"))
        self.lab_ask_bd_name.setText(_translate("AskDialog", "(name)"))
        self.lab_ask_bd_title_10.setText(
            _translate(
                "AskDialog",
                "would like your help studying a Battle Deck with these options:",
            )
        )
        self.val_decksize.setText(_translate("AskDialog", "(decksize)"))
        self.val_cardtype.setText(_translate("AskDialog", "(cardtype)"))
        self.lab_cards.setText(_translate("AskDialog", "cards"))
        self.lab_that_Are.setText(_translate("AskDialog", "that are"))
        self.val_today_only.setText(_translate("AskDialog", "(all or not)"))
        self.lab_due_today.setText(_translate("AskDialog", "due today"))
        self.lab_which_will.setText(_translate("AskDialog", "which will"))
        self.val_resched.setText(_translate("AskDialog", "(not)"))
        self.lab_be_rescheduled.setText(_translate("AskDialog", "be rescheduled"))
        self.lab_basedonanswers.setText(
            _translate("AskDialog", "based on your answers")
        )
        self.lab_ask_bd_title_11.setText(
            _translate("AskDialog", "Would you like to play?")
        )
        self.but_yes.setText(_translate("AskDialog", "Yes"))
        self.but_no.setText(_translate("AskDialog", "No"))
