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


class Ui_BatMainWin(object):
    def setupUi(self, BatMainWin):
        BatMainWin.setObjectName("BatMainWin")
        BatMainWin.setEnabled(True)
        BatMainWin.resize(550, 410)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BatMainWin.sizePolicy().hasHeightForWidth())
        BatMainWin.setSizePolicy(sizePolicy)
        BatMainWin.setMinimumSize(QtCore.QSize(460, 410))
        BatMainWin.setMaximumSize(QtCore.QSize(550, 410))
        BatMainWin.setBaseSize(QtCore.QSize(550, 410))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        BatMainWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(BatMainWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(410, 410))
        self.centralwidget.setMaximumSize(QtCore.QSize(550, 410))
        self.centralwidget.setBaseSize(QtCore.QSize(550, 410))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stackedWidget.sizePolicy().hasHeightForWidth()
        )
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(410, 410))
        self.stackedWidget.setMaximumSize(QtCore.QSize(550, 410))
        self.stackedWidget.setBaseSize(QtCore.QSize(550, 410))
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy)
        self.page_1.setMinimumSize(QtCore.QSize(460, 410))
        self.page_1.setMaximumSize(QtCore.QSize(550, 410))
        self.page_1.setBaseSize(QtCore.QSize(460, 410))
        self.page_1.setObjectName("page_1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_8.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize
        )
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_blank_d = myLabel(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_blank_d.sizePolicy().hasHeightForWidth()
        )
        self.label_blank_d.setSizePolicy(sizePolicy)
        self.label_blank_d.setMinimumSize(QtCore.QSize(20, 20))
        self.label_blank_d.setMaximumSize(QtCore.QSize(20, 20))
        self.label_blank_d.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_blank_d.setBaseSize(QtCore.QSize(31, 10))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_blank_d.setFont(font)
        self.label_blank_d.setText("")
        self.label_blank_d.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_blank_d.setWordWrap(False)
        self.label_blank_d.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.NoTextInteraction
        )
        self.label_blank_d.setObjectName("label_blank_d")
        self.verticalLayout_4.addWidget(self.label_blank_d)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(
            10,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem1)
        self.lab_logo_home = QtWidgets.QLabel(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_logo_home.sizePolicy().hasHeightForWidth()
        )
        self.lab_logo_home.setSizePolicy(sizePolicy)
        self.lab_logo_home.setMinimumSize(QtCore.QSize(20, 20))
        self.lab_logo_home.setMaximumSize(QtCore.QSize(45, 45))
        self.lab_logo_home.setText("")
        self.lab_logo_home.setObjectName("lab_logo_home")
        self.horizontalLayout_5.addWidget(self.lab_logo_home)
        spacerItem2 = QtWidgets.QSpacerItem(
            10,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 5, 0, 10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_blank_r = myLabel(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_blank_r.sizePolicy().hasHeightForWidth()
        )
        self.label_blank_r.setSizePolicy(sizePolicy)
        self.label_blank_r.setMinimumSize(QtCore.QSize(19, 35))
        self.label_blank_r.setMaximumSize(QtCore.QSize(19, 35))
        self.label_blank_r.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_blank_r.setBaseSize(QtCore.QSize(31, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_blank_r.setFont(font)
        self.label_blank_r.setToolTip("")
        self.label_blank_r.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.label_blank_r.setIndent(-1)
        self.label_blank_r.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.NoTextInteraction
        )
        self.label_blank_r.setObjectName("label_blank_r")
        self.horizontalLayout_20.addWidget(self.label_blank_r)
        self.lab_welcome = QtWidgets.QLabel(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_welcome.sizePolicy().hasHeightForWidth())
        self.lab_welcome.setSizePolicy(sizePolicy)
        self.lab_welcome.setMinimumSize(QtCore.QSize(240, 35))
        self.lab_welcome.setMaximumSize(QtCore.QSize(240, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab_welcome.setFont(font)
        self.lab_welcome.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lab_welcome.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lab_welcome.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lab_welcome.setScaledContents(False)
        self.lab_welcome.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_welcome.setOpenExternalLinks(True)
        self.lab_welcome.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard
            | QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse
        )
        self.lab_welcome.setObjectName("lab_welcome")
        self.horizontalLayout_20.addWidget(self.lab_welcome)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(
            10,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem3)
        self.lab_logo_home_2 = QtWidgets.QLabel(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_logo_home_2.sizePolicy().hasHeightForWidth()
        )
        self.lab_logo_home_2.setSizePolicy(sizePolicy)
        self.lab_logo_home_2.setMinimumSize(QtCore.QSize(20, 20))
        self.lab_logo_home_2.setMaximumSize(QtCore.QSize(45, 45))
        self.lab_logo_home_2.setText("")
        self.lab_logo_home_2.setObjectName("lab_logo_home_2")
        self.horizontalLayout_6.addWidget(self.lab_logo_home_2)
        spacerItem4 = QtWidgets.QSpacerItem(
            10,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_6.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.tableWidget_users_connected = QtWidgets.QTableWidget(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget_users_connected.sizePolicy().hasHeightForWidth()
        )
        self.tableWidget_users_connected.setSizePolicy(sizePolicy)
        self.tableWidget_users_connected.setMinimumSize(QtCore.QSize(260, 270))
        self.tableWidget_users_connected.setMaximumSize(QtCore.QSize(340, 270))
        self.tableWidget_users_connected.setBaseSize(QtCore.QSize(250, 270))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active,
            QtGui.QPalette.ColorRole.AlternateBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.AlternateBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.AlternateBase,
            brush,
        )
        self.tableWidget_users_connected.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget_users_connected.setFont(font)
        self.tableWidget_users_connected.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor)
        )
        self.tableWidget_users_connected.setMouseTracking(True)
        self.tableWidget_users_connected.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget_users_connected.setContextMenuPolicy(
            QtCore.Qt.ContextMenuPolicy.NoContextMenu
        )
        self.tableWidget_users_connected.setAutoFillBackground(False)
        self.tableWidget_users_connected.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget_users_connected.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget_users_connected.setLineWidth(2)
        self.tableWidget_users_connected.setMidLineWidth(0)
        self.tableWidget_users_connected.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.tableWidget_users_connected.setAutoScroll(False)
        self.tableWidget_users_connected.setAutoScrollMargin(0)
        self.tableWidget_users_connected.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tableWidget_users_connected.setTabKeyNavigation(False)
        self.tableWidget_users_connected.setProperty("showDropIndicator", False)
        self.tableWidget_users_connected.setDragDropOverwriteMode(False)
        self.tableWidget_users_connected.setAlternatingRowColors(False)
        self.tableWidget_users_connected.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tableWidget_users_connected.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tableWidget_users_connected.setTextElideMode(
            QtCore.Qt.TextElideMode.ElideNone
        )
        self.tableWidget_users_connected.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        self.tableWidget_users_connected.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        self.tableWidget_users_connected.setShowGrid(False)
        self.tableWidget_users_connected.setWordWrap(False)
        self.tableWidget_users_connected.setCornerButtonEnabled(False)
        self.tableWidget_users_connected.setRowCount(0)
        self.tableWidget_users_connected.setColumnCount(4)
        self.tableWidget_users_connected.setObjectName("tableWidget_users_connected")
        self.tableWidget_users_connected.horizontalHeader().setVisible(False)
        self.tableWidget_users_connected.horizontalHeader().setDefaultSectionSize(45)
        self.tableWidget_users_connected.horizontalHeader().setHighlightSections(False)
        self.tableWidget_users_connected.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget_users_connected.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_users_connected.verticalHeader().setVisible(False)
        self.tableWidget_users_connected.verticalHeader().setDefaultSectionSize(33)
        self.tableWidget_users_connected.verticalHeader().setHighlightSections(False)
        self.tableWidget_users_connected.verticalHeader().setMinimumSectionSize(33)
        self.horizontalLayout_15.addWidget(self.tableWidget_users_connected)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout_2.setContentsMargins(5, 13, 5, 10)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.but_away = QtWidgets.QPushButton(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_away.sizePolicy().hasHeightForWidth())
        self.but_away.setSizePolicy(sizePolicy)
        self.but_away.setMinimumSize(QtCore.QSize(50, 30))
        self.but_away.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.but_away.setFont(font)
        self.but_away.setCheckable(True)
        self.but_away.setObjectName("but_away")
        self.horizontalLayout_2.addWidget(self.but_away)
        self.but_solo = QtWidgets.QPushButton(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_solo.sizePolicy().hasHeightForWidth())
        self.but_solo.setSizePolicy(sizePolicy)
        self.but_solo.setMinimumSize(QtCore.QSize(50, 30))
        self.but_solo.setMaximumSize(QtCore.QSize(70, 40))
        self.but_solo.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.but_solo.setFont(font)
        self.but_solo.setCheckable(False)
        self.but_solo.setObjectName("but_solo")
        self.horizontalLayout_2.addWidget(self.but_solo)
        self.but_join = QtWidgets.QPushButton(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_join.sizePolicy().hasHeightForWidth())
        self.but_join.setSizePolicy(sizePolicy)
        self.but_join.setMinimumSize(QtCore.QSize(50, 30))
        self.but_join.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.but_join.setFont(font)
        self.but_join.setFlat(False)
        self.but_join.setObjectName("but_join")
        self.horizontalLayout_2.addWidget(self.but_join)
        self.but_sendittt = QtWidgets.QPushButton(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_sendittt.sizePolicy().hasHeightForWidth())
        self.but_sendittt.setSizePolicy(sizePolicy)
        self.but_sendittt.setMinimumSize(QtCore.QSize(50, 30))
        self.but_sendittt.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.but_sendittt.setFont(font)
        self.but_sendittt.setObjectName("but_sendittt")
        self.horizontalLayout_2.addWidget(self.but_sendittt)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(173, 280))
        self.frame.setMaximumSize(QtCore.QSize(180, 350))
        self.frame.setBaseSize(QtCore.QSize(173, 320))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(8)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem5 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_14.addItem(spacerItem5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(
            0,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_9.addItem(spacerItem6)
        self.lab_pg1_opt_tit = QtWidgets.QLabel(self.frame)
        self.lab_pg1_opt_tit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.lab_pg1_opt_tit.setFont(font)
        self.lab_pg1_opt_tit.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_opt_tit.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.NoTextInteraction
        )
        self.lab_pg1_opt_tit.setObjectName("lab_pg1_opt_tit")
        self.horizontalLayout_9.addWidget(self.lab_pg1_opt_tit)
        self.lab_pg1_opt_tit_2 = QtWidgets.QLabel(self.frame)
        self.lab_pg1_opt_tit_2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.lab_pg1_opt_tit_2.setFont(font)
        self.lab_pg1_opt_tit_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_opt_tit_2.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.NoTextInteraction
        )
        self.lab_pg1_opt_tit_2.setObjectName("lab_pg1_opt_tit_2")
        self.horizontalLayout_9.addWidget(self.lab_pg1_opt_tit_2)
        spacerItem7 = QtWidgets.QSpacerItem(
            0,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.numcards_layout = QtWidgets.QHBoxLayout()
        self.numcards_layout.setContentsMargins(0, -1, 0, -1)
        self.numcards_layout.setSpacing(5)
        self.numcards_layout.setObjectName("numcards_layout")
        spacerItem8 = QtWidgets.QSpacerItem(
            10,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.numcards_layout.addItem(spacerItem8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.spinbox_bdecksize_bw = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinbox_bdecksize_bw.sizePolicy().hasHeightForWidth()
        )
        self.spinbox_bdecksize_bw.setSizePolicy(sizePolicy)
        self.spinbox_bdecksize_bw.setMinimumSize(QtCore.QSize(80, 25))
        self.spinbox_bdecksize_bw.setMaximumSize(QtCore.QSize(100, 25))
        self.spinbox_bdecksize_bw.setBaseSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.spinbox_bdecksize_bw.setFont(font)
        self.spinbox_bdecksize_bw.setMouseTracking(True)
        self.spinbox_bdecksize_bw.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus
        )
        self.spinbox_bdecksize_bw.setMaximum(500)
        self.spinbox_bdecksize_bw.setProperty("value", 100)
        self.spinbox_bdecksize_bw.setObjectName("spinbox_bdecksize_bw")
        self.horizontalLayout_11.addWidget(self.spinbox_bdecksize_bw)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lab_max_cards = QtWidgets.QLabel(self.frame)
        self.lab_max_cards.setEnabled(False)
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
        self.horizontalLayout_19.addWidget(self.lab_max_cards)
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.numcards_layout.addLayout(self.verticalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(
            10,
            20,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.numcards_layout.addItem(spacerItem9)
        self.verticalLayout_14.addLayout(self.numcards_layout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem10 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem10)
        self.lab_pg1_cards = QtWidgets.QLabel(self.frame)
        self.lab_pg1_cards.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_cards.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_cards.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_cards.setFont(font)
        self.lab_pg1_cards.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_cards.setObjectName("lab_pg1_cards")
        self.horizontalLayout_10.addWidget(self.lab_pg1_cards)
        self.lab_pg1_cardtype = QtWidgets.QLabel(self.frame)
        self.lab_pg1_cardtype.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_cardtype.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_cardtype.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_cardtype.setFont(font)
        self.lab_pg1_cardtype.setObjectName("lab_pg1_cardtype")
        self.horizontalLayout_10.addWidget(self.lab_pg1_cardtype)
        self.lab_pg1_tit_cards = QtWidgets.QLabel(self.frame)
        self.lab_pg1_tit_cards.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_tit_cards.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_tit_cards.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_tit_cards.setFont(font)
        self.lab_pg1_tit_cards.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_tit_cards.setObjectName("lab_pg1_tit_cards")
        self.horizontalLayout_10.addWidget(self.lab_pg1_tit_cards)
        spacerItem11 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem11)
        self.verticalLayout_14.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem12 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_17.addItem(spacerItem12)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lab_pg1_due_today = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_due_today.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_due_today.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_due_today.setFont(font)
        self.lab_pg1_due_today.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_pg1_due_today.setObjectName("lab_pg1_due_today")
        self.verticalLayout_2.addWidget(self.lab_pg1_due_today)
        self.lab_pg1_overdues = QtWidgets.QLabel(self.frame)
        self.lab_pg1_overdues.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_overdues.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_overdues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lab_pg1_overdues.setFont(font)
        self.lab_pg1_overdues.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_overdues.setObjectName("lab_pg1_overdues")
        self.verticalLayout_2.addWidget(self.lab_pg1_overdues)
        self.horizontalLayout_17.addLayout(self.verticalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_17.addItem(spacerItem13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem14 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_13.addItem(spacerItem14)
        self.lab_pg1_cardorder = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_cardorder.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_cardorder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lab_pg1_cardorder.setFont(font)
        self.lab_pg1_cardorder.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_cardorder.setObjectName("lab_pg1_cardorder")
        self.horizontalLayout_13.addWidget(self.lab_pg1_cardorder)
        self.lab_pg1_tit_cardorder = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_tit_cardorder.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_tit_cardorder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lab_pg1_tit_cardorder.setFont(font)
        self.lab_pg1_tit_cardorder.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_tit_cardorder.setObjectName("lab_pg1_tit_cardorder")
        self.horizontalLayout_13.addWidget(self.lab_pg1_tit_cardorder)
        spacerItem15 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_13.addItem(spacerItem15)
        self.verticalLayout_14.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem16 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_16.addItem(spacerItem16)
        self.lab_pg1_resched = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_resched.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_resched.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_resched.setFont(font)
        self.lab_pg1_resched.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_resched.setObjectName("lab_pg1_resched")
        self.horizontalLayout_16.addWidget(self.lab_pg1_resched)
        self.lab_pg1_tit_resched = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_tit_resched.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_tit_resched.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_tit_resched.setFont(font)
        self.lab_pg1_tit_resched.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_tit_resched.setWordWrap(False)
        self.lab_pg1_tit_resched.setObjectName("lab_pg1_tit_resched")
        self.horizontalLayout_16.addWidget(self.lab_pg1_tit_resched)
        spacerItem17 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_16.addItem(spacerItem17)
        self.verticalLayout_14.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem18 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_14.addItem(spacerItem18)
        self.lab_pg1_matched = QtWidgets.QLabel(self.frame)
        self.lab_pg1_matched.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_matched.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_matched.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_matched.setFont(font)
        self.lab_pg1_matched.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_matched.setObjectName("lab_pg1_matched")
        self.horizontalLayout_14.addWidget(self.lab_pg1_matched)
        self.lab_pg1_tit_matched = QtWidgets.QLabel(self.frame)
        self.lab_pg1_tit_matched.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_tit_matched.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_tit_matched.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_tit_matched.setFont(font)
        self.lab_pg1_tit_matched.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_tit_matched.setObjectName("lab_pg1_tit_matched")
        self.horizontalLayout_14.addWidget(self.lab_pg1_tit_matched)
        spacerItem19 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_14.addItem(spacerItem19)
        self.verticalLayout_14.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem20 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_18.addItem(spacerItem20)
        self.lab_pg1_joiners = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_joiners.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_joiners.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_pg1_joiners.setFont(font)
        self.lab_pg1_joiners.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_joiners.setObjectName("lab_pg1_joiners")
        self.horizontalLayout_18.addWidget(self.lab_pg1_joiners)
        self.lab_pg1_tit_joiners = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_pg1_tit_joiners.sizePolicy().hasHeightForWidth()
        )
        self.lab_pg1_tit_joiners.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lab_pg1_tit_joiners.setFont(font)
        self.lab_pg1_tit_joiners.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lab_pg1_tit_joiners.setWordWrap(False)
        self.lab_pg1_tit_joiners.setObjectName("lab_pg1_tit_joiners")
        self.horizontalLayout_18.addWidget(self.lab_pg1_tit_joiners)
        spacerItem21 = QtWidgets.QSpacerItem(
            0,
            0,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_18.addItem(spacerItem21)
        self.verticalLayout_14.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.but_options = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_options.sizePolicy().hasHeightForWidth())
        self.but_options.setSizePolicy(sizePolicy)
        self.but_options.setMinimumSize(QtCore.QSize(115, 35))
        self.but_options.setObjectName("but_options")
        self.horizontalLayout_7.addWidget(self.but_options)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        spacerItem22 = QtWidgets.QSpacerItem(
            20,
            120,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_14.addItem(spacerItem22)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem23 = QtWidgets.QSpacerItem(
            40,
            0,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_12.addItem(spacerItem23)
        self.label_version = myLabel(self.page_1)
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
        self.label_version.setFont(font)
        self.label_version.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom
            | QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
        )
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_12.addWidget(self.label_version)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 210)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem24 = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_10.addItem(spacerItem24)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_22.setSpacing(30)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lab_link_pg2_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lab_link_pg2_4.setFont(font)
        self.lab_link_pg2_4.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lab_link_pg2_4.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lab_link_pg2_4.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lab_link_pg2_4.setScaledContents(False)
        self.lab_link_pg2_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_link_pg2_4.setOpenExternalLinks(True)
        self.lab_link_pg2_4.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.lab_link_pg2_4.setObjectName("lab_link_pg2_4")
        self.verticalLayout_22.addWidget(self.lab_link_pg2_4)
        self.lab_link_pg2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lab_link_pg2.setFont(font)
        self.lab_link_pg2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lab_link_pg2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lab_link_pg2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lab_link_pg2.setScaledContents(False)
        self.lab_link_pg2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_link_pg2.setOpenExternalLinks(True)
        self.lab_link_pg2.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.lab_link_pg2.setObjectName("lab_link_pg2")
        self.verticalLayout_22.addWidget(self.lab_link_pg2)
        self.lab_link_pg2_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lab_link_pg2_2.setFont(font)
        self.lab_link_pg2_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lab_link_pg2_2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lab_link_pg2_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lab_link_pg2_2.setScaledContents(False)
        self.lab_link_pg2_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_link_pg2_2.setOpenExternalLinks(True)
        self.lab_link_pg2_2.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.lab_link_pg2_2.setObjectName("lab_link_pg2_2")
        self.verticalLayout_22.addWidget(self.lab_link_pg2_2)
        self.lab_link_pg2_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lab_link_pg2_3.setFont(font)
        self.lab_link_pg2_3.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lab_link_pg2_3.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lab_link_pg2_3.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lab_link_pg2_3.setScaledContents(False)
        self.lab_link_pg2_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_link_pg2_3.setOpenExternalLinks(True)
        self.lab_link_pg2_3.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.lab_link_pg2_3.setObjectName("lab_link_pg2_3")
        self.verticalLayout_22.addWidget(self.lab_link_pg2_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_22)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        spacerItem25 = QtWidgets.QSpacerItem(
            0,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_10.addItem(spacerItem25)
        self.verticalLayout_11.addWidget(self.frame_3)
        self.progressBar_waiting = QtWidgets.QProgressBar(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.progressBar_waiting.sizePolicy().hasHeightForWidth()
        )
        self.progressBar_waiting.setSizePolicy(sizePolicy)
        self.progressBar_waiting.setMinimumSize(QtCore.QSize(341, 31))
        self.progressBar_waiting.setMaximumSize(QtCore.QSize(341, 31))
        self.progressBar_waiting.setSizeIncrement(QtCore.QSize(0, 0))
        self.progressBar_waiting.setProperty("value", 1)
        self.progressBar_waiting.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_waiting.setTextVisible(False)
        self.progressBar_waiting.setInvertedAppearance(False)
        self.progressBar_waiting.setObjectName("progressBar_waiting")
        self.verticalLayout_11.addWidget(
            self.progressBar_waiting, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        spacerItem26 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_11.addItem(spacerItem26)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_12.setContentsMargins(30, 0, 30, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem27 = QtWidgets.QSpacerItem(
            20,
            200,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_12.addItem(spacerItem27)
        self.pg3_stackedWidget = QtWidgets.QStackedWidget(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pg3_stackedWidget.sizePolicy().hasHeightForWidth()
        )
        self.pg3_stackedWidget.setSizePolicy(sizePolicy)
        self.pg3_stackedWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.pg3_stackedWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pg3_stackedWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.pg3_stackedWidget.setObjectName("pg3_stackedWidget")
        self.multi = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multi.sizePolicy().hasHeightForWidth())
        self.multi.setSizePolicy(sizePolicy)
        self.multi.setMaximumSize(QtCore.QSize(16777215, 60))
        self.multi.setObjectName("multi")
        self.layoutWidget = QtWidgets.QWidget(self.multi)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 490, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lab_bat_tit = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_bat_tit.sizePolicy().hasHeightForWidth())
        self.lab_bat_tit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.lab_bat_tit.setFont(font)
        self.lab_bat_tit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_bat_tit.setWordWrap(True)
        self.lab_bat_tit.setObjectName("lab_bat_tit")
        self.horizontalLayout_21.addWidget(self.lab_bat_tit)
        self.pg3_stackedWidget.addWidget(self.multi)
        self.solo = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solo.sizePolicy().hasHeightForWidth())
        self.solo.setSizePolicy(sizePolicy)
        self.solo.setMinimumSize(QtCore.QSize(0, 181))
        self.solo.setBaseSize(QtCore.QSize(0, 181))
        self.solo.setObjectName("solo")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.solo)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lab_bat_tit_2 = QtWidgets.QLabel(self.solo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_bat_tit_2.sizePolicy().hasHeightForWidth()
        )
        self.lab_bat_tit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.lab_bat_tit_2.setFont(font)
        self.lab_bat_tit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lab_bat_tit_2.setWordWrap(True)
        self.lab_bat_tit_2.setObjectName("lab_bat_tit_2")
        self.verticalLayout_15.addWidget(self.lab_bat_tit_2)
        self.solo_widget = QtWidgets.QWidget(self.solo)
        self.solo_widget.setEnabled(True)
        self.solo_widget.setObjectName("solo_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.solo_widget)
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.solo_space = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.solo_space.setFont(font)
        self.solo_space.setText("")
        self.solo_space.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solo_space.setObjectName("solo_space")
        self.verticalLayout_16.addWidget(self.solo_space)
        self.solo_label_cards = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_label_cards.setFont(font)
        self.solo_label_cards.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.solo_label_cards.setObjectName("solo_label_cards")
        self.verticalLayout_16.addWidget(self.solo_label_cards)
        self.solo_label_speed = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_label_speed.setFont(font)
        self.solo_label_speed.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.solo_label_speed.setObjectName("solo_label_speed")
        self.verticalLayout_16.addWidget(self.solo_label_speed)
        self.solo_label_percent = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_label_percent.setFont(font)
        self.solo_label_percent.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.solo_label_percent.setObjectName("solo_label_percent")
        self.verticalLayout_16.addWidget(self.solo_label_percent)
        self.horizontalLayout_23.addLayout(self.verticalLayout_16)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.solo_best = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.solo_best.setFont(font)
        self.solo_best.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solo_best.setObjectName("solo_best")
        self.verticalLayout_9.addWidget(self.solo_best)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.solo_val_cards_best = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_val_cards_best.setFont(font)
        self.solo_val_cards_best.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solo_val_cards_best.setObjectName("solo_val_cards_best")
        self.horizontalLayout_26.addWidget(self.solo_val_cards_best)
        self.verticalLayout_9.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.solo_val_speed_best = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_val_speed_best.setFont(font)
        self.solo_val_speed_best.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.solo_val_speed_best.setObjectName("solo_val_speed_best")
        self.horizontalLayout_24.addWidget(self.solo_val_speed_best)
        self.solo_label_speed_unit = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_label_speed_unit.setFont(font)
        self.solo_label_speed_unit.setObjectName("solo_label_speed_unit")
        self.horizontalLayout_24.addWidget(self.solo_label_speed_unit)
        self.verticalLayout_9.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.solo_val_percent_best = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_val_percent_best.setFont(font)
        self.solo_val_percent_best.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solo_val_percent_best.setObjectName("solo_val_percent_best")
        self.horizontalLayout_25.addWidget(self.solo_val_percent_best)
        self.verticalLayout_9.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_23.addLayout(self.verticalLayout_9)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.solo_Today = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.solo_Today.setFont(font)
        self.solo_Today.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solo_Today.setObjectName("solo_Today")
        self.verticalLayout_13.addWidget(self.solo_Today)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.solo_val_cards_best_2 = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_val_cards_best_2.setFont(font)
        self.solo_val_cards_best_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solo_val_cards_best_2.setObjectName("solo_val_cards_best_2")
        self.horizontalLayout_27.addWidget(self.solo_val_cards_best_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.solo_val_speed_best_2 = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_val_speed_best_2.setFont(font)
        self.solo_val_speed_best_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.solo_val_speed_best_2.setObjectName("solo_val_speed_best_2")
        self.horizontalLayout_29.addWidget(self.solo_val_speed_best_2)
        self.solo_label_speed_unit_2 = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_label_speed_unit_2.setFont(font)
        self.solo_label_speed_unit_2.setObjectName("solo_label_speed_unit_2")
        self.horizontalLayout_29.addWidget(self.solo_label_speed_unit_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.solo_val_percent_best_2 = QtWidgets.QLabel(self.solo_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_val_percent_best_2.setFont(font)
        self.solo_val_percent_best_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solo_val_percent_best_2.setObjectName("solo_val_percent_best_2")
        self.horizontalLayout_28.addWidget(self.solo_val_percent_best_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_23.addLayout(self.verticalLayout_13)
        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 2)
        self.horizontalLayout_23.setStretch(2, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_30.setSpacing(20)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem28 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_30.addItem(spacerItem28)
        spacerItem29 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_30.addItem(spacerItem29)
        spacerItem30 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_30.addItem(spacerItem30)
        self.solo_but_reset_all_time = QtWidgets.QPushButton(self.solo_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.solo_but_reset_all_time.sizePolicy().hasHeightForWidth()
        )
        self.solo_but_reset_all_time.setSizePolicy(sizePolicy)
        self.solo_but_reset_all_time.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_but_reset_all_time.setFont(font)
        self.solo_but_reset_all_time.setFlat(False)
        self.solo_but_reset_all_time.setObjectName("solo_but_reset_all_time")
        self.horizontalLayout_30.addWidget(self.solo_but_reset_all_time)
        spacerItem31 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_30.addItem(spacerItem31)
        spacerItem32 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_30.addItem(spacerItem32)
        self.solo_but_reset_today = QtWidgets.QPushButton(self.solo_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.solo_but_reset_today.sizePolicy().hasHeightForWidth()
        )
        self.solo_but_reset_today.setSizePolicy(sizePolicy)
        self.solo_but_reset_today.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.solo_but_reset_today.setFont(font)
        self.solo_but_reset_today.setFlat(False)
        self.solo_but_reset_today.setObjectName("solo_but_reset_today")
        self.horizontalLayout_30.addWidget(self.solo_but_reset_today)
        spacerItem33 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_30.addItem(spacerItem33)
        self.verticalLayout_5.addLayout(self.horizontalLayout_30)
        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_15.addWidget(self.solo_widget)
        self.verticalLayout_17.addLayout(self.verticalLayout_15)
        self.pg3_stackedWidget.addWidget(self.solo)
        self.verticalLayout_12.addWidget(self.pg3_stackedWidget)
        spacerItem34 = QtWidgets.QSpacerItem(
            20,
            200,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_12.addItem(spacerItem34)
        self.progressBar_p1 = QtWidgets.QProgressBar(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.progressBar_p1.sizePolicy().hasHeightForWidth()
        )
        self.progressBar_p1.setSizePolicy(sizePolicy)
        self.progressBar_p1.setMinimumSize(QtCore.QSize(300, 61))
        self.progressBar_p1.setMaximumSize(QtCore.QSize(510, 61))
        self.progressBar_p1.setBaseSize(QtCore.QSize(510, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar_p1.setFont(font)
        self.progressBar_p1.setProperty("value", 24)
        self.progressBar_p1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_p1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar_p1.setTextDirection(
            QtWidgets.QProgressBar.Direction.TopToBottom
        )
        self.progressBar_p1.setObjectName("progressBar_p1")
        self.verticalLayout_12.addWidget(self.progressBar_p1)
        spacerItem35 = QtWidgets.QSpacerItem(
            20,
            200,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_12.addItem(spacerItem35)
        self.progressBar_p2 = QtWidgets.QProgressBar(self.page_3)
        self.progressBar_p2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.progressBar_p2.sizePolicy().hasHeightForWidth()
        )
        self.progressBar_p2.setSizePolicy(sizePolicy)
        self.progressBar_p2.setMinimumSize(QtCore.QSize(300, 61))
        self.progressBar_p2.setMaximumSize(QtCore.QSize(510, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar_p2.setFont(font)
        self.progressBar_p2.setAutoFillBackground(False)
        self.progressBar_p2.setProperty("value", 24)
        self.progressBar_p2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_p2.setTextVisible(True)
        self.progressBar_p2.setInvertedAppearance(False)
        self.progressBar_p2.setTextDirection(
            QtWidgets.QProgressBar.Direction.BottomToTop
        )
        self.progressBar_p2.setObjectName("progressBar_p2")
        self.verticalLayout_12.addWidget(self.progressBar_p2)
        spacerItem36 = QtWidgets.QSpacerItem(
            20,
            200,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_12.addItem(spacerItem36)
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        BatMainWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(BatMainWin)
        self.stackedWidget.setCurrentIndex(2)
        self.pg3_stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(BatMainWin)

    def retranslateUi(self, BatMainWin):
        _translate = QtCore.QCoreApplication.translate
        BatMainWin.setWindowTitle(_translate("BatMainWin", "Anki with Friends"))
        self.label_blank_r.setText(_translate("BatMainWin", "W"))
        self.lab_welcome.setText(
            _translate(
                "BatMainWin",
                'elcome to <a href="https://ankiweb.net/shared/info/613520216">Anki with Friends</a>!',
            )
        )
        self.tableWidget_users_connected.setToolTip(
            _translate(
                "BatMainWin",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; text-decoration: underline;">Connected players are shown here</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" text-decoration: underline;">To initiate a session:</span><br />- Select any player(s) and then click &quot;Send Request&quot;...<br />- A waiting screen is displayed while we ask the player(s) if they\'d like to study a deck with the options you suggested<br />- if they accept, a notification will appear and the study session will begin immediately<br />- if they do not accept, or are away from their computer, a different notification will appear</p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" text-decoration: underline;">To join a session in progress:</span><br />- Select any player in battle and then click &quot;Join Battle&quot;<br />- you will start with the number of cards equal to whoever currently has the most cards left</p></body></html>',
            )
        )
        self.tableWidget_users_connected.setSortingEnabled(True)
        self.but_away.setToolTip(
            _translate(
                "BatMainWin",
                '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline;">Set your status here</span></p><p>- clicking the red &quot;Away Status&quot; button will set your status to &quot;Away&quot; and won\'t allow others to invite you to a session</p><p>- clicking the green &quot;Ready Status&quot; button will set your status to &quot;Ready&quot; and will allow others to invite you to a session</p></body></html>',
            )
        )
        self.but_away.setText(_translate("BatMainWin", "Away\n" "Status"))
        self.but_solo.setToolTip(
            _translate(
                "BatMainWin",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; text-decoration: underline;">Solo Battle (aka NatEmy mode)</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Play against yourself using your best metrics from today as a goal. Simply reset them by clicking the reset button during a solo battle.</p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Metrics to beat are:<br /> - time per card<br /> - percent correct<br /> - total cards per day (based on <a href="https://faqs.ankiweb.net/the-anki-2.1-scheduler.html"><span style=" text-decoration: underline; color:#0000ff;">your scheduler</span></a>\'s cutoff time)</p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:7.5pt; font-weight:600;">NatEmy mode</span><span style=" font-size:7.5pt;"> (pronounced &quot;anatomy&quot;) inspired by Natalie and Emily from the class of 2023</span></p></body></html>',
            )
        )
        self.but_solo.setText(_translate("BatMainWin", "Solo\n" "Battle"))
        self.but_join.setToolTip(
            _translate(
                "BatMainWin",
                '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline;">To join a session in progress:</span></p><p>- Select any player in battle and then click &quot;Join Battle&quot;<br/>- you will start with the number of cards equal to whoever currently has the most cards left</p></body></html>',
            )
        )
        self.but_join.setText(_translate("BatMainWin", "Join\n" "Battle"))
        self.but_sendittt.setToolTip(
            _translate(
                "BatMainWin",
                '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline;">To initiate a session:</span></p><p>- Select any player(s) and then click &quot;Send Request&quot;...<br/>- A waiting screen is displayed while we ask the player(s) if they\'d like to study a deck with the options you suggested<br/>- if they accept, a notification will appear and the study session will begin immediately<br/>- if they do not accept, or are away from their computer, a different notification will appear</p></body></html>',
            )
        )
        self.but_sendittt.setText(_translate("BatMainWin", "Send\n" "Request"))
        self.lab_pg1_opt_tit.setText(_translate("BatMainWin", "Current"))
        self.lab_pg1_opt_tit_2.setText(_translate("BatMainWin", "Options:"))
        self.spinbox_bdecksize_bw.setSuffix(_translate("BatMainWin", " cards"))
        self.lab_max_cards.setText(_translate("BatMainWin", "Max 500 cards"))
        self.lab_pg1_cards.setText(_translate("BatMainWin", "###"))
        self.lab_pg1_cardtype.setText(_translate("BatMainWin", "@@@"))
        self.lab_pg1_tit_cards.setText(_translate("BatMainWin", "cards"))
        self.lab_pg1_due_today.setText(_translate("BatMainWin", "Due today"))
        self.lab_pg1_overdues.setText(_translate("BatMainWin", "including overdues"))
        self.lab_pg1_cardorder.setText(_translate("BatMainWin", "@@@"))
        self.lab_pg1_tit_cardorder.setText(_translate("BatMainWin", "order"))
        self.lab_pg1_resched.setText(_translate("BatMainWin", "Yes"))
        self.lab_pg1_tit_resched.setText(_translate("BatMainWin", "Reschedule"))
        self.lab_pg1_matched.setText(_translate("BatMainWin", "Unmatched"))
        self.lab_pg1_tit_matched.setText(_translate("BatMainWin", "Deck"))
        self.lab_pg1_joiners.setText(_translate("BatMainWin", "Yes"))
        self.lab_pg1_tit_joiners.setText(
            _translate("BatMainWin", "Accept joins in battle")
        )
        self.but_options.setToolTip(
            _translate(
                "BatMainWin",
                '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline;">Click here to change deck options</span></p><p>- This will open a new window that allows you to adjust several options<br/>- When you &quot;Accept&quot; a request, some of these options will not be applied. Instead, the options displayed in the invitation window (that the other person suggested) will be used</p></body></html>',
            )
        )
        self.but_options.setText(_translate("BatMainWin", "Change Options"))
        self.label_version.setText(_translate("BatMainWin", "v2.08"))
        self.lab_link_pg2_4.setText(
            _translate(
                "BatMainWin",
                '<html><head/><body><p><a href="https://www.battleanki.com"><span style=" text-decoration: underline; color:#0000ff;">Anki with Friends Website</span></a></p></body></html>',
            )
        )
        self.lab_link_pg2.setText(
            _translate(
                "BatMainWin",
                '<a href="https://www.usmle.org/step-1/">USMLE Step 1 Website</a>',
            )
        )
        self.lab_link_pg2_2.setText(
            _translate(
                "BatMainWin",
                '<a href="https://www.prometric.com/site-status?__hstc=46213176.fa91e3a14cbb7194a16283fe8a740005.1609850017232.1609850017232.1609850017232.1&__hssc=46213176.1.1609850017233&__hsfp=2324073213">Prometric Site Status Page</a>',
            )
        )
        self.lab_link_pg2_3.setText(
            _translate(
                "BatMainWin", '<a href="https://www.uptodate.com/login">UpToDate</a>'
            )
        )
        self.progressBar_waiting.setFormat(_translate("BatMainWin", "%p%"))
        self.lab_bat_tit.setText(_translate("BatMainWin", "Anki Study Time!"))
        self.lab_bat_tit_2.setText(_translate("BatMainWin", "Solo Study Session!"))
        self.solo_label_cards.setText(_translate("BatMainWin", "Cards:"))
        self.solo_label_speed.setText(_translate("BatMainWin", "Speed:"))
        self.solo_label_percent.setText(_translate("BatMainWin", "% correct:"))
        self.solo_best.setToolTip(
            _translate("BatMainWin", "Stats for all-time fastest Solo Battle")
        )
        self.solo_best.setText(
            _translate("BatMainWin", "All-Time Fastest Solo Session")
        )
        self.solo_val_cards_best.setToolTip(
            _translate("BatMainWin", "Stats for all-time best Solo Battle")
        )
        self.solo_val_cards_best.setText(_translate("BatMainWin", "(cds)"))
        self.solo_val_speed_best.setToolTip(
            _translate("BatMainWin", "Stats for all-time best Solo Battle")
        )
        self.solo_val_speed_best.setText(_translate("BatMainWin", "(spd)"))
        self.solo_label_speed_unit.setToolTip(
            _translate("BatMainWin", "Stats for all-time best Solo Battle")
        )
        self.solo_label_speed_unit.setText(_translate("BatMainWin", "s/card"))
        self.solo_val_percent_best.setToolTip(
            _translate("BatMainWin", "Stats for all-time best Solo Battle")
        )
        self.solo_val_percent_best.setText(_translate("BatMainWin", "(%)"))
        self.solo_Today.setToolTip(
            _translate("BatMainWin", "Stats for best Solo Battle today")
        )
        self.solo_Today.setText(_translate("BatMainWin", "Fastest Solo Session Today"))
        self.solo_val_cards_best_2.setToolTip(
            _translate("BatMainWin", "Stats for best Solo Battle today")
        )
        self.solo_val_cards_best_2.setText(_translate("BatMainWin", "(cds)"))
        self.solo_val_speed_best_2.setText(_translate("BatMainWin", "(spd)"))
        self.solo_label_speed_unit_2.setToolTip(
            _translate("BatMainWin", "Stats for best Solo Battle today")
        )
        self.solo_label_speed_unit_2.setText(_translate("BatMainWin", "s/card"))
        self.solo_val_percent_best_2.setToolTip(
            _translate("BatMainWin", "Stats for best Solo Battle today")
        )
        self.solo_val_percent_best_2.setText(_translate("BatMainWin", "(%)"))
        self.solo_but_reset_all_time.setText(_translate("BatMainWin", "Reset"))
        self.solo_but_reset_today.setText(_translate("BatMainWin", "Reset"))


from .myclass import myLabel


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BatMainWin = QtWidgets.QMainWindow()
    ui = Ui_BatMainWin()
    ui.setupUi(BatMainWin)
    BatMainWin.show()
    sys.exit(app.exec_())
