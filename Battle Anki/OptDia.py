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


class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        OptionsDialog.resize(270, 480)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OptionsDialog.sizePolicy().hasHeightForWidth())
        OptionsDialog.setSizePolicy(sizePolicy)
        OptionsDialog.setMinimumSize(QtCore.QSize(270, 480))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        OptionsDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        OptionsDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(OptionsDialog)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 6, -1, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lab_opt_tit = QtWidgets.QLabel(OptionsDialog)
        self.lab_opt_tit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_opt_tit.sizePolicy().hasHeightForWidth())
        self.lab_opt_tit.setSizePolicy(sizePolicy)
        self.lab_opt_tit.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lab_opt_tit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_opt_tit.setWordWrap(True)
        self.lab_opt_tit.setObjectName("lab_opt_tit")
        self.verticalLayout_6.addWidget(self.lab_opt_tit)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(OptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(180, 380))
        self.frame.setMaximumSize(QtCore.QSize(180, 380))
        self.frame.setBaseSize(QtCore.QSize(173, 320))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setContentsMargins(0, 6, 0, 10)
        self.verticalLayout_14.setSpacing(7)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.numcards_layout = QtWidgets.QHBoxLayout()
        self.numcards_layout.setContentsMargins(0, -1, 0, -1)
        self.numcards_layout.setSpacing(5)
        self.numcards_layout.setObjectName("numcards_layout")
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.numcards_layout.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinbox_bdecksize_opts = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinbox_bdecksize_opts.sizePolicy().hasHeightForWidth()
        )
        self.spinbox_bdecksize_opts.setSizePolicy(sizePolicy)
        self.spinbox_bdecksize_opts.setMinimumSize(QtCore.QSize(80, 25))
        self.spinbox_bdecksize_opts.setMaximumSize(QtCore.QSize(100, 25))
        self.spinbox_bdecksize_opts.setBaseSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.spinbox_bdecksize_opts.setFont(font)
        self.spinbox_bdecksize_opts.setMouseTracking(True)
        self.spinbox_bdecksize_opts.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus
        )
        self.spinbox_bdecksize_opts.setMaximum(500)
        self.spinbox_bdecksize_opts.setProperty("value", 100)
        self.spinbox_bdecksize_opts.setObjectName("spinbox_bdecksize_opts")
        self.horizontalLayout_4.addWidget(self.spinbox_bdecksize_opts)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lab_max_cards = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_max_cards.sizePolicy().hasHeightForWidth()
        )
        self.lab_max_cards.setSizePolicy(sizePolicy)
        self.lab_max_cards.setMinimumSize(QtCore.QSize(80, 13))
        self.lab_max_cards.setMaximumSize(QtCore.QSize(80, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_max_cards.setFont(font)
        self.lab_max_cards.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_max_cards.setObjectName("lab_max_cards")
        self.horizontalLayout_3.addWidget(self.lab_max_cards)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.numcards_layout.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.numcards_layout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.numcards_layout, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_4.setContentsMargins(5, 7, 3, 5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_match_q = QtWidgets.QCheckBox(self.frame)
        self.checkBox_match_q.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_match_q.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_match_q.setSizePolicy(sizePolicy)
        self.checkBox_match_q.setMinimumSize(QtCore.QSize(0, 13))
        self.checkBox_match_q.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_match_q.setFont(font)
        self.checkBox_match_q.setCheckable(False)
        self.checkBox_match_q.setObjectName("checkBox_match_q")
        self.verticalLayout_4.addWidget(self.checkBox_match_q)
        self.lab_matched_desc = QtWidgets.QLabel(self.frame)
        self.lab_matched_desc.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_matched_desc.sizePolicy().hasHeightForWidth()
        )
        self.lab_matched_desc.setSizePolicy(sizePolicy)
        self.lab_matched_desc.setMaximumSize(QtCore.QSize(185, 16777215))
        self.lab_matched_desc.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_matched_desc.setWordWrap(True)
        self.lab_matched_desc.setIndent(0)
        self.lab_matched_desc.setObjectName("lab_matched_desc")
        self.verticalLayout_4.addWidget(self.lab_matched_desc)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_ctype = QtWidgets.QFrame(self.frame)
        self.frame_ctype.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_ctype.sizePolicy().hasHeightForWidth())
        self.frame_ctype.setSizePolicy(sizePolicy)
        self.frame_ctype.setMinimumSize(QtCore.QSize(75, 0))
        self.frame_ctype.setAutoFillBackground(False)
        self.frame_ctype.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_ctype.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_ctype.setObjectName("frame_ctype")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_ctype)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lab_cardtype = QtWidgets.QLabel(self.frame_ctype)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_cardtype.sizePolicy().hasHeightForWidth())
        self.lab_cardtype.setSizePolicy(sizePolicy)
        self.lab_cardtype.setMinimumSize(QtCore.QSize(0, 13))
        self.lab_cardtype.setMaximumSize(QtCore.QSize(70, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lab_cardtype.setFont(font)
        self.lab_cardtype.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_cardtype.setObjectName("lab_cardtype")
        self.horizontalLayout_17.addWidget(self.lab_cardtype)
        self.verticalLayout_18.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lab_cardtype_2 = QtWidgets.QLabel(self.frame_ctype)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_cardtype_2.sizePolicy().hasHeightForWidth()
        )
        self.lab_cardtype_2.setSizePolicy(sizePolicy)
        self.lab_cardtype_2.setMinimumSize(QtCore.QSize(0, 26))
        self.lab_cardtype_2.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_cardtype_2.setFont(font)
        self.lab_cardtype_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.lab_cardtype_2.setWordWrap(False)
        self.lab_cardtype_2.setObjectName("lab_cardtype_2")
        self.horizontalLayout_18.addWidget(self.lab_cardtype_2)
        self.verticalLayout_18.addLayout(self.horizontalLayout_18)
        self.verticalLayout_2.addLayout(self.verticalLayout_18)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(3, -1, -1, -1)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.checkBox_card_learn = QtWidgets.QCheckBox(self.frame_ctype)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_card_learn.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_card_learn.setSizePolicy(sizePolicy)
        self.checkBox_card_learn.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_card_learn.setFont(font)
        self.checkBox_card_learn.setChecked(True)
        self.checkBox_card_learn.setAutoExclusive(True)
        self.checkBox_card_learn.setObjectName("checkBox_card_learn")
        self.verticalLayout_15.addWidget(self.checkBox_card_learn)
        self.checkBox_newANDreview = QtWidgets.QCheckBox(self.frame_ctype)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_newANDreview.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_newANDreview.setSizePolicy(sizePolicy)
        self.checkBox_newANDreview.setMaximumSize(QtCore.QSize(60, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_newANDreview.setFont(font)
        self.checkBox_newANDreview.setAutoExclusive(True)
        self.checkBox_newANDreview.setObjectName("checkBox_newANDreview")
        self.verticalLayout_15.addWidget(self.checkBox_newANDreview)
        self.checkBox_card_new = QtWidgets.QCheckBox(self.frame_ctype)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_card_new.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_card_new.setSizePolicy(sizePolicy)
        self.checkBox_card_new.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_card_new.setFont(font)
        self.checkBox_card_new.setAutoExclusive(True)
        self.checkBox_card_new.setObjectName("checkBox_card_new")
        self.verticalLayout_15.addWidget(self.checkBox_card_new)
        self.verticalLayout_2.addLayout(self.verticalLayout_15)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.horizontalLayout_11.addWidget(self.frame_ctype)
        self.frame_corder = QtWidgets.QFrame(self.frame)
        self.frame_corder.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_corder.sizePolicy().hasHeightForWidth())
        self.frame_corder.setSizePolicy(sizePolicy)
        self.frame_corder.setMinimumSize(QtCore.QSize(91, 0))
        self.frame_corder.setMaximumSize(QtCore.QSize(91, 16777215))
        self.frame_corder.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_corder.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_corder.setObjectName("frame_corder")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_corder)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_16.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lab_cardtype_3 = QtWidgets.QLabel(self.frame_corder)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_cardtype_3.sizePolicy().hasHeightForWidth()
        )
        self.lab_cardtype_3.setSizePolicy(sizePolicy)
        self.lab_cardtype_3.setMinimumSize(QtCore.QSize(0, 13))
        self.lab_cardtype_3.setMaximumSize(QtCore.QSize(83, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lab_cardtype_3.setFont(font)
        self.lab_cardtype_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_cardtype_3.setObjectName("lab_cardtype_3")
        self.horizontalLayout_14.addWidget(self.lab_cardtype_3)
        self.verticalLayout_19.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lab_cardtype_4 = QtWidgets.QLabel(self.frame_corder)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_cardtype_4.sizePolicy().hasHeightForWidth()
        )
        self.lab_cardtype_4.setSizePolicy(sizePolicy)
        self.lab_cardtype_4.setMinimumSize(QtCore.QSize(0, 26))
        self.lab_cardtype_4.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_cardtype_4.setFont(font)
        self.lab_cardtype_4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.lab_cardtype_4.setWordWrap(False)
        self.lab_cardtype_4.setObjectName("lab_cardtype_4")
        self.horizontalLayout_16.addWidget(self.lab_cardtype_4)
        self.verticalLayout_19.addLayout(self.horizontalLayout_16)
        self.verticalLayout_16.addLayout(self.verticalLayout_19)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetFixedSize
        )
        self.verticalLayout_17.setContentsMargins(3, 0, -1, 0)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.radioButton_random = QtWidgets.QRadioButton(self.frame_corder)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.radioButton_random.sizePolicy().hasHeightForWidth()
        )
        self.radioButton_random.setSizePolicy(sizePolicy)
        self.radioButton_random.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_random.setFont(font)
        self.radioButton_random.setChecked(False)
        self.radioButton_random.setAutoExclusive(True)
        self.radioButton_random.setObjectName("radioButton_random")
        self.verticalLayout_17.addWidget(self.radioButton_random)
        self.radioButton_due = QtWidgets.QRadioButton(self.frame_corder)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.radioButton_due.sizePolicy().hasHeightForWidth()
        )
        self.radioButton_due.setSizePolicy(sizePolicy)
        self.radioButton_due.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_due.setFont(font)
        self.radioButton_due.setAutoExclusive(True)
        self.radioButton_due.setObjectName("radioButton_due")
        self.verticalLayout_17.addWidget(self.radioButton_due)
        self.radioButton_odue = QtWidgets.QRadioButton(self.frame_corder)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.radioButton_odue.sizePolicy().hasHeightForWidth()
        )
        self.radioButton_odue.setSizePolicy(sizePolicy)
        self.radioButton_odue.setMinimumSize(QtCore.QSize(22, 0))
        self.radioButton_odue.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_odue.setFont(font)
        self.radioButton_odue.setChecked(True)
        self.radioButton_odue.setAutoExclusive(True)
        self.radioButton_odue.setObjectName("radioButton_odue")
        self.verticalLayout_17.addWidget(self.radioButton_odue)
        self.verticalLayout_16.addLayout(self.verticalLayout_17)
        self.horizontalLayout_13.addLayout(self.verticalLayout_16)
        self.horizontalLayout_11.addWidget(self.frame_corder)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setContentsMargins(6, -1, -1, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.checkBox_card_mature = QtWidgets.QCheckBox(self.frame)
        self.checkBox_card_mature.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_card_mature.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_card_mature.setSizePolicy(sizePolicy)
        self.checkBox_card_mature.setMinimumSize(QtCore.QSize(0, 13))
        self.checkBox_card_mature.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_card_mature.setFont(font)
        self.checkBox_card_mature.setToolTipDuration(-1)
        self.checkBox_card_mature.setCheckable(False)
        self.checkBox_card_mature.setAutoExclusive(True)
        self.checkBox_card_mature.setObjectName("checkBox_card_mature")
        self.verticalLayout_20.addWidget(self.checkBox_card_mature)
        self.verticalLayout_14.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_21.setContentsMargins(6, 1, -1, 3)
        self.verticalLayout_21.setSpacing(1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.checkBox_apply_resched = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_apply_resched.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_apply_resched.setSizePolicy(sizePolicy)
        self.checkBox_apply_resched.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox_apply_resched.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_apply_resched.setFont(font)
        self.checkBox_apply_resched.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_apply_resched.setChecked(True)
        self.checkBox_apply_resched.setTristate(False)
        self.checkBox_apply_resched.setObjectName("checkBox_apply_resched")
        self.verticalLayout_21.addWidget(self.checkBox_apply_resched)
        self.lab_based_on_answers = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_based_on_answers.sizePolicy().hasHeightForWidth()
        )
        self.lab_based_on_answers.setSizePolicy(sizePolicy)
        self.lab_based_on_answers.setMinimumSize(QtCore.QSize(0, 20))
        self.lab_based_on_answers.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_based_on_answers.setFont(font)
        self.lab_based_on_answers.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_based_on_answers.setWordWrap(True)
        self.lab_based_on_answers.setIndent(20)
        self.lab_based_on_answers.setObjectName("lab_based_on_answers")
        self.verticalLayout_21.addWidget(self.lab_based_on_answers)
        self.checkBox_todayonly = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_todayonly.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_todayonly.setSizePolicy(sizePolicy)
        self.checkBox_todayonly.setMinimumSize(QtCore.QSize(0, 18))
        self.checkBox_todayonly.setMaximumSize(QtCore.QSize(120, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_todayonly.setFont(font)
        self.checkBox_todayonly.setChecked(True)
        self.checkBox_todayonly.setTristate(False)
        self.checkBox_todayonly.setObjectName("checkBox_todayonly")
        self.verticalLayout_21.addWidget(self.checkBox_todayonly)
        self.lab_today_only_explain = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_today_only_explain.sizePolicy().hasHeightForWidth()
        )
        self.lab_today_only_explain.setSizePolicy(sizePolicy)
        self.lab_today_only_explain.setMinimumSize(QtCore.QSize(0, 13))
        self.lab_today_only_explain.setWordWrap(False)
        self.lab_today_only_explain.setIndent(20)
        self.lab_today_only_explain.setObjectName("lab_today_only_explain")
        self.verticalLayout_21.addWidget(self.lab_today_only_explain)
        self.checkBox_no_overdue = QtWidgets.QCheckBox(self.frame)
        self.checkBox_no_overdue.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_no_overdue.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_no_overdue.setSizePolicy(sizePolicy)
        self.checkBox_no_overdue.setMinimumSize(QtCore.QSize(0, 18))
        self.checkBox_no_overdue.setMaximumSize(QtCore.QSize(220, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_no_overdue.setFont(font)
        self.checkBox_no_overdue.setCheckable(False)
        self.checkBox_no_overdue.setChecked(False)
        self.checkBox_no_overdue.setTristate(False)
        self.checkBox_no_overdue.setObjectName("checkBox_no_overdue")
        self.verticalLayout_21.addWidget(self.checkBox_no_overdue)
        self.verticalLayout_14.addLayout(self.verticalLayout_21)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.checkBox_joins = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkBox_joins.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_joins.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_joins.setFont(font)
        self.checkBox_joins.setChecked(True)
        self.checkBox_joins.setObjectName("checkBox_joins")
        self.verticalLayout_13.addWidget(
            self.checkBox_joins, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(40, -1, 40, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.but_apply = QtWidgets.QPushButton(OptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_apply.sizePolicy().hasHeightForWidth())
        self.but_apply.setSizePolicy(sizePolicy)
        self.but_apply.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.but_apply.setFont(font)
        self.but_apply.setFlat(False)
        self.but_apply.setObjectName("but_apply")
        self.horizontalLayout_5.addWidget(self.but_apply)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem3)
        self.label_version = myLabel(OptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_version.sizePolicy().hasHeightForWidth()
        )
        self.label_version.setSizePolicy(sizePolicy)
        self.label_version.setMinimumSize(QtCore.QSize(0, 9))
        self.label_version.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_version.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_version.setBaseSize(QtCore.QSize(31, 10))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_version.setFont(font)
        self.label_version.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom
            | QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
        )
        self.label_version.setObjectName("label_version")
        self.horizontalLayout.addWidget(self.label_version)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 100)
        self.verticalLayout.setStretch(1, 100)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(OptionsDialog)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)

    def retranslateUi(self, OptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        OptionsDialog.setWindowTitle(_translate("OptionsDialog", "Battle Anki Options"))
        self.lab_opt_tit.setText(
            _translate(
                "OptionsDialog",
                "Please note: some older, infequently used options and future options are temporarily disabled.",
            )
        )
        self.spinbox_bdecksize_opts.setSuffix(_translate("OptionsDialog", " cards"))
        self.lab_max_cards.setText(_translate("OptionsDialog", "Max 500 cards"))
        self.checkBox_match_q.setText(_translate("OptionsDialog", "Matched Deck?"))
        self.lab_matched_desc.setText(
            _translate("OptionsDialog", "Identical cards for both players")
        )
        self.lab_cardtype.setText(_translate("OptionsDialog", "Card Type"))
        self.lab_cardtype_2.setText(_translate("OptionsDialog", "for\n" "both players"))
        self.checkBox_card_learn.setText(_translate("OptionsDialog", "Review"))
        self.checkBox_newANDreview.setText(_translate("OptionsDialog", "Both"))
        self.checkBox_card_new.setText(_translate("OptionsDialog", "New"))
        self.lab_cardtype_3.setText(_translate("OptionsDialog", "Card Order"))
        self.lab_cardtype_4.setText(_translate("OptionsDialog", "for\n" "you only"))
        self.radioButton_random.setText(_translate("OptionsDialog", "Random"))
        self.radioButton_due.setText(_translate("OptionsDialog", "Order Due"))
        self.radioButton_odue.setText(
            _translate("OptionsDialog", "Relative\n" "Overdueness")
        )
        self.checkBox_card_mature.setText(
            _translate("OptionsDialog", "Mature cards only")
        )
        self.checkBox_apply_resched.setText(
            _translate("OptionsDialog", "Apply rescheduling?")
        )
        self.lab_based_on_answers.setText(
            _translate(
                "OptionsDialog", "if left unchecked, these\n" "cards won't count"
            )
        )
        self.checkBox_todayonly.setText(_translate("OptionsDialog", "Bailey Mode"))
        self.lab_today_only_explain.setText(
            _translate("OptionsDialog", "cards due today and overdue")
        )
        self.checkBox_no_overdue.setText(
            _translate("OptionsDialog", "Exclude overdues")
        )
        self.checkBox_joins.setText(
            _translate("OptionsDialog", "Accept joins while in battle")
        )
        self.but_apply.setText(_translate("OptionsDialog", "Apply"))
        self.label_version.setText(_translate("OptionsDialog", "v2.08"))


from .myclass import myLabel
