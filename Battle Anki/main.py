#                     Copyright © 2020-2022 Joseph Policarpio

#     Anki with Friends (previously Battle Anki) is an add-on for Anki,
#     a program for studying flash cards.

#     This file is part of Anki with Friends
#
#     Anki with Friends is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License (AGPL)
#     version 3 of the License, as published by the Free Software Foundation.
#                               AGPL-3.0-only.
#
#     Anki with Friends is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


from .consts import *
from .vars import *
from .dicts import *
from .myclass import *
from .BAmainwin import *
from .OptDia import *
from .ask_BD import *
from .battle_conf import *
from .reb_comms import *
from .ty import *
from .isd import *
from PyQt6 import QtWidgets
from pathlib import Path

import socket
import threading
import select
import time
import shutil
import re
import logging.handlers

# import sys
# import subprocess
# import datetime
# import os
# import json
# from sys import _getframe
# from datetime import datetime as dt
# from .activity import *
# from anki.consts import *


from datetime import timedelta as delT
from anki.stats import CollectionStats
from aqt import gui_hooks, mw
from aqt.qt import *
from aqt.utils import *


# #####################################################################################################
# todo: cardtype not always recalled after battle - maybe fixed?
# ######################################################################################################################


def function_logger(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        try:
            logger_utils.debug(f"{name} started")
        except TypeError as e:
            # エラーをキャッチし、エラーメッセージをログに出力する
            # ログにエラーメッセージを追加
            logger.error("TypeError occured.", error=str(e))
        before = time.time()
        result = func(*args, **kwargs) or None
        logger_utils.info("%s finished" % name)
        return result if result else None

    return wrapper


def function_timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs) or None
        try:
            logger_utils.debug(
                f"{func.__name__} took:" f"{time.time() - before} seconds"
            )
        except TypeError as e:
            # エラーをキャッチし、エラーメッセージをログに出力する
            # ログにエラーメッセージを追加
            logger.error("TypeError occured.", error=str(e))
        return result if result else None

    return wrapper


def debugger_logger(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        try:
            logger_utils.debug(f"{name} started")
        except TypeError as e:
            # エラーをキャッチし、エラーメッセージをログに出力する
            # ログにエラーメッセージを追加
            logger.error("TypeError occured.", error=str(e))
        before = time.time()
        result = func(*args, **kwargs) or None
        logger_utils.debug(
            "%s finished\n" "%s took: %g seconds" % (name, name, time.time() - before)
        )
        return result if result else None

    return wrapper


def save_solo_to_config(solo_dict: dict):
    global config
    config = mw.addonManager.getConfig(__name__)
    config["solo"] = dict(solo_dict)
    mw.addonManager.writeConfig(__name__, config)
    return


# todo: make 'invisible' version and 'interactive' version
class MainWindow:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_win = QtWidgets.QMainWindow()
        self.main_win.hide()
        self.ui = Ui_BatMainWin()
        self.ui.setupUi(self.main_win)
        self.main_win.closeEvent = self.closeEvent

        # center main_win
        qtRectangle = self.main_win.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.main_win.move(qtRectangle.topLeft())

        self.main_win.setMinimumSize(self.main_win.size())

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.page_2.hide()
        self.ui.page_3.hide()

        self.ui.label_version.setText(f"v{BA_VER}")
        self.ui.label_version.clicked.connect(lambda: openfolder(LOG_FOLD))

        self.ui.label_blank_d.setText(" ")

        # self.ui.label_blank_d.clicked.connect(lambda: sav_sd())
        self.ui.label_blank_r.clicked.connect(lambda: do_Ro())

        sb = self.ui.spinbox_bdecksize_bw
        sb.valueChanged.connect(lambda: spinbox_val_change(sb.value(), "bw"))

        self.update_home_labels()

        self.ui.but_away.clicked.connect(self.set_away)
        # self.ui.but_badge.clicked.connect(self.toggle_badges)
        self.ui.but_solo.clicked.connect(self.solo_battle)
        self.ui.but_join.clicked.connect(self.join_battle)
        self.ui.but_sendittt.clicked.connect(lambda: sendittt())

        self.ui.but_options.clicked.connect(lambda: opts_open())

        self.ui.solo_but_reset_all_time.clicked.connect(
            lambda: self.reset_solo("alltime")
        )
        self.ui.solo_but_reset_today.clicked.connect(lambda: self.reset_solo("today"))

        self.timer = QTimer()  # heartbeat timer
        self.timer.timeout.connect(lambda: running())
        self.timer.timeout.connect(self.hb)

        self.ui.tableWidget_users_connected.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.ui.tableWidget_users_connected.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.ui.tableWidget_users_connected.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.MultiSelection
        )
        self.ui.tableWidget_users_connected.horizontalHeader().setVisible(True)
        self.ui.tableWidget_users_connected.setStyleSheet(
            "QHeaderView::section{font-size: 9pt;"
            "Background-color:rgb(186, 186, 186);"
            "border-color: rgb(168, 168, 168);"
            "border-top-style: none;"
            "border-top-width: 0px;"
            "border-bottom-style: solid;"
            "border-bottom-width: 2px;"
            "border-left-style: solid;"
            "border-left-width: 1px;"
            "border-right-style: solid;"
            "border-right-width: 1px;}"
        )
        self.set_badgeview()

        self.ui.progressBar_waiting.setStyleSheet(
            "QProgressBar::chunk{background: QLinearGradient(x1: 0, y1: 0, x2: 1,"
            " y2: 0, stop: 0 rgb(147, 34, 245), stop: 0.5 rgb(211, 90, 219),"
            " stop: 1 rgb(245, 220, 34));}"
            "QProgressBar{border:1px solid black;border-radius:4px;color:black;}"
        )

        self.timer_battle = QTimer()
        self.timer_battle.timeout.connect(self.updateBattleBars)

        self.timer_bar = QTimer()  # waiting after send request
        self.timer_bar.timeout.connect(self.updateWaitingBar)
        self.step = 0

        self.timer_load = QTimer()  # loading on startup timer
        self.timer_load.timeout.connect(self.updateLoadBar)
        self.step_load = 0

        self.timer_undo_accepted = (
            QTimer()
        )  # undoing accepted request, now in battle timer
        self.timer_undo_accepted.timeout.connect(self.undoaccept)

        self.timer_undo_request = QTimer()  # undoing a request, maybe in battle timer
        self.timer_undo_request.timeout.connect(self.undorequest)

        self.timer_undo_rejected = QTimer()  # undoing saying no to a battle timer
        self.timer_undo_rejected.timeout.connect(lambda: undo_rejected())

        self.timer_denied = QTimer()  # my request was denied timer
        self.timer_denied.timeout.connect(lambda: req_was_denied())

        self.timer_joined = QTimer()
        self.timer_joined.timeout.connect(self.undojoin)

        self.timer_hb = QTimer()  # another heartbeat timer
        self.timer_hb.timeout.connect(self.hb_dias)

        self.best_timer = QTimer()
        self.best_timer.timeout.connect(self.best_count)
        self.best_bar_count = 0

        self.cards_left = 0

        self.move_resource("battle_anki_icon.png")
        self.move_resource("ba_bronze.png")
        self.move_resource("ba_silver.png")
        self.move_resource("ba_gold.png")
        self.move_resource("ba_black.png")
        self.move_resource("ba_platinum.png")
        self.move_resource("star.png", repl=True)

        self.BA_log = QPixmap("battle_anki_icon.png")

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("battle_anki_icon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )

        w = 25
        h = 25
        self.sc_7 = self.scale_img("ba_platinum.png", w, h)
        self.sc_6 = self.scale_img("ba_black.png", w, h)
        self.sc_5 = self.scale_img("ba_gold.png", w, h)
        self.sc_4 = self.scale_img("ba_silver.png", w, h)
        self.sc_3 = self.scale_img("ba_bronze.png", w, h)
        self.sc_2 = self.scale_img("battle_anki_icon.png", w, h)
        self.sc_1 = self.scale_img("star.png", 18, 18)

        self.main_win.setWindowIcon(icon)

        # self.ui.lab_logo_home.setPixmap(self.fireworks_logo2)
        # self.ui.lab_logo_home_2.setPixmap(self.fireworks_logo2)

        self.bar_left_radius = (
            "border-top-left-radius: 24px;" "border-bottom-left-radius: 24px;"
        )
        self.bar_radius = "border-radius: 24px;"

        self.odd_bar_bot_color = COLOR_ODD_BAR_BOTTOM_HALF
        self.odd_bar_top_color = COLOR_ODD_BAR_TOP_HALF
        self.odd_backgr_top_color = COLOR_ODD_BAR_BACKGROUND_TOP_HALF
        self.odd_backgr_bot_color = COLOR_ODD_BAR_BACKGROUND_BOTTOM_HALF

        self.even_bar_bot_color = COLOR_EVEN_BAR_BOTTOM_HALF
        self.even_bar_top_color = COLOR_EVEN_BAR_TOP_HALF
        self.even_backgr_top_color = COLOR_EVEN_BAR_BACKGROUND_TOP_HALF
        self.even_backgr_bot_color = COLOR_EVEN_BAR_BACKGROUND_BOTTOM_HALF

        self.odd_bar_text_color = self.even_bar_bot_color
        self.even_bar_text_color = self.odd_bar_bot_color

        self.odd_bar_head = (
            f"QProgressBar::chunk"
            f"{{"
            f"border: 1px solid {self.odd_bar_bot_color};"
            f"border-style: outset;"
        )
        #                    # RADIUS HERE
        self.odd_bar_tail = (
            f"background: QLinearGradient( x1: 0.2, y1: 0.2,"
            f" x2: 0.4, y2: 1,"
            f" stop: 0 {self.odd_bar_top_color},"
            f" stop: 1 {self.odd_bar_bot_color});"
            f"}}"
            f"QProgressBar"
            f"{{"
            f"border: 2px solid {self.odd_bar_bot_color};"
            f"border-style: inset;"
            f"border-radius: 24px;"
            f"background: QLinearGradient( x1: 0, y1: 0,"
            f" x2: 0.9, y2: 1,"
            f" stop: 0 {self.odd_backgr_top_color},"
            f" stop: 1 {self.odd_backgr_bot_color});"
            f"color: {self.odd_bar_text_color};"
            f"}}"
        )

        self.even_bar_head = (
            f"QProgressBar::chunk"
            f"{{"
            f"border: 1px solid {self.even_bar_bot_color};"
            f"border-style: outset;"
        )
        #                     # RADIUS HERE
        self.even_bar_tail = (
            f"background: QLinearGradient( x1: 0.2, y1: 0.2,"
            f" x2: 0.4, y2: 1,"
            f" stop: 0 {self.even_bar_top_color},"
            f" stop: 1 {self.even_bar_bot_color});"
            f"}}"
            f"QProgressBar"
            f"{{"
            f"border: 2px solid {self.even_bar_bot_color};"
            f"border-style: inset;"
            f"border-radius: 24px;"
            f"background: QLinearGradient( x1: 0, y1: 0,"
            f" x2: 0.9, y2: 1,"
            f" stop: 0 {self.even_backgr_top_color},"
            f" stop: 1 {self.even_backgr_bot_color});"
            f"color: {self.even_bar_text_color};"
            f"}}"
        )

        self.ss_odd_bar_left_radius = (
            self.odd_bar_head + self.bar_left_radius + self.odd_bar_tail
        )
        self.ss_odd_bar_round = self.odd_bar_head + self.bar_radius + self.odd_bar_tail

        self.ss_even_bar_left_radius = (
            self.even_bar_head + self.bar_left_radius + self.even_bar_tail
        )
        self.ss_even_bar_round = (
            self.even_bar_head + self.bar_radius + self.even_bar_tail
        )

        self.ui.progressBar_p1.valueChanged.connect(
            lambda: self.ss_update_any_bar(self.ui.progressBar_p1)
        )
        self.ui.progressBar_p2.valueChanged.connect(
            lambda: self.ss_update_any_bar(self.ui.progressBar_p2)
        )

        # self.reset_progBar_styles()
        self.ss_set_2_bars()

        s = self.ui

        s.away_hovered = "#ff877a"
        s.away_hov_bd = colorscale(s.away_hovered, 0.7)
        s.away_hv_chck = "#7cf283"
        s.away_hv_chck_bd = colorscale(s.away_hv_chck, 0.7)
        s.away_chckd = colorscale(s.away_hovered, 0.9)
        s.away_chckd_bd = colorscale(s.away_chckd, 0.7)

        s.away_hv_prs = colorscale(s.away_chckd, 0.9)
        s.away_hv_prs_bd = colorscale(s.away_hv_prs, 0.7)

        s.bdg_hovered = "#ffdab9"
        s.bdg_hov_bd = colorscale(s.bdg_hovered, 0.8)
        s.bdg_hv_chck = "#ffa866"
        s.bdg_hv_chck_bd = colorscale(s.bdg_hv_chck, 0.8)
        s.bdg_hvprs = "#e87720"
        s.bdg_hvprs_bd = colorscale(s.bdg_hvprs, 0.8)
        s.bdg_chckd = "#f08b3e"
        s.bdg_chckd_bd = colorscale(s.bdg_chckd, 0.8)

        s.join_hovered = "#7edbfc"
        s.join_hov_bd = colorscale(s.join_hovered, 0.8)
        s.join_prs = "#4fbfe8"
        s.join_prs_bd = colorscale(s.join_prs, 0.7)

        s.send_hov = "#78e387"
        s.send_hov_bd = colorscale(s.send_hov, 0.8)
        s.send_prs = "#48c759"
        s.send_prs_bd = colorscale(s.send_prs, 0.8)

        s.opt_hovered = "#c0a8ed"
        s.opt_hov_bd = colorscale(s.opt_hovered, 0.7)
        s.opt_prs = "#e07ee0"
        s.opt_prs_bd = colorscale(s.opt_prs, 0.5)

        s.b = "1"  # pushbutton border width:

        b_a = self.ui.but_away
        b_a.setStyleSheet(
            f"QPushButton#but_away:hover:!pressed{{background-color: {s.away_hovered};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.away_hov_bd};}}"
            f"QPushButton#but_away:hover:checked{{background-color: {s.away_hv_chck};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.away_hv_chck_bd};}}"
            f"QPushButton#but_away:hover:pressed{{background-color: {s.away_hv_prs};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.away_hv_prs_bd};}}"
            f"QPushButton#but_away:checked{{background-color: {s.away_chckd};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.away_chckd_bd};}}"
        )
        b_b = self.ui.but_solo  # but_badge
        b_b.setStyleSheet(
            f"QPushButton#but_solo:hover:!pressed{{background-color: {s.bdg_hovered};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.bdg_hov_bd};}}"
            f"QPushButton#but_solo:hover:checked{{background-color: {s.bdg_hv_chck};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.bdg_hv_chck_bd};}}"
            f"QPushButton#but_solo:hover:pressed{{background-color: {s.bdg_hvprs};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.bdg_hvprs_bd};}}"
            f"QPushButton#but_solo:checked{{background-color: {s.bdg_chckd};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.bdg_chckd_bd};}}"
        )
        b_j = self.ui.but_join
        b_j.setStyleSheet(
            f"QPushButton#but_join:hover:!pressed{{background-color: {s.join_hovered};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.join_hov_bd};}}"
            f"QPushButton#but_join:pressed{{background-color: {s.join_prs};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.join_prs_bd};}}"
        )
        b_s = self.ui.but_sendittt
        b_s.setStyleSheet(
            f"QPushButton#but_sendittt:hover:!pressed{{background-color: {s.send_hov};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.send_hov_bd};}}"
            f"QPushButton#but_sendittt:pressed{{background-color: {s.send_prs};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.send_prs_bd};}}"
        )
        b_o = self.ui.but_options
        b_o.setStyleSheet(
            f"QPushButton#but_options:hover:!pressed{{background-color: {s.opt_hovered};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.opt_hov_bd};}}"
            f"QPushButton#but_options:pressed{{background-color: {s.opt_prs};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.opt_prs_bd};}}"
        )

        logger_ui.info("Mainwindow instance initiated")
        self.update_home_labels()

        return

    def set_pg3(self, mode: str = "solo" or "multi"):
        if mode == "solo":
            # self.ui.pg3_stackedWidget.setMaximumHeight(181)
            self.ui.pg3_stackedWidget.setCurrentWidget(self.ui.solo)
        elif mode == "multi":
            # self.ui.pg3_stackedWidget.setMaximumHeight(50)

            self.ui.pg3_stackedWidget.setCurrentWidget(self.ui.multi)
        return

    def uncheck_away(self):
        ba_var["inbattle"] = 1
        self.ui.but_away.setText("Away\nStatus")
        self.ui.but_away.setChecked(False)
        save_ba_var()
        get_local_data()
        send_pulse()
        return

    def solo_battle(self):
        global ba_var

        self.uncheck_away()

        ba_var["solo"] = True
        reset_if_new_day()
        self.best_bar_count = 0
        dummys()
        recall_boxes()
        build_terms_of_battle()
        self.set_pg3("solo")
        make_battle_deck(ba_var["terms_of_battle"])

        return

    def update_home_labels(self):
        self.ui.lab_pg1_overdues.hide()
        self.ui.lab_pg1_matched.hide()
        self.ui.lab_pg1_tit_matched.hide()
        self.ui.lab_pg1_tit_cardorder.hide()
        self.ui.lab_pg1_cards.hide()  # setText(str(ba_var['decksize']))
        self.ui.lab_pg1_tit_cards.hide()
        self.ui.lab_max_cards.hide()
        self.ui.lab_pg1_opt_tit.hide()
        self.ui.lab_pg1_opt_tit_2.hide()
        self.ui.lab_pg1_joiners.hide()
        self.ui.lab_pg1_tit_joiners.hide()

        self.ui.spinbox_bdecksize_bw.setValue(ba_var["decksize"])

        self.ui.lab_pg1_cardtype.setText(ba_var["card_type_str"])
        self.ui.lab_pg1_cardorder.setText(ba_var["card_order_str"])

        if ba_var["today_only"]:
            self.ui.lab_pg1_due_today.show()
            # self.ui.lab_pg1_overdues.show()
        else:
            self.ui.lab_pg1_due_today.hide()
            # self.ui.lab_pg1_overdues.hide()

        if ba_var["resched_box"]:
            self.ui.lab_pg1_resched.hide()  # setText('')
            self.ui.lab_pg1_tit_resched.setText("Reschedule")
        else:
            self.ui.lab_pg1_resched.setText("Do NOT")
            self.ui.lab_pg1_resched.show()  # setText('')
            self.ui.lab_pg1_tit_resched.setText("reschedule")

        if ba_var["joiners_box"]:
            self.ui.lab_pg1_joiners.hide()  # setText('')
            self.ui.lab_pg1_tit_joiners.hide()  # setText('Accept joins in battle')
        else:
            self.ui.lab_pg1_joiners.setText("Do NOT")
            self.ui.lab_pg1_joiners.show()  # setText('')
            self.ui.lab_pg1_tit_joiners.setText("accept joins in battle")
            self.ui.lab_pg1_tit_joiners.show()
        # logger_ui.info('update_home_labels completed')
        return

    def scale_img(self, name: str, w: int, h: int):
        img = QPixmap(name)
        scaled = img.scaled(
            w,
            h,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        logger_ui.debug("scale_img completed")
        return scaled

    def make_table_item(self, img: QPixmap):
        lbl = QLabel()
        lbl.setPixmap(img)
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        itm = lbl
        logger_ui.debug("make_table_item completed")
        return itm

    def undojoin(self):
        self.timer_joined.stop()
        global ba_var
        ba_var["accepted_req"] = False
        logger_ui.info("undojoin completed")

    def move_resource(self, res_name: str, repl=False):
        end_dest = os.path.join(os.getcwd(), res_name)
        if repl:
            # back_len_join = len(os.path.join(mw.pm.name, "collection.media"))
            # com_root = os.Path.cwd()()[:-back_len_join]
            source_fold = os.path.join(mw.pm.addonFolder(), BA_FOLDER_NAME, "res")
            source = os.path.join(source_fold, res_name)
            dest = f"{os.getcwd()}"
            shutil.move(source, end_dest)
            shutil.copy(end_dest, source_fold)
            logger_ui.debug("move_resource completed")
        else:
            if os.path.isfile(f"{end_dest}") is False:
                # back_len_join = len(os.path.join(mw.pm.name, "collection.media"))
                # com_root = os.Path.cwd()()[:-back_len_join]
                source_fold = os.path.join(mw.pm.addonFolder(), BA_FOLDER_NAME, "res")
                source = os.path.join(source_fold, res_name)
                dest = f"{os.getcwd()}"
                shutil.move(source, dest)
                shutil.copy(end_dest, source_fold)
                logger_ui.debug("move_resource completed")

    def set_away(self):
        logger_user.debug("set_away clicked")
        global ba_var
        if self.ui.but_away.isChecked():
            ba_var["inbattle"] = 0
            self.ui.but_away.setText("Ready\nStatus")
        else:
            ba_var["inbattle"] = 1
            self.ui.but_away.setText("Away\nStatus")
        save_ba_var()
        get_local_data()
        send_pulse()
        logger_ui.info(f"set_away() clicked & completed [Status: {inbattle_status()}]")

    def ss_set_2_bars(self):
        self.ui.progressBar_p1.setValue(7)
        self.ui.progressBar_p2.setValue(7)
        self.ui.progressBar_p1.setStyleSheet(self.ss_odd_bar_left_radius)
        self.ui.progressBar_p2.setStyleSheet(self.ss_even_bar_left_radius)
        logger_ui.debug("ss_set_2_bars() completed")

    def undorequest(self):
        global local_data
        global ba_var
        ba_var["matched_list"] = []
        ba_var["matched_size"] = 0
        ba_var["matched_terms"] = ""
        local_data["matched terms"] = ""
        local_data["card ids"] = [{}]
        local_data["request options"]["req Remote IP"] = ""
        local_data["request options"]["req name"] = ""
        self.timer_undo_request.stop()
        logger_ui.info("undorequest completed")

    def undoaccept(self):
        global ba_var

        ba_var["accepted_req"] = False
        ba_var["matched_terms"] = ""
        local_data["matched terms"] = ""

        for rd in [
            d
            for d in sd
            if d["user info"]["Remote IP"] in ba_var["challenger_ip"]
            if d["user info"]["in battle?"] != 2
        ]:
            i = ba_var["challenger_ip"].index(rd["user info"]["Remote IP"])
            try:
                ba_var["challenger_ip"].pop(i)
                ba_var["challenger_name"].pop(i)
                ba_var["challenger_progress"].pop(i)
                ba_var["acc_list"].pop(i)
                ba_var["conn"].pop(i)
            except IndexError:
                pass
        self.timer_undo_accepted.stop()
        logger_ui.info("undoaccept completed")

    def reset(self):
        global ba_var
        global local_data

        delete_battle_decks()

        # event_trigger(5)

        self.undorequest()

        if ba_var["acc_list"] and max(ba_var["acc_list"]) > 2:
            self.remove_progressbars()

        ba_var["myprogress"] = 0

        ba_var["solo"] = False

        ba_var["challenger_name"] = []
        ba_var["challenger_ip"] = []
        ba_var["challenger_progress"] = []
        ba_var["acc_list"] = []
        ba_var["conn"] = []

        local_data["request options"] = {
            "req name": "",
            "req names": [],
            "req Remote IP": str(),
            "req Remote IPs": [],
        }
        ba_var["accepted_req"] = False
        ba_var["told_problem"] = False
        ba_var["window_open"] = False
        ba_var["opponent_problem"] = False
        ba_var["make_deck_problem"] = False
        ba_var["ready_for_request"] = True
        ba_var["popped_comms"] = False
        ba_var["popped_req"] = False
        ba_var["inbattle"] = 1

        # x = read(X_CONFIG_NAME)
        # x[2] = ba_var
        # write(x, X_CONFIG_NAME)
        x = save_ba_var()

        recall_boxes(x)

        self.ss_set_2_bars()
        self.main_win.show()
        self.set_pg3("multi")

        logger_ui.info("reset completed")

    def update_best_bar(self, b_date: str = None, pct_corr: float = 100.00):

        def name():
            self.ui.progressBar_p2.setFormat(f"{mw.pm.name} on {b_date}    {int(p)}%")
            return

        c = self.best_bar_count
        if pct_corr != 0:
            adjusted_deck = int(ba_var["decksize"] / (pct_corr / 100))
        else:
            adjusted_deck = int(ba_var["decksize"])

        p = int((c / adjusted_deck) * 100)

        if p < 7:
            self.ui.progressBar_p2.setValue(7)
            name()
        elif 7 <= p < 100:
            self.ui.progressBar_p2.setValue(p)
            name()
        elif p == 100:
            self.best_timer.stop()
            self.ui.progressBar_p2.setValue(p)
            name()
            # self.best_bar_count = 0

        # showInfo(f"decksize: {ba_var['decksize']}\n\n"
        #          f"percent correct: {pct_corr/100}")
        self.ui.progressBar_p2.update()

        return

    # todo: when click away, save?

    def set_best_labels(self, indict: dict = None):
        b = indict if indict else read(SOLO_CONFIG)[0]
        self.ui.solo_val_speed_best.setText("{:.2f}".format(b["best"]["speed"]))
        self.ui.solo_val_cards_best.setText(str(b["best"]["cards"]))
        self.ui.solo_val_percent_best.setText("{:.1f}".format(b["best"]["corr"]))

        self.ui.solo_val_percent_best_2.setText("{:.1f}".format(b["today"]["corr"]))
        self.ui.solo_val_speed_best_2.setText("{:.2f}".format(b["today"]["speed"]))
        self.ui.solo_val_cards_best_2.setText(str(b["today"]["cards"]))

        # self.ui.progressBar_p2.setFormat(f"Answer a card 'good' to start the timer!")
        if ba_var["myprogress"] > 0:
            self.ui.progressBar_p2.setFormat(
                f"{mw.pm.name} on {b['today']['finish']}    0%"
            )
        # self.update_best_bar(b)

        return

    def best_count(self, indict: dict = None):

        if indict:
            b = indict
        elif type(read(SOLO_CONFIG)) == list:
            b = read(SOLO_CONFIG)[0]
        else:
            b = read(SOLO_CONFIG)

        if self.best_bar_count == 0 and indict is not None:
            today_speed = (
                float(b["today"]["speed"]) if float(b["today"]["speed"]) else 30.000
            )
            best_speed = (
                float(b["best"]["speed"]) if float(b["best"]["speed"]) else 30.000
            )
            sp = today_speed  # min(today_speed)      #, best_speed)
            self.best_timer.start(int(sp * 1000))
            self.set_best_labels(b)
            self.ui.progressBar_p2.setFormat(
                f"Answer a card 'good' to start the timer!"
            )
        else:
            self.best_bar_count += 1
            # todo: delete this line (test):
            # self.ui.solo_val_cards_best.setText(str(self.best_bar_count))
            try:
                self.update_best_bar(b["today"]["finish"], float(b["today"]["corr"]))
            except TypeError:
                pass

        return

    def reset_solo(self, which: str = "alltime" or "today"):
        d = read(SOLO_CONFIG)[0]
        which = "best" if which == "alltime" else "today"
        for key in d[which].keys():
            if type(d[which][key]) == str:
                d[which][key] = "01/01/00 00:00:00"
            elif type(d[which][key]) == int:
                d[which][key] = 0
            elif type(d[which][key]) == float:
                d[which][key] = 30.000

        write(d, SOLO_CONFIG)

        save_solo_to_config(d)

        self.set_best_labels(d)

        return

    def solo_fin(self):
        # todo: compare with best times and save into solo.json dict

        # def this_to_last(indict: dict):
        #     indict['last']['start'] = str(indict['this']['start'])
        #     indict['this']['start'] = "01/01/0000 00:00:00"
        #     indict['last']['finish'] = str(indict['this']['finish'])
        #     indict['this']['finish'] = "01/01/0000 00:00:00"
        #     return indict

        r = read(SOLO_CONFIG)
        s = dict(r[0])
        now = dt.now()
        s["this"]["finish"] = dt2s(now)

        # showInfo(f"{s['this']}")
        this_start = str(s["this"]["start"])
        this_finish = str(s["this"]["finish"])

        s["last"]["start"] = this_start
        s["last"]["finish"] = this_finish

        t1 = s2dt(s["last"]["start"]).timestamp()
        t2 = s2dt(s["last"]["finish"]).timestamp()

        # showInfo(f"before:\n"
        #          f"last start, last finish: {s2['last']['start'], s2['last']['finish']}\n\n"
        #          f".timestamp: {(s2dt(s2['last']['start']).timestamp()), (s2dt(s2['last']['finish']).timestamp())}")

        # showInfo(f"after:\n"
        #          f"t1, t2: {t1, t2}")

        correct, ncards, tsec = get_pct_corr(t1, t2)

        s["last"]["corr"] = correct
        s["last"]["cards"] = ncards
        s["last"]["time"] = tsec

        # showInfo(f"after:\n"
        #          f"pct, cards, time: {correct, ncards, tsec}")

        s["last"]["speed"] = (
            (s["last"]["time"] / s["last"]["cards"]) if s["last"]["cards"] else 0.000
        )

        s["today"] = (
            s["last"].copy()
            if (s["last"]["speed"] < s["today"]["speed"])
            else s["today"]
        )

        s["best"] = (
            s["last"].copy() if (s["last"]["speed"] < s["best"]["speed"]) else s["best"]
        )

        write(s, SOLO_CONFIG)
        save_solo_to_config(s)

        self.set_best_labels(s)

        return

    # todo: send solo_battle data via event_trigger?
    def solo_bars(self):

        def today_start(d: dict):
            if not d["today"]["start"]:
                d["today"]["start"] = dt2s(dt.now())
            else:
                today_st = s2dt(d["today"]["start"])
                if (
                    dt.now() - today_st
                ).total_seconds() > 0 and dt.now().day != today_st.day:
                    d["today"]["start"] = dt2s(dt.now())
            return d

        self.my_progbar()

        if self.best_bar_count == 0 and ba_var["myprogress"] == 0:
            red = read(SOLO_CONFIG)
            s = dict(red[0])
            s["this"]["start"] = dt2s(dt.now())
            s2 = today_start(s)
            # s2['today']['cards'] = ba_var['cards_today']

            # s2['today']['time'] = t_today
            write(s2, SOLO_CONFIG)
            save_solo_to_config(s2)
            self.best_count(s2)
        elif ba_var["myprogress"] == 100:

            self.best_timer.stop()
            self.timer_battle.stop()
            self.my_progbar()
            self.solo_fin()

        self.check_fin()
        return

    def my_progbar(self):
        global ba_var
        prog = ba_var["myprogress"]
        prog = int(
            (1.00 - (ba_var["cards_left"] / ba_var["decksize"])) * 100
        )  # - (100/ba_var['decksize']))
        prog = prog if prog >= 0 else 0
        ba_var["myprogress"] = prog

        self.ui.progressBar_p1.setFormat(f"{mw.pm.name}   {ba_var['myprogress']}%")
        return

    def updateBattleBars(self):
        global ba_var
        global local_data
        # global sd
        # global dyn_id

        if ba_var["solo"]:
            self.solo_bars()
            if self.best_bar_count == 0 and ba_var["myprogress"] > 0:
                b = read(SOLO_CONFIG)[0]
                self.ui.progressBar_p2.setFormat(
                    f"{mw.pm.name} on {b['best']['finish']}    0%"
                )
            return
        elif ba_var["joiners_box"]:
            check_for_joins()

        if ba_var["inbattle"] == 2:
            self.my_progbar()
            if sd and ba_var["challenger_ip"]:

                for rd in [
                    d
                    for d in sd
                    if d["user info"]["Remote IP"] in ba_var["challenger_ip"]
                ]:

                    if (
                        ba_var["joiners_box"]
                        and "req Remote IPs" in rd["request options"].keys()
                    ):
                        for nc in [
                            c
                            for c in sd
                            if rd["user info"]["progress"] != 0
                            if c["user info"]["Remote IP"]
                            not in ba_var["challenger_ip"]
                            if c["user info"]["Remote IP"]
                            in rd["request options"]["req Remote IPs"]
                            if c["user info"]["Remote IP"] != ba_var["loc_rem_ip"]
                            if c["user info"]["in battle?"] == 2
                        ]:
                            ba_var["challenger_ip"].append(nc["user info"]["Remote IP"])
                            ba_var["challenger_name"].append(nc["user info"]["name"])
                            ba_var["challenger_progress"].append(0)
                            ba_var["acc_list"].append(0)
                            ba_var["conn"].append(0)

                    idx = ba_var["challenger_ip"].index(rd["user info"]["Remote IP"])
                    pr = int(rd["user info"]["progress"])
                    ib = bool(rd["user info"]["in battle?"] == 2)

                    if ba_var["conn"][idx] == 0:
                        # they are connected
                        ba_var["conn"][idx] = 1

                    if (
                        ba_var["acc_list"][idx] == 0
                        and rd["user info"]["in battle?"] == 2
                        and idx != 0
                    ):
                        # they they need a progress bar
                        ba_var["acc_list"][idx] = p = max(ba_var["acc_list"]) + 1
                        if ba_var["conn"][idx] == 2:
                            # they just ' joined the game!'
                            ba_var["challenger_name"][idx] = name_str(
                                str(ba_var["challenger_name"][idx]), 1
                            )
                            ba_var["conn"][idx] = 1
                        self.add_progressbar(p, idx)
                        ba_var["challenger_progress"][idx] = 0

                    if ba_var["acc_list"][idx] != 0:
                        # they have a progressbar...

                        if ba_var["challenger_progress"][idx] == 100:
                            if ib and pr == 0:
                                # they started a new match, need to forget their IP
                                ba_var["challenger_ip"][idx] = ""
                                ba_var["challenger_name"][idx] = name_str(
                                    str(ba_var["challenger_name"][idx]), 2
                                )  # LEFT
                            elif (
                                ib
                                and pr != 0
                                and rd["user info"]["accepted req"]
                                and "req Remote IPs" in rd["request options"].keys()
                                and ba_var["loc_rem_ip"]
                                in rd["request options"]["req Remote IPs"]
                            ):
                                # they finished, and then ' rejoined the game!'
                                ba_var["challenger_progress"][idx] = pr
                                ba_var["challenger_name"][idx] = name_str(
                                    str(ba_var["challenger_name"][idx]), 0
                                )  # rejoin

                        elif (
                            ba_var["challenger_progress"][idx] >= 98
                            and ib is not True
                            and pr == 0
                        ):
                            # they just finished and ' LEFT the game...'
                            ba_var["challenger_progress"][idx] = 100
                            ba_var["challenger_name"][idx] = name_str(
                                str(ba_var["challenger_name"][idx]), 2
                            )  # LEFT

                        if ib:
                            if pr != 0 and ba_var["challenger_progress"][idx] != 100:
                                # in battle, playing
                                ba_var["challenger_progress"][idx] = pr
                                if ba_var["challenger_name"][idx][-len(LEFT) :] == LEFT:
                                    # they ' rejoined the game!' after previously leaving
                                    ba_var["challenger_name"][idx] = name_str(
                                        str(ba_var["challenger_name"][idx]), 0
                                    )  # rejoin
                                elif (
                                    ba_var["challenger_name"][idx][-len(REJOINED) :]
                                    == REJOINED
                                ):
                                    pass
                                else:
                                    # set name to only name
                                    ba_var["challenger_name"][idx] = name_str(
                                        str(ba_var["challenger_name"][idx]), 4
                                    )  # name only
                            elif pr == 0 and ba_var["challenger_progress"][idx] != 100:
                                ba_var["challenger_name"][idx] = name_str(
                                    str(ba_var["challenger_name"][idx]), 3
                                )  # starting
                        else:
                            # they are not in battle
                            if ba_var["challenger_progress"][idx] > 0:
                                # they ' LEFT the game...'
                                ba_var["challenger_name"][idx] = name_str(
                                    str(ba_var["challenger_name"][idx]), 2
                                )  # LEFT
                            elif ba_var["challenger_progress"][idx] == 0:
                                if rd["user info"]["accepted req"]:
                                    # they are just starting
                                    ba_var["challenger_name"][idx] = name_str(
                                        str(ba_var["challenger_name"][idx]), 3
                                    )  # starting
                                else:
                                    ba_var["challenger_name"][idx] = name_str(
                                        str(ba_var["challenger_name"][idx]), 2
                                    )  # LEFT

                        if (
                            ba_var["challenger_progress"][idx]
                            and ba_var["acc_list"][idx]
                        ):
                            player = int(ba_var["acc_list"][idx])

                            for p in ba_var[
                                "challenger_progress"
                            ]:  # set any negative progs to zero
                                p = p if p >= 0 else 0

                            if ba_var["challenger_progress"][idx] < 7:
                                exec(
                                    f"""self.ui.progressBar_p{player}.setValue(7)
self.ui.progressBar_p{player}.setFormat(f"{ba_var['challenger_name'][idx]}    {ba_var['challenger_progress'][idx]}%")
self.ui.progressBar_p{player}.update()\n"""
                                )
                            elif ba_var["challenger_progress"][idx] >= 7:
                                exec(
                                    f"""self.ui.progressBar_p{player}.setValue({ba_var['challenger_progress'][idx]})
self.ui.progressBar_p{player}.setFormat(f"{ba_var['challenger_name'][idx]}    {ba_var['challenger_progress'][idx]}%")
self.ui.progressBar_p{player}.update()"""
                                )
                    if 2 not in [
                        x["user info"]["in battle?"]
                        for x in sd
                        if x["user info"]["Remote IP"] in ba_var["challenger_ip"]
                    ]:
                        # only tell me someone has makedeckproblem if no one else is in battle!!!
                        if (
                            "deck problem" in rd["user info"].keys()
                            and rd["user info"]["deck problem"] is True
                            and (ba_var["told_problem"] is False)
                            and (ba_var["popped_comms"] is False)
                        ):
                            ba_var["told_problem"] = True
                            show_and_log(
                                f"We were unable to make a Battle Deck for one of\n"
                                f"your opponents. You can still complete the deck\n"
                                f"if you would like...\n\n"
                                f"If you'd rather end this battle and try again,\n"
                                f"just close the battle window and reopen it!\n"
                                f"Sorry about that!"
                            )

                if 0 in ba_var["conn"]:
                    ded = ba_var["conn"].index(0)
                    ba_var["challenger_name"][ded] = name_str(
                        str(ba_var["challenger_name"][ded]), 2
                    )  # LEFT
                    if ba_var["acc_list"][ded] != 0:
                        try:
                            exec(
                                f"""self.ui.progressBar_p{ba_var['acc_list'][ded]}.setFormat(f"{ba_var['challenger_name'][ded]}    {ba_var['challenger_progress'][ded]}%")\n'
self.ui.progressBar_p{ba_var['acc_list'][ded]}.update()"""
                            )
                        except:
                            pass

            ba_var["conn"] = [0] * len(ba_var["conn"])

            self.check_fin()

        logger_ui.debug("updateBattleBars completed")
        return

    def check_fin(self):
        if ba_var["myprogress"] >= 100:
            self.log_fin()
            get_local_data()
            send_pulse()
            self.ui.progressBar_p1.setValue(ba_var["myprogress"])
            self.ui.progressBar_p1.update()
            self.timer_battle.stop()
            if max(ba_var["challenger_progress"]) >= 100:
                show_and_log("Keep up the good work!\nBetter luck next time!")
            if max(ba_var["challenger_progress"]) < 100:
                show_and_log("Nice work! You are almost an AnKing!")
            self.reset()
            self.showHome()
        elif ba_var["myprogress"] < 7:
            self.ui.progressBar_p1.setValue(7)
            self.ui.progressBar_p1.update()
        elif 7 <= ba_var["myprogress"] < 100:
            self.ui.progressBar_p1.setValue(ba_var["myprogress"])
            self.ui.progressBar_p1.update()
        return

    def log_fin(self):
        s1 = (f"[Total Connected to Server: {len(sd)} ]", "")
        s2 = (f"[{mw.pm.name} FINISHED battle]", "%")
        so = fmt_n_log([s1, s2])
        log_bat_info(so)

    def updateLoadBar(self):
        global ba_var
        if self.step_load < 20:
            self.step_load += 1
            self.main_win.setWindowTitle(
                f"Anki with Friends is Loading...{round(self.step_load * (100 / 20))}%"
            )
        else:
            self.ui.lab_bat_tit.setDisabled(False)
            self.ui.label_blank_r.setDisabled(False)
            self.ui.frame.setDisabled(False)
            self.ui.centralwidget.setDisabled(False)
            self.main_win.setDisabled(False)
            self.timer_load.stop()
            ba_var["isloading"] = False
            self.main_win.setWindowTitle(f"Anki with Friends")
        logger_ui.debug("updateLoadBar completed")

    def updateWaitingBar(self):
        if self.step <= 180:
            self.step += 1
        else:
            self.step = 0
        self.ui.progressBar_waiting.setValue(self.step * (100 / 180))
        self.ui.progressBar_waiting.update()
        logger_ui.debug("updateWaitingBar completed")

    def show(self):
        self.main_win.show()
        logger_ui.info("show completed")

    def showBattle(self):
        logger_ui.info(f"showBattle called...")
        global ba_var

        ba_var["myprogress"] = 0

        ch = len(ba_var["challenger_ip"])
        ba_var["challenger_progress"] = [0] * ch
        ba_var["conn"] = [0] * ch
        ba_var["acc_list"] = [0] * ch
        ba_var["acc_list"][0] = 2

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

        self.ui.progressBar_p1.setFormat(f"{mw.pm.name}   {ba_var['myprogress']}%")
        self.ui.progressBar_p2.setFormat(
            f"{ba_var['challenger_name'][0]}   {ba_var['challenger_progress'][0]}%"
        )

        if ba_var["solo"]:
            ba_var["inbattle"] = 3  # "Solo"
            self.set_pg3("solo")
        else:
            ba_var["inbattle"] = 2  # "In Battle"
            self.set_pg3("multi")

        self.ui.page_3.show()
        self.ui.page_2.hide()
        self.ui.page_1.hide()
        self.ui.page_3.setFocus()

        self.timer_bar.stop()
        self.ui.progressBar_waiting.reset()

        self.ui.progressBar_p1.setValue(7)
        self.ui.progressBar_p2.setValue(7)

        ba_var["cards_left"] = sum(list(mw.col.sched.counts())) + 1
        self.timer_battle.start(300)

        if not self.main_win.isVisible():
            self.main_win.show()

        s1 = (f"[Total Connected to Server: {len(sd)} ]", "", False)
        s2 = (f"[{mw.pm.name} is STARTED BATTLE]", "%")
        so = fmt_n_log([s1, s2])
        logger_ui.info(so)

        # event_trigger(4)

        self.ui.page_3.setFocus()

        return

    def closeEvent(self, event):

        # try:
        self.timer_battle.stop()
        self.best_timer.stop()

        if not ba_var["shutdown"]:
            self.reset()

            # mw.tybox = QDialog()
            # mw.tybox = TY()
            # mw.tybox.show()
        # except Exception as msg:
        #     show_and_log(f'Sorry, there was an error\n'
        #                  f'closing the window\n'
        #                  f'Error Code 1775\n'
        #                  f'{msg}')
        #     logger_ui.exception('Error Code 1775')
        # finally:
        logger_ui.info("Mainwindow closeEvent completed")
        return

    def close_all(self):
        global ba_var
        try:
            self.timer.stop()
            # bye_to_server()
            self.main_win.close()
            ba_var["socket_open"] = False
            ba_var["startup"] = True
        except:
            pass
        finally:
            x = read(X_CONFIG_NAME)
            x[2] = ba_var
            write(x, X_CONFIG_NAME)

            logger_ui.info("close_all completed")
            return

    # from local window
    def get_request_data(self, join=False):
        logger_ui.info("get_request_data started")
        global ba_var
        global local_data
        ba_var["challenger_ip"] = []
        ba_var["challenger_name"] = []
        ba_var["challenger_progress"] = []
        ba_var["can_sendittt"] = False
        if ba_var["inbattle"] == 0:
            show_and_log(
                "Your status is currently set to 'Away' !\n"
                "you have to be 'Ready' to initiate a battle..."
            )
            return False

        if ba_var["decksize"] == 0 and join is False:
            show_and_log("You need to choose the number of cards!")
            return False

        else:
            if (
                ba_var["new_box"]
                or ba_var["learn_box"]
                or ba_var["mature_box"]
                or ba_var["new_AND_review_box"]
            ):
                if (
                    len(
                        self.ui.tableWidget_users_connected.selectionModel().selectedRows()
                    )
                    > 0
                ):
                    if (
                        join
                        and len(
                            self.ui.tableWidget_users_connected.selectionModel().selectedRows(
                                0
                            )
                        )
                        > 1
                    ):
                        show_and_log(f"You can only join one person\n" f"at a time...")
                        return False
                    else:
                        try:
                            self.ui.tableWidget_users_connected.setSortingEnabled(False)
                            for (
                                item
                            ) in self.ui.tableWidget_users_connected.selectionModel().selectedRows(
                                1
                            ):
                                ba_var["challenger_name"].append(item.data(0))
                            ba_var["inbattle_str"] = []
                            if ba_var["badgeview"] is True:
                                for (
                                    item
                                ) in self.ui.tableWidget_users_connected.selectionModel().selectedRows(
                                    2
                                ):
                                    ba_var["inbattle_str"].append(item.data(0))
                            # elif ba_var['badgeview'] is False:
                            #     for item in self.ui.tableWidget_users_connected.selectionModel().selectedRows(1):
                            #         ba_var['inbattle_str'].append(item.data(0))
                            if "Away" not in ba_var["inbattle_str"]:
                                c1 = bool("In Battle" not in ba_var["inbattle_str"])
                                c2 = bool(
                                    c1 is False and join is True
                                )  # pass: inbattle, joining
                                c3 = bool(
                                    c1 is True and join is False
                                )  # pass: not in battle, inviting
                                c4 = bool(
                                    c1 is False and join is False
                                )  # fail: in battle, not joining
                                c5 = bool(
                                    c1 is True and join is True
                                )  # fail: not in battle, trying to join
                                c6 = bool("Solo" in ba_var["inbattle_str"])

                                if c6:
                                    show_and_log(
                                        "One of the players\n"
                                        "you selected is running Solo!\n"
                                        "If you want to play with them,\n"
                                        "you'll have to wait until they're done!"
                                    )
                                    ba_var["challenger_name"] = []
                                    return False
                                elif c5:
                                    show_and_log(
                                        "To join a battle, the player\n"
                                        "you selected has to be in battle!"
                                    )
                                    ba_var["challenger_name"] = []
                                    return False
                                elif c4:
                                    show_and_log(
                                        f"Sorry... {ba_var['challenger_name']} is \n"
                                        f"currently in battle!"
                                    )
                                    ba_var["challenger_name"] = []
                                    return False
                                elif c2 or c3:
                                    sel_ips = []
                                    # check to make sure not self...
                                    if ba_var["badgeview"] is True:
                                        for (
                                            item
                                        ) in self.ui.tableWidget_users_connected.selectionModel().selectedRows(
                                            3
                                        ):
                                            sel_ips.append(str_to_ip(item.data(0)))
                                    # elif ba_var['badgeview'] is False:
                                    #     for item in self.ui.tableWidget_users_connected.selectionModel().selectedRows(
                                    #             2):
                                    #         sel_ips.append(str_to_ip(item.data(0)))
                                    if (
                                        str(mw.pm.name) not in ba_var["challenger_name"]
                                    ) and (ba_var["loc_rem_ip"] not in sel_ips):
                                        incompatible = None
                                        if join:
                                            for p in [
                                                d
                                                for d in sd
                                                if d["user info"]["Remote IP"]
                                                in sel_ips
                                            ]:
                                                if "ver" in p.keys() and p["ver"]:
                                                    cv = str(p["ver"]).split(".")
                                                    if int(cv[0]) < 2:
                                                        incompatible = True
                                        else:
                                            pass
                                        if join and incompatible:
                                            show_and_log(
                                                f"Sorry, {ba_var['challenger_name'][0]}'s\n"
                                                f"Anki with Friends version (v{cv[0]}.{cv[1]})\n"
                                                f"does not support the 'Join Battle' function...\n\n"
                                                f"        Please tell them to update!!!\n\n"
                                                f"Your version:\n\n"
                                                f"             v{BA_VER}\n\n"
                                            )
                                            incompatible = None
                                            return False
                                        else:
                                            local_data["request options"][
                                                "req names"
                                            ] = ba_var["challenger_name"]
                                            local_data["request options"][
                                                "req Remote IPs"
                                            ] = ba_var["challenger_ip"] = sel_ips
                                            local_data["request options"][
                                                "req in battle?"
                                            ] = False
                                            logger_ui.info(
                                                "get_request_data() JOIN data pulled from tablewidget"
                                            )
                                            if c3:
                                                logger_ui.info(
                                                    "get_request_data() INVITE data pulled from tablewidget"
                                                )
                                                local_data["request options"][
                                                    "req name"
                                                ] = ba_var["challenger_name"][0]
                                                local_data["request options"][
                                                    "req Remote IP"
                                                ] = ba_var["challenger_ip"][0]
                                            ba_var["challenger_progress"] = [0] * len(
                                                sel_ips
                                            )
                                            if len(sel_ips) > 1:
                                                local_data["request options"][
                                                    "matched box"
                                                ] = ba_var["matched_box"] = False
                                            ba_var["can_sendittt"] = True
                                            ba_var["inbattle"] = 0
                                            logger_ui.info(
                                                "get_request_data() passed True"
                                            )
                                            return True
                                    else:
                                        ba_var["can_sendittt"] = False
                                        ba_var["challenger_name"] = []
                                        show_and_log(
                                            f"As fun as it sounds, you can't\n"
                                            f"battle yourself on Anki with Friends...\n"
                                            f"If you got this message incorrectly,\n"
                                            f"Please report it\n"
                                            f"EC 732"
                                        )
                                        return False
                            else:
                                ba_var["can_sendittt"] = False
                                ba_var["challenger_name"] = []
                                show_and_log(
                                    f"Sorry... someone you selected\n "
                                    f"is currently away!"
                                )
                                return False
                        except Exception as msge:
                            show_and_log(
                                f"{msge}"
                                f"Sorry, there was a problem...\n"
                                f"you'll have to restart Anki to be able to play.\n"
                                f"EC 607"
                            )
                            return False
                        finally:
                            self.ui.tableWidget_users_connected.setSortingEnabled(True)
                else:
                    ba_var["can_sendittt"] = False
                    show_and_log("You need to choose someone to battle!")
                    return False

            else:
                ba_var["can_sendittt"] = False
                show_and_log("You need to choose the type of cards!")
                return False

    def showWait(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.page_2.show()
        self.ui.page_1.hide()
        self.ui.page_2.setFocus()
        logger_ui.info("showWait() completed")

    def startWaitingBar(self):
        self.step = 0
        self.timer_bar.start(50)
        logger_ui.debug("startWaitingBar completed")

    def refresh_users(self):
        self.ui.tableWidget_users_connected.setSortingEnabled(False)

        # if ba_var['badgeview'] is False:
        #     self.refresh_regview()
        # if ba_var['badgeview'] is True:
        self.refresh_badgeview()

        self.ui.tableWidget_users_connected.setSortingEnabled(True)
        logger_ui.debug("refresh_users completed")
        return

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.spinbox_bdecksize_bw.setValue(ba_var["decksize"])
        self.main_win.show()
        self.ui.page_1.show()
        self.ui.page_1.setFocus()
        logger_ui.info("showHome completed")

    def start_load_bw(self):
        global ba_var
        ba_var["isloading"] = True
        # self.ui.progressBar_loading.setFormat(f'Loading... %p%')
        self.main_win.setWindowTitle("Anki with Friends is Loading...0%")
        self.step_load = 0

        # self.ui.lab_batform_connected.hide()
        # self.ui.lab_users_connected.hide()
        # self.ui.tableWidget_users_connected.hide()
        self.ui.lab_bat_tit.setDisabled(True)
        self.ui.label_blank_r.setDisabled(True)
        self.ui.frame.setDisabled(True)
        self.ui.centralwidget.setDisabled(True)
        self.timer_load.start(50)
        logger_ui.debug("start_load_bw completed")

    def hb(self):
        if ba_var["isloading"] is False:
            self.main_win.setWindowTitle("Ankı with Friends")
            self.timer_hb.start(700)
        logger_ui.debug("hb completed")

    def hb_dias(self):
        if ba_var["isloading"] is False:
            self.main_win.setWindowTitle("Anki with Friends")
        logger_ui.debug("hb_dias completed")

    def ss_update_any_bar(self, bar: QtWidgets.QProgressBar):
        dig = int(bar.objectName()[-1:])
        if (dig % 2) != 0:
            # odd
            if bar.value() >= 95:
                bar.setStyleSheet(self.ss_odd_bar_round)
            else:
                bar.setStyleSheet(self.ss_odd_bar_left_radius)
        else:
            # even
            if bar.value() >= 95:
                bar.setStyleSheet(self.ss_even_bar_round)
            else:
                bar.setStyleSheet(self.ss_even_bar_left_radius)
        logger_ui.debug("ss_update_any_bar completed")

    def ss_p1(self):
        if self.ui.progressBar_p1.value() >= 95:
            self.ui.progressBar_p1.setStyleSheet(
                f"QProgressBar::chunk"
                f"{{"
                f"border: 1px solid {self.odd_bar_bot_color};"
                f"border-style: outset;"
                f"border-radius: 24px;"
                f"background: QLinearGradient( x1: 0.2, y1: 0.2,"
                f" x2: 0.4, y2: 1,"
                f" stop: 0 {self.odd_bar_top_color},"
                f" stop: 1 {self.odd_bar_bot_color});"
                f"}}"
                f"QProgressBar"
                f"{{"
                f"border: 2px solid {self.odd_bar_bot_color};"
                f"border-style: inset;"
                f"border-radius: 24px;"
                f"background: QLinearGradient( x1: 0, y1: 0,"
                f" x2: 0.9, y2: 1,"
                f" stop: 0 {self.odd_backgr_top_color},"
                f" stop: 1 {self.odd_backgr_bot_color});"
                f"color: {self.even_bar_bot_color};"
                f"}}"
            )
        logger_ui.debug("ss_p1() completed")

    def ss_p2(self):
        if self.ui.progressBar_p2.value() >= 95:
            self.ui.progressBar_p2.setStyleSheet(
                f"QProgressBar::chunk"
                f"{{"
                f"border: 1px solid {self.even_bar_bot_color};"
                f"border-style: outset;"
                f"border-radius: 24px;"
                f"background: QLinearGradient( x1: 0.2, y1: 0.2,"
                f" x2: 0.4, y2: 1,"
                f" stop: 0 {self.even_bar_top_color},"
                f" stop: 1 {self.even_bar_bot_color});"
                f"}}"
                f"QProgressBar"
                f"{{"
                f"border: 2px solid {self.even_bar_bot_color};"
                f"border-style: inset;"
                f"border-radius: 24px;"
                f"background: QLinearGradient( x1: 0, y1: 0,"
                f" x2: 0.9, y2: 1,"
                f" stop: 0 {self.even_backgr_top_color},"
                f" stop: 1 {self.even_backgr_bot_color});"
                f"color: {self.odd_bar_bot_color};"
                f"}}"
            )
        logger_ui.debug("ss_p2() completed")

    def set_badgeview(self):
        logger_user.debug("set_badgeview() clicked")
        self.main_win.setFixedSize(550, 410)
        # self.ui.but_badge.setText('Hide\nBadges')
        self.main_win.resize(550, 410)
        self.ui.tableWidget_users_connected.setColumnCount(4)
        self.ui.tableWidget_users_connected.setIconSize(QSize(26, 26))
        self.ui.tableWidget_users_connected.setHorizontalHeaderItem(
            0, QTableWidgetItem("Badge")
        )
        self.ui.tableWidget_users_connected.setColumnWidth(0, 45)
        self.ui.tableWidget_users_connected.setHorizontalHeaderItem(
            1, QTableWidgetItem("Name")
        )
        # self.ui.tableWidget_users_connected.setHorizontalHeaderItem(2, QTableWidgetItem("t Today"))
        # self.ui.tableWidget_users_connected.setColumnWidth(2, 60)
        self.ui.tableWidget_users_connected.setHorizontalHeaderItem(
            2, QTableWidgetItem("Status")
        )
        self.ui.tableWidget_users_connected.setColumnWidth(2, 98)
        self.ui.tableWidget_users_connected.setHorizontalHeaderItem(
            3, QTableWidgetItem("IP")
        )
        self.ui.tableWidget_users_connected.setColumnWidth(3, 1)
        logger_ui.info("set_badgeview clicked & completed")

    def mod_tableWidget_users(self, player_tuple, row):
        if deID in ADMIN_LIST:
            if player_tuple[4] not in EN_PAR_EN:
                self.ui.tableWidget_users_connected.selectRow(row)
                for item in self.ui.tableWidget_users_connected.selectedItems():
                    item.setForeground(QColor(255, 0, 0))
                self.ui.tableWidget_users_connected.clearSelection()

        return

    def refresh_badgeview(self):
        logger_ui.debug("refresh_badgeview STARTED")
        try:
            sel_ip = []
            if self.ui.tableWidget_users_connected.selectedItems():
                for (
                    item
                ) in self.ui.tableWidget_users_connected.selectionModel().selectedRows(
                    3
                ):
                    sel_ip.append(item.data(0))

            sd_modified = mod_show_list(sd)

            if sd_modified is None:
                sd_modified = [local_data]

            show = list(
                {
                    (
                        d["user info"]["cards today"],
                        d["user info"]["name"],
                        d["user info"]["in battle?"],
                        d["user info"]["Remote IP"],
                        d["user info"]["deID"],
                    )
                    for d in sd
                    if ("ver", "user info" in d.keys())
                    and (int(str(d["ver"]).split(".")[1][:2]) > 32)
                    and (
                        "cards today",
                        "in battle?",
                        "Remote IP",
                        "deID" in d["user info"].keys(),
                    )
                }
            )

            player_count = len(show)
            if player_count > 7:
                self.ui.tableWidget_users_connected.setColumnWidth(1, 175)
            else:
                self.ui.tableWidget_users_connected.setColumnWidth(1, 193)

            # update the contents
            self.ui.tableWidget_users_connected.clearContents()
            self.ui.tableWidget_users_connected.setRowCount(player_count)

            for i in range(0, len(show)):
                self.ui.tableWidget_users_connected.setItem(
                    i, 1, QTableWidgetItem(str(show[i][1]))
                )
                self.ui.tableWidget_users_connected.setItem(
                    i, 3, QTableWidgetItem(str(show[i][3]))
                )

                if show[i][2] == 2:
                    self.ui.tableWidget_users_connected.setItem(
                        i, 2, QTableWidgetItem("In Battle")
                    )
                elif show[i][2] == 1:
                    self.ui.tableWidget_users_connected.setItem(
                        i, 2, QTableWidgetItem("Ready")
                    )
                elif show[i][2] == 3:
                    self.ui.tableWidget_users_connected.setItem(
                        i, 2, QTableWidgetItem("Solo")
                    )
                elif show[i][2] == 0:
                    self.ui.tableWidget_users_connected.setItem(
                        i, 2, QTableWidgetItem("Away")
                    )
                # todo: change to numbers here for more options (solo battle)
                # elif show[i]['user info']['in battle?'] is None:
                #     self.ui.tableWidget_users_connected.setItem(i, 2, QTableWidgetItem('Away'))
                else:
                    show_and_log(
                        f"Sorry, there was a problem with Anki with Friends...\n\n"
                        f"                 EC 994"
                    )

                if show[i][0] >= 5000:
                    itm_7 = self.make_table_item(self.sc_7)
                    self.ui.tableWidget_users_connected.setCellWidget(i, 0, itm_7)
                elif show[i][0] >= 2500:
                    itm_6 = self.make_table_item(self.sc_6)
                    self.ui.tableWidget_users_connected.setCellWidget(i, 0, itm_6)
                elif show[i][0] >= 1000:
                    itm_5 = self.make_table_item(self.sc_5)
                    self.ui.tableWidget_users_connected.setCellWidget(i, 0, itm_5)
                elif show[i][0] >= 750:
                    itm_4 = self.make_table_item(self.sc_4)
                    self.ui.tableWidget_users_connected.setCellWidget(i, 0, itm_4)
                elif show[i][0] >= 500:
                    itm_3 = self.make_table_item(self.sc_3)
                    self.ui.tableWidget_users_connected.setCellWidget(i, 0, itm_3)
                elif show[i][0] >= 250:
                    itm_2 = self.make_table_item(self.sc_2)
                    self.ui.tableWidget_users_connected.setCellWidget(i, 0, itm_2)
                elif show[i][0] > 0:
                    itm_1 = self.make_table_item(self.sc_1)
                    self.ui.tableWidget_users_connected.setCellWidget(i, 0, itm_1)
                else:
                    self.ui.tableWidget_users_connected.setItem(
                        i, 0, QTableWidgetItem(" ")
                    )

                # self.mod_tableWidget_users(show[i], i)    # sends row, changes color of text

            if sel_ip:
                for i in range(self.ui.tableWidget_users_connected.rowCount()):
                    if self.ui.tableWidget_users_connected.item(i, 3).data(0) in sel_ip:
                        self.ui.tableWidget_users_connected.selectRow(i)

            self.ui.tableWidget_users_connected.update()

            logger_ui.debug("refresh_badgeview completed")
            return

        except Exception as mesg:
            show_and_log(
                f"Sorry, there was a problem with Anki with Friends...\n"
                f"EC 1536\n"
                f"{mesg}"
            )
            mw.battle_window.timer.stop()
            self.main_win.close()
            return

    def add_progressbar(self, p: int, ind: int):
        logger_ui.debug("add_progressbar() STARTED")
        s = p + 20
        name = f"progressBar_p{p}"
        name_sp = f"spacerItem{s}"
        setattr(self.ui, name, QtWidgets.QProgressBar(self.ui.page_3))
        bar = f"self.ui.{name}"
        exec(
            f"""
{bar}.setEnabled(True)
sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth({bar}.sizePolicy().hasHeightForWidth())
{bar}.setSizePolicy(sizePolicy)
{bar}.setMinimumSize(QtCore.QSize(300, 61))
{bar}.setMaximumSize(QtCore.QSize(510, 61))
font = QtGui.QFont()
font.setPointSize(14)
{bar}.setFont(font)
{bar}.setAutoFillBackground(False)
{bar}.setProperty("value", 24)
{bar}.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
{bar}.setTextVisible(True)
{bar}.setInvertedAppearance(False)
{bar}.setTextDirection(QtWidgets.QProgressBar.Direction.BottomToTop)
{bar}.setObjectName("{name}")
self.ui.verticalLayout_12.addWidget({bar})
{name_sp} = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
self.ui.verticalLayout_12.addItem({name_sp})
{bar}.valueChanged.connect(lambda: mw.battle_window.ss_update_any_bar(mw.battle_window.ui.progressBar_p{p}))
{bar}.setValue(7)
{bar}.setFormat(f'{ba_var['challenger_name'][ind]}   {ba_var['challenger_progress'][ind]}%')
{bar}.update()
"""
        )
        self.ui.page_3.update()
        logger_ui.info("add_progressbar() completed")

    def remove_progressbars(self):
        logger_ui.debug("remove_progressbars() STARTED")
        try:
            for nu in [
                x
                for x in ba_var["acc_list"]
                if x > 2
                if self.ui.verticalLayout_12.count() > 7
            ]:
                child = self.ui.verticalLayout_12.takeAt(7)
                if child.widget():
                    child.widget().deleteLater()
                    child2 = self.ui.verticalLayout_12.takeAt(7)
                    if child2.spacerItem():
                        self.ui.verticalLayout_12.removeItem(child2.spacerItem())
                elif child.spacerItem():
                    self.ui.verticalLayout_12.removeItem(child.spacerItem())
                    child2 = self.ui.verticalLayout_12.takeAt(7)
                    if child2.widget():
                        child2.widget().deleteLater()
                logger_ui.info("remove_progressbars() 1 ITEM REMOVED")
            else:
                logger_ui.info("remove_progressbars() completed")
                return
        except Exception as excp:
            show_and_log(
                f"Sorry, something went wrong...\n" f"Error Code 1352\n" f"{excp}"
            )

    def join_battle(self):
        logger_user.info("join_battle clicked")
        global ba_var
        global dyn_id
        global local_data

        store_before_send()

        local_data["request options"]["req name"] = ""
        local_data["request options"]["req Remote IP"] = ""

        max_cl = 0
        m_ds = 0
        ib = [False]
        real_decksize = int()
        ba_var["ready_for_request"] = False

        if self.get_request_data(True):
            c = str(ba_var["challenger_ip"][0])
            d = next((x for x in sd if x["user info"]["Remote IP"] == c), None)
            if sd and d:
                if "req Remote IPs" in d["request options"].keys():
                    ips = list(d["request options"]["req Remote IPs"])
                    for item in [
                        ip
                        for ip in ips
                        if ip is not None
                        if ip not in ba_var["challenger_ip"]
                        if ip != ba_var["loc_rem_ip"]
                    ]:
                        ba_var["challenger_ip"].append(item)

                np = len(ba_var["challenger_ip"])
                ba_var["challenger_name"] = [""] * np
                ba_var["challenger_progress"] = [0] * np
                ba_var["acc_list"] = [0] * np
                ba_var["acc_list"][0] = 2
                mc = [0] * np
                ds = [0] * np
                ib = [False] * np

                for v in ba_var["challenger_ip"]:
                    i = ba_var["challenger_ip"].index(v)
                    for q in [z for z in sd if z["user info"]["Remote IP"] == v]:
                        ba_var["challenger_name"][i] = q["user info"]["name"]
                        if "pfrac" in q["user info"].keys():
                            mc[i] = q["user info"]["pfrac"][0]
                            ds[i] = q["user info"]["pfrac"][1]
                        if (
                            q["user info"]["in battle?"] == 2
                            and q["user info"]["progress"] != 0
                        ):
                            ib[i] = True
                            ba_var["challenger_progress"][i] = q["user info"][
                                "progress"
                            ]
                max_cl = max([0 if r is None else r for r in mc])
                m_ds = max([0 if s is None else s for s in ds])
            build_terms_of_battle()
            if max_cl > 0:
                buildn = max_cl
            else:
                deck = mw.col.decks.byName(f"{use_deck}")
                buildn = min(mw.col.sched.counts()[2], 100)
            if m_ds > 0:
                ba_var["decksize"] = m_ds
            # else:
            #     ba_var['decksize'] = self.ui.spinbox_bdecksize.value()  # shouldnt need this - join battle disabled for v < 1.35

            ba_var["accepted_req"] = True
            self.timer_joined.start(10 * 1000)

            dyn_id = make_battle_deck(ba_var["terms_of_battle"], buildn)
            logger_ui.info("join_battle() completed")
            return
        else:
            logger_ui.info("join_battle() FAILED")
            ba_var["ready_for_request"] = True
            return


class ConfDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the form on the new battle window
        self.ui = Ui_bat_conf_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)

        # center it
        qtRectangle = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.ui.buttonBox_conf_dialog.accepted.connect(lambda: confOK())
        logger_ui.info("ConfDialog() instance initiated")


class AskDialog(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the form on the ask window
        self.ui = Ui_AskDialog()
        self.ui.setupUi(self)

        # center it
        qtRectangle = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.move_resource = MainWindow.move_resource
        self.move_resource(self, "scroll.png", repl=True)

        self.scale = MainWindow.scale_img
        # scroll = self.scale(self, 'scroll.png',
        #                     self.ui.back_label.width(),
        #                     self.ui.back_label.height())
        self.ui.back_label.setPixmap(QPixmap("scroll.png"))

        # self.setStyleSheet(f"background-color:transparent;"
        #                    f"background-image:url(scroll.png);")

        logo = self.scale(
            self,
            "battle_anki_icon.png",
            self.ui.lab_logo.width(),
            self.ui.lab_logo.height(),
        )
        self.ui.lab_logo.setPixmap(logo)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        s = self
        s.b = "1"  # pushbutton border width
        s.norm = "#726649"
        s.norm_bd = colorscale(s.norm, 0.8)
        s.hov = "#BEAA79"
        s.hov_bd = colorscale(s.hov, 0.8)
        s.prs = "#332F24"
        s.prs_bd = colorscale(s.prs, 0.8)

        s.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # f"QDialog{{background-color:transparent}}"
        # f"QDialog#AskDialog{{background-image:url('scroll.png')}}"

        pal = QPalette()
        pal.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
        s.setPalette(pal)

        s.setStyleSheet(
            f"QDialog QLabel{{color: black;}}"
            f"QPushButton{{background-color: {s.norm};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.norm_bd};}}"
            f"QPushButton:hover:!pressed{{background-color: {s.hov};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.hov_bd};}}"
            f"QPushButton:pressed{{background-color: {s.prs};"
            f"border-style: solid; border-width: {s.b}px; border-color: {s.prs_bd};}}"
        )

        self.timer_ask = QTimer()
        self.timer_ask.timeout.connect(lambda: auto_timeout_reject())

        # custom callbacks
        self.accepted.connect(lambda: accepted())
        self.rejected.connect(lambda: rejected())
        logger_ui.info("AskDialog() instance initiated")
        return

    def fill_options(self, indict=dict):
        global ba_var
        ba_var["decksize"] = indict["deck size"]
        ba_var["matched_box"] = indict["matched box"]
        ba_var["new_box"] = indict["new box"]
        ba_var["learn_box"] = indict["learn box"]
        ba_var["mature_box"] = indict["mature box"]
        ba_var["resched_box"] = indict["resched box"]
        ba_var["today_only"] = indict["due box"]
        ba_var["requester"] = indict["requester"]
        # req_in_bat = indict['req in battle?']

        self.ui.lab_ask_bd_name.setText(str(ba_var["requester"]))

        self.ui.val_decksize.setText(str(ba_var["decksize"]))

        # todo: test this ... newANDlearn box not coming in?
        cardtype = ""
        if ba_var["new_box"] and ba_var["learn_box"]:
            cardtype = "new and review"
        elif ba_var["new_box"] and not ba_var["learn_box"]:
            cardtype = "new"
        elif ba_var["learn_box"] and not ba_var["new_box"]:
            cardtype = "review"
        if cardtype:
            self.ui.val_cardtype.setText(cardtype)

        if ba_var["today_only"]:
            self.ui.val_today_only.setText("all")
        else:
            self.ui.val_today_only.setText("not")

        if ba_var["resched_box"]:
            self.ui.val_resched.setText("")
        else:
            self.ui.val_resched.setText("not")

        logger_ui.debug("fill_options() completed")
        return


class RebComms(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the form on the rebcoms window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)

        # center it
        qtRectangle = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        global ba_var
        if ba_var["opponent_problem"] is True:
            self.ui.lab_reb_comms_title.setText(
                f"We were unable to make a full battle deck for\n"
                f"your opponent. You can still complete this deck\n"
                f"if you would like...\n\n"
                f"If you'd rather end this battle, just close\n"
                f"the Anki with Friends window and reopen it!\n"
                f"Sorry about that!"
            )
            ow = self.ui.lab_reb_comms_title.width()
            oh = self.ui.lab_reb_comms_title.height()
            self.ui.lab_reb_comms_title.adjustSize()
            w = self.ui.lab_reb_comms_title.width()
            h = self.ui.lab_reb_comms_title.height()
            dw = w - ow
            dh = h - oh
            self.resize((self.width() + dw), (self.height() + dh))
            bb_ox = self.ui.buttonBox_reb_comms.x()
            bb_oy = self.ui.buttonBox_reb_comms.y()
            bb_nx = bb_ox + (dw / 2)
            bb_ny = bb_oy + dh
            bb_w = self.ui.buttonBox_reb_comms.width()
            bb_h = self.ui.buttonBox_reb_comms.height()
            self.ui.buttonBox_reb_comms.setGeometry(bb_nx, bb_ny, bb_w, bb_h)

        if ba_var["make_deck_problem"] is True:
            if ba_var["made_count"] is None:
                self.ui.lab_reb_comms_title.setText(
                    f"No cards matched the criteria you provided.\n"
                    f"Please try again..."
                )
            elif type(ba_var["made_count"]) == list:
                self.ui.lab_reb_comms_title.setText(
                    f"We couldn't find enough cards with\n"
                    f"the criteria you provided\n\n"
                    f"Found:     {len(ba_var['made_count'])}\n"
                    f"Requested: {ba_var['tried']}\n"
                    f"Please try again..."
                )
            elif type(ba_var["made_count"]) == int:
                self.ui.lab_reb_comms_title.setText(
                    f"We couldn't find enough cards with\n"
                    f"the criteria you provided\n\n"
                    f"Found:     {ba_var['made_count']}\n"
                    f"Requested: {ba_var['tried']}\n"
                    f"Please try again..."
                )
            else:
                self.ui.lab_reb_comms_title.setText(
                    f"There was a problem.\n" f"Please try again..." f"EC 892"
                )
            ow = self.ui.lab_reb_comms_title.width()
            oh = self.ui.lab_reb_comms_title.height()
            self.ui.lab_reb_comms_title.adjustSize()
            w = self.ui.lab_reb_comms_title.width()
            h = self.ui.lab_reb_comms_title.height()
            dw = w - ow
            dh = h - oh
            self.resize((self.width() + dw), (self.height() + dh))
            bb_ox = self.ui.buttonBox_reb_comms.x()
            bb_oy = self.ui.buttonBox_reb_comms.y()
            bb_nx = bb_ox + (dw / 2)
            bb_ny = bb_oy + dh
            bb_w = self.ui.buttonBox_reb_comms.width()
            bb_h = self.ui.buttonBox_reb_comms.height()
            self.ui.buttonBox_reb_comms.setGeometry(bb_nx, bb_ny, bb_w, bb_h)
            mw.battle_window.showHome()
        logger_ui.info("RebComms instance initiated")


class TY(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the form on the ty window
        self.ui = Ui_Dialog_ty()
        self.ui.setupUi(self)
        self.setModal(True)

        # center the window
        qtRectangle = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        logger_ui.info("TY instance initiated")
        self.show()
        return


class ISD(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the form on the ty window
        self.ui = Ui_Dialog_in_dis()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.closeEvent = self.closeEvent

        # center the window
        qtRectangle = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.ui.frame.setStyleSheet(
            f".QFrame"
            f"{{"
            f"background: QLinearGradient( x1: 0.3, y1: 0,"
            f" x2: 0.6, y2: 0.7,"
            f" stop: 0 {COLOR_CIMED_ORANGE},"
            f" stop: 1 {COLOR_CIMED_BLUE});"
            f"}}"
            f"QLabel"
            f"{{"
            f"color: {COLOR_NEAR_WHITE_GRAY}"
            f"}}"
        )

        self.ui.lab_pid.setText(f"{deID}")

        self.show()

        logger_ui.info("ISD instance initiated")
        return


class OptDia(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the form on the ask window
        self.ui = Ui_OptionsDialog()
        self.ui.setupUi(self)
        self.ui.closeEvent = self.closeEvent

        # center it
        qtRectangle = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)

        self.ui.label_version.setText(f"v{BA_VER}")
        self.ui.label_version.clicked.connect(lambda: openfolder(LOG_FOLD))

        sb = self.ui.spinbox_bdecksize_opts
        sb.valueChanged.connect(lambda: spinbox_val_change(sb.value(), "opt"))

        self.ui.but_apply.clicked.connect(self.apply_selected_options)

        if mw.pm.night_mode() is True:
            self.ui.frame_ctype.setStyleSheet(
                "QFrame{background-color: rgb(255, 250, 250, 50);}"
                "QLabel#lab_cardtype{background-color: rgb(0, 0, 0, 0);}"
                "QLabel#lab_cardtype_2{background-color: rgb(0, 0, 0, 0);}"
            )
            self.ui.frame_corder.setStyleSheet(
                "QFrame{background-color: rgb(255, 250, 250, 50);}"
                "QLabel#lab_cardtype_3{background-color: rgb(0, 0, 0, 0);}"
                "QLabel#lab_cardtype_4{background-color: rgb(0, 0, 0, 0);}"
            )
        else:
            self.ui.frame_ctype.setStyleSheet(
                "QFrame{background-color: rgb(255, 250, 250);}"
                "QLabel#lab_cardtype{background-color: rgb(0, 0, 0, 0);}"
                "QLabel#lab_cardtype_2{background-color: rgb(0, 0, 0, 0);}"
            )
            self.ui.frame_corder.setStyleSheet(
                "QFrame{background-color: rgb(255, 250, 250);}"
                "QLabel#lab_cardtype_3{background-color: rgb(0, 0, 0, 0);}"
                "QLabel#lab_cardtype_4{background-color: rgb(0, 0, 0, 0);}"
            )

        self.ui.checkBox_match_q.hide()
        self.ui.lab_matched_desc.hide()
        self.ui.checkBox_card_mature.hide()
        self.ui.checkBox_no_overdue.hide()

        self.set_OptDia_ui()

        logger_ui.info("OptDia instance initiated")
        return

    def closeEvent(self, event):
        self.apply_selected_options()
        return

    def update_boxes(self):
        global ba_var

        try:
            ba_var["decksize"] = ba_var["spinbox_decksize"] = (
                self.ui.spinbox_bdecksize_opts.value()
            )

            if self.ui.radioButton_random.isChecked():
                ba_var["card_order"] = DYN_RANDOM
                ba_var["card_order_str"] = "Random order"
            elif self.ui.radioButton_due.isChecked():
                ba_var["card_order"] = DYN_DUE
                ba_var["card_order_str"] = "Order due"
            elif self.ui.radioButton_odue.isChecked():
                ba_var["card_order"] = DYN_DUEPRIORITY
                ba_var["card_order_str"] = "Order of relative overdueness"

            # if self.ui.checkBox_match_q.isChecked():
            #     ba_var['matched_box'] = True
            # else:
            #     ba_var['matched_box'] = False

            if self.ui.checkBox_card_new.isChecked():
                ba_var["new_box"] = True
                ba_var["card_type_str"] = "News Only"
            else:
                ba_var["new_box"] = False
            if self.ui.checkBox_card_learn.isChecked():
                ba_var["learn_box"] = True
                ba_var["card_type_str"] = "Reviews Only"
            else:
                ba_var["learn_box"] = False
            if self.ui.checkBox_newANDreview.isChecked():
                ba_var["new_box"] = False
                ba_var["learn_box"] = False
                ba_var["new_AND_review_box"] = True
                ba_var["card_type_str"] = "Both news & reviews"
            else:
                ba_var["new_AND_review_box"] = False

            # if self.ui.checkBox_card_mature.isChecked():
            #     ba_var['mature_box'] = True
            # else:
            #     ba_var['mature_box'] = False

            if self.ui.checkBox_apply_resched.isChecked():
                ba_var["resched_box"] = True
            else:
                ba_var["resched_box"] = False
            if self.ui.checkBox_todayonly.isChecked():
                ba_var["today_only"] = True
            else:
                ba_var["today_only"] = False

            if self.ui.checkBox_joins.isChecked():
                ba_var["joiners_box"] = True
            else:
                ba_var["joiners_box"] = False

            if hasattr(mw, "battle_window"):
                mw.battle_window.update_home_labels()

            logger_ui.debug("update_boxes() completed")
            return
        except Exception as err:
            show_and_log(f"There was a problem..." f"Sorry!" f"EC 545")
            mw.battle_window.timer.stop()

    def set_OptDia_ui(self):
        recall_boxes()

        self.ui.spinbox_bdecksize_opts.setValue(ba_var["decksize"])
        self.ui.checkBox_card_learn.setChecked(ba_var["learn_box"])
        self.ui.checkBox_newANDreview.setChecked(ba_var["new_AND_review_box"])
        self.ui.checkBox_card_new.setChecked(ba_var["new_box"])
        if ba_var["card_order"] == DYN_RANDOM:
            self.ui.radioButton_random.setChecked(True)
        else:
            self.ui.radioButton_random.setChecked(False)
        if ba_var["card_order"] == DYN_DUE:
            self.ui.radioButton_due.setChecked(True)
        else:
            self.ui.radioButton_due.setChecked(False)
        if ba_var["card_order"] == DYN_DUEPRIORITY:
            self.ui.radioButton_odue.setChecked(True)
        else:
            self.ui.radioButton_odue.setChecked(False)
        self.ui.checkBox_apply_resched.setChecked(ba_var["resched_box"])
        self.ui.checkBox_todayonly.setChecked(ba_var["today_only"])
        self.ui.checkBox_joins.setChecked(ba_var["joiners_box"])

        self.show()

        logger_ui.info(f"set_OptDia_ui completed")
        return  # showInfo(f'store data:\n{store_data}')

    def apply_selected_options(self):
        # if ba_var['new_box'] and ba_var['mature_box']:
        #     show_and_log("New cards can't be mature...\n"
        #                  "you haven't done them yet!")
        #     return False
        if (
            self.ui.checkBox_card_new.isChecked()
            and self.ui.checkBox_todayonly.isChecked()
        ):
            show_and_log(
                "New cards can't be due today because  \n"
                "   they don't have a due date\n\n"
                " You'll need to uncheck Bailey Mode\n"
                "    if you want to do new cards..."
            )
            return False
        if (
            self.ui.checkBox_newANDreview.isChecked()
            and self.ui.checkBox_todayonly.isChecked()
        ):
            show_and_log(
                "New cards can't be due today because  \n"
                "   they don't have a due date\n\n"
                " You'll need to uncheck Bailey Mode\n"
                "    if you want to include new cards..."
            )
            return False
        if self.ui.checkBox_card_new.isChecked() and (
            self.ui.radioButton_due.isChecked() or self.ui.radioButton_odue.isChecked()
        ):
            show_and_log(
                "New cards can't be due today because\n"
                "   they don't have a due date\n\n"
                "You'll need to change the order to random  \n"
                "    if you want to do new cards..."
            )
            return False

        else:
            self.update_boxes()
            store_before_send()
            get_loc_req_opts()
            self.close()

            logger_user.info("apply_selected_options completed")
            return  # showInfo(f'store data:\n{store_data}')  # True


# ######################################################################################################################


def accepted():
    logger_user.info("accepted clicked")
    global ba_var
    global dyn_id
    ba_var["ready_for_request"] = False
    ba_var["inbattle"] = 2  # "In Battle"
    build_terms_of_battle()
    if ba_var["matched_box"]:
        # send applicable cards to server
        build_matched_list()
        if ba_var["matched_size"] >= ba_var["decksize"]:
            ba_var["accepted_req"] = True
            dyn_id = make_battle_deck(ba_var["matched_terms"])
        else:
            ba_var["accepted_req"] = True
            ba_var["make_deck_problem"] = True
            show_and_log(
                f"There are not enough cards that match\n"
                f"the criteria! Try again!\n\n"
                f"      Only this many match:  {ba_var['matched_size']}\n"
                f"But we tried for this many:  {ba_var['decksize']}"
            )
    elif not ba_var["matched_box"]:
        ba_var["accepted_req"] = True
        dyn_id = make_battle_deck(ba_var["terms_of_battle"])
    get_local_data()
    mw.battle_window.timer_undo_accepted.start(15 * 1000)
    logger_ui.info("accepted completed")


def answered_card(*args, **kwargs):
    global ba_var
    if ba_var["inbattle"] == 2 or ba_var["inbattle"] == 3:
        ba_var["cards_left"] = sum(list(mw.col.sched.counts()))
    cards_time_today()
    logger_user.info("answered_card completed")


def auto_timeout_reject():
    mw.ask_deck.timer_ask.stop()
    if ba_var["inbattle"] == 0 or ba_var["inbattle"] == 1:
        mw.ask_deck.close()
        mw.battle_window.timer_undo_rejected.start(6 * 1000)
    logger_ui.info("auto_timeout_reject completed")


def ba_init():  # on gui_hooks._ProfileDidOpenHook().append(ba_init)
    # global  ba_var
    # ba_var = read(X_CONFIG_NAME)[2]
    get_user_config()
    start_logger(deb=DEBUG_MODE)
    logger_user.info(f"ba_init by: {mw.pm.name}")
    make_bw()
    start_client_conn()
    # running()

    check_timer()

    logger_user.info(f"{sys._getframe().f_code.co_name} completed")

    start_receiving()
    cards_time_today()
    # event_trigger(ANKI_STARTED)
    return


# def testmet_1():
#     """
#     got_data in dictionary:
#     "activity": activity,
#         # individual cal-heatmap dates need to be in ms:
#     "start": first_day * 1000 if first_day else None,
#     "stop": last_day * 1000 if last_day else None,
#     "today": self.today * 1000,
#     "offset": self.offset,
#     "stats": {
#         "streak_max": {"type": "streak", "value": streak_max},
#         "streak_cur": {"type": "streak", "value": streak_cur},
#         "pct_days_active": {"type": "percentage", "value": pdays},
#         "activity_daily_avg": {"type": "cards", "value": avg_cur},
#
#     """
#     dtt = dt
#     # ar = ActivityReporter(mw.col)
#     # got_data = ar.getData(9, 2)     #days in the past, days in the future
#     # act = got_data['activity']      #dict keys = day(epochsecs) : cards done
#     # dates = [
#     #         dtt.fromtimestamp(d) for d in
#     #         got_data['activity'].keys()
#     # ]
#     # return act


def dummys():
    global ba_var
    # global ba_var['challenger_progress']
    ba_var["challenger_ip"] = ["dummy"]
    ba_var["challenger_name"] = [mw.pm.name]
    # save_ba_var
    return


def stats_cum(days: int = 1):
    """
    cumulative
    days = how many days back? (to count yesterday, d = 2)
    gets the number of cards, time in sec, again count, learn, review, relearn, and
    filtered card counts
    """

    def specStats(self):
        lim = self._revlogLimit()
        if lim:
            lim = " and " + lim
        cards, thetime, failed, lrn, rev, relrn, filt = self.col.db.first(
            f"""
        select count(), sum(time)/1000,
        sum(case when ease = 1 then 1 else 0 end), /* failed */
        sum(case when type = {REVLOG_LRN} then 1 else 0 end), /* learning */
        sum(case when type = {REVLOG_REV} then 1 else 0 end), /* review */
        sum(case when type = {REVLOG_RELRN} then 1 else 0 end), /* relearn */
        sum(case when type = {REVLOG_CRAM} then 1 else 0 end) /* filter */
        from revlog where id > ? """
            + lim,
            (self.col.sched.day_cutoff - (86400 * days)) * 1000,
        )
        return cards, thetime, failed, lrn, rev, relrn, filt

    CollectionStats.specStats = specStats
    result = mw.col.stats().specStats()

    return result


def stats_qd(days: int = 1, stop: int = 0):
    """
    per day for a given timeframe
    days = how many days back? (1 is today, 2 includes yesterday)
    stop = look till when? 0 is to current, 1 is to yesterday
    gets the number of cards, time in sec, again count, learn, review, relearn, and
    filtered card counts
    """
    now = dt.now()
    end = int(dt(now.year, now.month, now.day - 1).timestamp()) - 86400 * stop

    def uspecStats(self):

        start = self.col.sched.day_cutoff - (86400 * (days + 1))  # * 1000
        dts = dt.fromtimestamp(start)
        dtss = dt(dts.year, dts.month, dts.day)
        dtsss = int(dtss.timestamp())

        sched_offset = (dts - dtss).total_seconds()

        tz_offset = (dt.now() - dt.utcnow()).total_seconds()

        lims = []
        lims = [f"day >= {dtsss}", f"day < {end}"]

        deck_limit = self._revlogLimit()
        if deck_limit:
            lims.append(deck_limit)

        lim = "WHERE " + " AND ".join(lims) if lims else ""
        sumthin = f"""
select CAST(STRFTIME('%s', id / 1000 - {sched_offset}, 'unixepoch',
                     'localtime', 'start of day') AS int)
AS day, count(), sum(time)/1000,
        sum(case when ease = 1 then 1 else 0 end), /* failed */
        sum(case when type = {REVLOG_LRN} then 1 else 0 end), /* learning */
        sum(case when type = {REVLOG_REV} then 1 else 0 end), /* review */
        sum(case when type = {REVLOG_RELRN} then 1 else 0 end), /* relearn */
        sum(case when type = {REVLOG_CRAM} then 1 else 0 end) /* filter */
        from revlog {lim}
        GROUP BY day ORDER BY day"""  # + lim

        ans = self.col.db.all(sumthin)
        return ans

    CollectionStats.uspecStats = uspecStats
    result = mw.col.stats().uspecStats()

    return result


def get_pct_corr(t1: Union[int, float] = None, t2: Union[int, float] = None):
    """
    returns percent correct during time frame from t1 to t2 (epoch secs), and total cards
    """
    t1 = (mw.col.sched.day_cutoff - 86400) if not t1 else t1
    t2 = time.time() if not t2 else t2

    [[ct, secs, again, hard]] = mw.col.db.all(
        f"""
select count(), sum(time)/1000,
sum(case when ease = 1 then 1 else 0 end), /* failed */
sum(case when ease = 2 then 1 else 0 end) /* hard */
from revlog where id > {int(t1*1000)} and id < {int(t2*1000)+1000}"""
    )

    pct = (1 - ((again + hard) / ct)) * 100 if ct else 0.00

    return pct, ct, secs


def stats_delta_t(
    t1: Union[dt, int, float],
    t2: Union[dt, int, float] = None,
    to_select: str = "id, cid, usn, ease, ivl, lastIvl, factor, time, type",
):
    """
    returns a list containing the cards answered from
    time t1 to t2 (as datetime or epoch integer or days ago)

    - if t1 is an integer less than 1000, returns the cards completed since that many days ago, using the scheduler cutoff time. yesterday = 1

    - if t2 is not specified, the current time will be used

    :param t1: from when? OR from how many days ago?
    :type t1: Union[dt, int]
    :param t2: to when? (current time if not specified)
    :type t2: Union[dt, int, None]
    :param to_select: optional query string to replace default
    :type to_select: str
    :return: tuple of (list of lists of cards answered within the specified timeframe, delta time)
    :rtype: tuple[list, str]
    """

    def handle_arg(self, t_in: Union[dt, int, float, None]):
        t_in = int(t_in) if type(t_in) == float else t_in

        if type(t_in) == dt:
            return int(t_in.timestamp()) * 1000

        elif t_in is None:
            return int(time.time()) * 1000

        elif type(t_in) == int and t_in <= 1000:
            sco = self.col.sched.day_cutoff
            sc = dt.fromtimestamp(sco)
            s = dt(sc.year, sc.month, sc.day - (t_in + 1), sc.hour)
            return int(s.timestamp()) * 1000

        elif (
            type(t_in) == int and t_in > 1000
        ):  # this 1000 has nothing to do with the others!
            return int(t_in) * 1000 if len(str(int(t_in))) <= 10 else int(t_in)

    def deltaStats(self):
        lims = [f"id >= {t1}", f"id < {t2}"]

        deck_limit = self._revlogLimit()
        if deck_limit:
            lims.append(deck_limit)
        lim = "WHERE " + " AND ".join(lims) if lims else ""

        query = f"""
        SELECT
            {str(to_select)}
        FROM
          REVLOG {lim}
        """

        query = query + "ORDER BY id ASC" if "id" in to_select else query

        ans = self.col.db.all(query)
        return ans

    CollectionStats.handle_arg = handle_arg
    t1 = mw.col.stats().handle_arg(t1)
    t2 = mw.col.stats().handle_arg(t2)

    delta = str(delT(seconds=int((t2 - t1) / 1000)))

    CollectionStats.deltaStats = deltaStats
    result = mw.col.stats().deltaStats()

    return result, delta


def send_log(to_send: str):
    """
    sends the "to_log" dict (that was logged) to the server
    """
    try:

        msg_whead = f"{len(to_send):<{HEADER}}" + to_send
        msg_send = msg_whead.encode(MSG_FORMAT)
        ready_to_send = check_socks(writeables=[mw.socket])
        if len(ready_to_send[1]) > 0:
            mw.socket.send(msg_send)
        logger_comms.debug(f"{sys._getframe().f_code.co_name} completed")
    except Exception as hj:
        show_and_log(f"There was a problem...\n" f"Sorry!\n" f"EC 2056\n" f"{hj}")
        return False

    return True


def new_thread_send_log():
    # ev_th = threading.Thread(target=event_helper,
    #                          daemon=True,
    #                          args=(ev, backlog_start, backlog_end))
    # ev_th.start()

    return


def log_X(
    slist: list, ev: int, evti: str, pevti: str, delta: str, cc: int, others: dict = {}
):  # typ: str,
    """
    takes a dict of stats, and event (and type of event), and a dict of others involved and
    logs it all to X_datalog.jsonl, returning the logged dict
    :param slist: dict of stats to log
    :type slist: dict
    :param ev: event to log
    :type ev: str
    :param evti: time of event
    :type evti: str
    :param pevti: time of previous event
    :type pevti: str
    :param delta: total delta seconds from last event
    :type delta: int
    :param cc: card count from last event
    :type cc: int
    :param others: dict of others' PIDs
    :type others: dict
    :return: the logged dict
    :rtype: dict
    """
    # todo: is ba_var['inbattle'] var correct at this time?
    to_log = {
        "PID": deID,
        "Ev": ev,
        "ib": ba_var["inbattle"],
        # "EvTyp": typ,
        "EvTi": evti,
        "PEvTi": pevti,
        "dT": delta,
        "OPs": others,
        "cc": cc,
        "sdata": slist,
    }
    # pairs = list(to_log.items())
    # get_or_set_X_dict(pairs)

    result = write(to_log, ".jsonl")
    logger_X.info(result)
    return send_log(result)


@debugger_logger
def check_timer():

    if not bw.timer.isActive():
        logger_user.info(f"{sys._getframe().f_code.co_name} restarting timer")
        bw.timer.start(2500)

    logger_user.info(f"{sys._getframe().f_code.co_name} called")

    return


@debugger_logger
def check_if_enrolled():
    if int(deID) in EN_PAR_DIS:
        mw.in_dis = QDialog()
        mw.in_dis = ISD()
    elif int(deID) in EN_PAR_EN:
        bw.update_home_labels()
        bw.showHome()
    else:
        mw.tempbox = QDialog()
        mw.tempbox = TY()
    return


# @debugger_logger
def battle_anki_clicked():  # on action.triggered.connect(lambda: battle_anki_clicked())
    global ba_var
    logger_user.info("battle_anki_clicked started")

    try:
        #  test()      # todo: remove this

        ba_var = read(X_CONFIG_NAME)[2]
        ba_var["inbattle"] = 1
        ba_var["solo"] = False
        save_ba_var()

        if "socket_open" in ba_var.keys() and ba_var["socket_open"] is False:
            logger_user.info(
                f"{sys._getframe().f_code.co_name} if socket_open == False"
            )

            start_client_conn()
            # running()
            start_receiving()

        if "utd_ver" in server_data.keys():
            if server_data["utd_ver"] is not None:
                c1 = str(local_data["ver"]).split(".")
                s1 = str(server_data["utd_ver"]).split(".")

                if int(c1[0]) < int(s1[0]) or int(c1[1][:2]) < int(s1[1]):
                    utd_ver = str(server_data["utd_ver"])
                    show_and_log(
                        f"An Anki with Friends upgrade is available!\n\n"
                        f" The most current version is:\n"
                        f"         {utd_ver}\n\n"
                        f"     Your version is:\n"
                        f"         {BA_VER}\n\n"
                    )

        check_timer()

        cards_time_today()
        # ba_var = read(X_CONFIG_NAME)[2]
        # check_if_enrolled()
        bw.update_home_labels()
        bw.showHome()

        ## bw.start_load_bw()

        logger_ui.info("battle_anki_clicked completed")

        return

    except Exception as e1:
        show_and_log(
            f"There was a problem starting Anki with Friends...\n\n"
            f"Please check the config options in\n"
            f"Tools -> Addons -> Anki with Friends -> Config\n"
            f"If problems persist, please report:\n\n"
            f"Error Code 2257",
            True,
        )
        mw.battle_window.timer.stop()
        if mw.battle_window.main_win.isVisible():
            mw.battle_window.main_win.setDisabled(True)


def build_matched_list():
    global ba_var
    # try:
    ba_var["matched_list"] = []
    # get challenger's applicable cards back and make deck
    card_ids = mw.col.find_cards(ba_var["terms_of_battle"])
    for z in ba_var["requesters_cards"]:
        for key, value in z.items():
            if value in card_ids:
                ba_var["matched_list"].append(value)
                if len(ba_var["matched_list"]) >= ba_var["decksize"]:
                    break
    ba_var["matched_size"] = len(ba_var["matched_list"])
    if ba_var["matched_size"] > 0:
        ba_var["matched_terms"] = str()
        count = 0
        while count <= ba_var["decksize"]:
            ba_var["matched_terms"] += f" or cid:{ba_var['matched_list'][count]}"
            count += 1
    ba_var["matched_terms"] = ba_var["matched_terms"][4:]
    local_data["matched terms"] = ba_var["matched_terms"]
    logger_ui.info("build_matched_list completed")
    # except:
    #     pass


def build_terms_of_battle():
    global ba_var
    ba_var["terms_of_battle"] = (
        f'"deck:{use_deck}" {xtra_search}' if xtra_search else f'"deck:{use_deck}"'
    )
    if ba_var["new_box"]:
        ba_var["terms_of_battle"] += " is:new"
    if ba_var["learn_box"]:
        ba_var["terms_of_battle"] += " -is:new"
    if ba_var["mature_box"]:
        ba_var["terms_of_battle"] += " prop:ivl>21"
    if ba_var["today_only"]:
        ba_var["terms_of_battle"] += " is:due"
    logger_utils.info(
        f"build_terms_of_battle completed\n" f"terms:| {ba_var['terms_of_battle']}"
    )


def bye_to_server():
    logger_comms.info("bye_to_server STARTED")
    mw.socket.settimeout(0.0)
    try:
        msg_whead = f"{len(DISCONN_MSG):<{HEADER}}" + DISCONN_MSG
        msg_send = msg_whead.encode(MSG_FORMAT)
        ready_to_send = check_socks(writeables=[mw.socket])
        if len(ready_to_send[1]) > 0:
            mw.socket.send(msg_send)
            mw.socket.shutdown()
            mw.socket.close()
            logger_comms.info("bye_to_server SHUTDOWN THE SOCKET")
        logger_comms.info("bye_to_server completed")
    except:
        show_and_log(
            f"There was a problem closing the connection to the server...\n"
            f"Error Code 2383\n"
        )
    # finally:
    #     return


@debugger_logger
def cards_time_today():
    global ba_var
    today_stats = mw.col.stats().todayStats()
    today_list = today_stats.split(" ")
    cards_td, time_td = mw.col.db.first(
        "select count(), sum(time)/1000 " "from revlog where id > ? ",
        (mw.col.sched.day_cutoff - 86400) * 1000,
    )
    ba_var["cards_today"] = cards_td or 0
    ba_var["time_secs"] = time_td or 0  # in seconds!!!
    if ba_var["time_secs"] > 0:
        ty_res = time.gmtime(ba_var["time_secs"])
        ba_var["time_today"] = time.strftime("%H:%M", ty_res)
        if int(ba_var["time_today"][0]) == 0:
            ba_var["time_today"] = ba_var["time_today"][1:]
    else:
        ba_var["time_today"] = "0:00"

    save_ba_var()
    logger_utils.info("cards_time_today completed")
    return


def check_for_joins():
    global ba_var
    # global sd
    global local_data

    if ba_var["inbattle"] == 2 and sd:  # in battle that is not solo
        for rd in [
            d
            for d in sd
            if "req Remote IPs" in d["request options"].keys()
            if ba_var["loc_rem_ip"] in d["request options"]["req Remote IPs"]
            if d["user info"]["Remote IP"] not in ba_var["challenger_ip"]
            if d["request options"]["req Remote IP"] == ""
            if d["user info"]["accepted req"]
            if d["user info"]["in battle?"] == 2
        ]:
            ba_var["challenger_ip"].append(rd["user info"]["Remote IP"])
            ba_var["challenger_name"].append(rd["user info"]["name"])
            ba_var["challenger_progress"].append(0)
            ba_var["acc_list"].append(0)
            ba_var["conn"].append(2)  # will add 'joined the game' to progbar text
    logger_ui.debug("check_for_joins completed")


def check_for_requests():
    global ba_var
    # global sd
    global local_data
    # try:
    if (
        ba_var["popped_req"] is False
        and ba_var["ready_for_request"] is True
        and ba_var["inbattle"] == 1
    ):
        # if local_data['user info']['in battle?'] is False:
        if len(sd) > 1:
            for rd in [
                c
                for c in sd
                if len(c["request options"]["req Remote IP"]) > 0
                if (
                    ba_var["loc_rem_ip"] in c["request options"]["req Remote IP"]
                    or (
                        "req Remote IPs" in c["request options"].keys()
                        and ba_var["loc_rem_ip"]
                        in c["request options"]["req Remote IPs"]
                    )
                )
            ]:
                if not_dup_request(
                    rd["user info"]["Remote IP"], rd["user info"]["in battle?"]
                ):
                    if str(rd["user info"]["name"]) not in ba_var["challenger_name"]:
                        ba_var["challenger_name"].insert(
                            0, str(rd["user info"]["name"])
                        )
                    if str(rd["user info"]["Remote IP"]) not in ba_var["challenger_ip"]:
                        ba_var["challenger_ip"].insert(
                            0, str(rd["user info"]["Remote IP"])
                        )

                    if "req Remote IPs" in rd["request options"].keys():
                        for nc in [
                            c
                            for c in sd
                            if c["user info"]["Remote IP"]
                            not in ba_var["challenger_ip"]
                            if c["user info"]["Remote IP"] != ba_var["loc_rem_ip"]
                            if c["user info"]["Remote IP"]
                            in rd["request options"]["req Remote IPs"]
                        ]:
                            ba_var["challenger_ip"].append(nc["user info"]["Remote IP"])
                            ba_var["challenger_name"].append(nc["user info"]["name"])
                            ba_var["challenger_progress"].append(0)

                    if len(rd["card ids"]) > 1:
                        ba_var["requesters_cards"] = list(rd["card ids"])
                    mw.ask_deck = QDialog()
                    mw.ask_deck = AskDialog()
                    mw.ask_deck.fill_options(rd["request options"])

                    ba_var["popped_req"] = True
                    ba_var["ready_for_request"] = False

                    mw.ask_deck.timer_ask.start(26 * 1000)
                    mw.ask_deck.show()
                    logger_comms.debug(
                        "check_for_requests completed and initiatied AskDialog"
                    )
    logger_comms.debug("check_for_requests completed WITHOUT AskDialog")
    return
    # except Exception as mxg:
    #     show_and_log(f'{mxg}')


def check_if_req_accepted():
    global ba_var
    # global sd
    global local_data
    # try:
    if (
        (ba_var["popped_comms"] is False)
        and (ba_var["inbattle"] == 0 or ba_var["inbattle"] == 1)
        and len(local_data["request options"]["req Remote IP"]) > 0
    ):
        for rd in [
            d
            for d in sd
            if d["user info"]["Remote IP"] in ba_var["challenger_ip"]
            if d["user info"]["accepted req"] is True
            if d["user info"]["in battle?"] == 2
        ]:
            ba_var["chal_index"] = ba_var["challenger_ip"].index(
                rd["user info"]["Remote IP"]
            )
            ba_var["challenger_ip"].insert(
                0, ba_var["challenger_ip"].pop(ba_var["chal_index"])
            )
            ba_var["challenger_name"].insert(
                0, ba_var["challenger_name"].pop(ba_var["chal_index"])
            )
            if "deck problem" in rd["user info"].keys():
                if rd["user info"]["deck problem"] is True:
                    ba_var["opponent_problem"] = rd["user info"]["deck problem"]
            if ba_var["matched_box"] is True:
                ba_var["matched_terms"] = rd["matched terms"]
            ba_var["popped_comms"] = True
            ba_var["challenger_progress"][0] = 0
            latestart()
            mw.comms = QDialog()
            mw.comms = RebComms()
            mw.comms.show()
            logger_ui.info("check_if_req_accepted and yes it was")
            return
    logger_ui.debug("check_if_req_accepted completed OUTSIDE of IF FOR loop")


def check_socks(
    readables=None, writeables=None, exceptioners=None, tmout: float = 0.0
) -> list:
    try:
        if readables is None:
            readables = []
        if writeables is None:
            writeables = []
        if exceptioners is None:
            exceptioners = []
        ready_reads, ready_writes, in_errors = select.select(
            readables, writeables, exceptioners, tmout
        )
        logger_utils.debug("check_socks() completed")
        return [ready_reads, ready_writes, in_errors]
    except:
        show_and_log(f"Sorry, there was a problem with Anki with Friends..." f"EC 2451")


def close_down():
    global ba_var
    ba_var["shutdown"] = True
    event_trigger(ANKI_CLOSED)
    try:
        mw.battle_window.close_all()
    except:
        pass
    finally:
        logger_utils.info("close_down completed")
        logging.shutdown()
        return


@debugger_logger
def delete_battle_decks():
    try:
        d = 1
        while mw.col.decks.id_for_name("Battle Deck %d" % d):
            the_id = mw.col.decks.id_for_name("Battle Deck %d" % d)
            mw.col.sched.emptyDyn(the_id)
            mw.col.decks.rem(the_id)
            logger_utils.warning("delete_battle_decks() DELETED 1 Battle Deck")
            d += 1
        mw.moveToState("deckBrowser")
        mw.maybeReset()
    except Exception as msg:
        show_and_log(
            f"Sorry, there was an error removing the Battle Deck...\n"
            f"Error Code 1775\n"
            f"{msg}"
        )
    finally:
        logger_utils.info("delete_battle_decks completed")
        return


def deltacien(cd: dict):
    global deltas  # a list of dicts

    def lit():
        logger_comms.info(f"[deltacien]  {cd['user info']['name']}\n{dict_to_str(cd)}")
        return

    if cd["user info"]["Remote IP"] not in [
        x["user info"]["Remote IP"] for x in deltas
    ]:
        deltas.append(cd)
        lit()
        return
    else:
        idx = [x["user info"]["Remote IP"] for x in deltas].index(
            cd["user info"]["Remote IP"]
        )
        s_t = dt.strptime(str(cd["current CST:"]), "%a %b %d %H:%M:%S %Y")
        llg_t = dt.strptime(str(deltas[idx]["current CST:"]), "%a %b %d %H:%M:%S %Y")
        if (
            (s_t - llg_t > delT(minutes=30))
            or (
                "cards today" in cd["user info"].keys()
                and (
                    int(cd["user info"]["cards today"])
                    - int(deltas[idx]["user info"]["cards today"])
                    >= 100
                )
            )
            or (
                "c_t" in cd.keys() and (int(cd["c_t"]) - int(deltas[idx]["c_t"]) >= 100)
            )
        ):
            lit()
            deltas.pop(idx)
            deltas.insert(idx, cd)
            return
        else:
            return


def dict_to_str(in_dict: dict):
    out_str = json.dumps(in_dict, indent=2, sort_keys=True)
    return out_str


def do_Ro():
    handlr.doRollover()
    show_and_log("The logging handler has completed\n" "file rollover. ")


def confOK():
    logger_user.debug("confOK() clicked")
    global ba_var
    get_loc_req_opts()
    store_before_send()
    if mw.battle_window.get_request_data():
        mw.battle_window.startWaitingBar()
        build_terms_of_battle()
        if ba_var["matched_box"] is True:
            requesters_cards_for_matching()
        get_local_data()
        if ba_var["can_sendittt"] is True:
            mw.battle_window.showWait()
            mw.battle_window.timer_denied.start(30 * 1000)
        logger_ui.info("confOK completed and passed")
    else:
        logger_ui.info("confOK FAILED")
        ba_var["inbattle"] = 1


def fmt_n_log(str_chr: list, le=80, str_log=""):
    """
    to omit the HEADER linebreak '\n', place False as third item in tuple [(s1,c1, False), (s2,c2)]
    :param str_chr: a list of tuples [(s1,c1), (s2,c2)] with 'string to log', 'character to fill'
    :param le: length of line output, including fill characters
    :param str_log: a string you want to append this to
    :return: the formatted string
    """
    try:
        for s in range(len(str_chr)):
            if len(str_chr[s]) > 2 and str_chr[s][2] is False:
                str_log += str_chr[s][0]
            else:
                p1 = f"{str_chr[s][0]:{str_chr[s][1]}^{le}}"
                str_log += "\n" + p1
        return str_log
    except:
        show_and_log(
            f"There was a problem with Anki with Friends..." f"Error Code 2520"
        )


def get_loc_req_opts():
    global local_data
    local_data["request options"]["both box"] = ba_var["new_AND_review_box"]
    local_data["request options"]["deck size"] = ba_var["decksize"]
    local_data["request options"]["matched box"] = ba_var["matched_box"]
    local_data["request options"]["new box"] = ba_var["new_box"]
    local_data["request options"]["learn box"] = ba_var["learn_box"]
    local_data["request options"]["mature box"] = ba_var["mature_box"]
    local_data["request options"]["resched box"] = ba_var["resched_box"]
    local_data["request options"]["due box"] = ba_var["today_only"]
    local_data["request options"]["requester"] = str(mw.pm.name)

    logger_utils.debug("get_loc_req_opts completed")
    return


def get_local_data():
    logger_ui.debug("get_local_data STARTED")
    global local_data

    record_readys()

    local_data["matched size"] = ba_var["matched_size"]
    local_data["matched terms"] = ba_var["matched_terms"]
    local_data["window open"] = ba_var["window_open"]
    local_data["user info"]["Connected"] = ba_var["socket_open"]
    local_data["user info"]["in battle?"] = ba_var["inbattle"]
    local_data["user info"]["accepted req"] = ba_var["accepted_req"]
    local_data["user info"]["progress"] = ba_var["myprogress"]
    local_data["user info"]["Remote IP"] = ba_var["loc_rem_ip"]
    local_data["user info"]["name"] = str(mw.pm.name)
    local_data["user info"]["deck problem"] = ba_var["make_deck_problem"]
    local_data["user info"]["pfrac"] = [ba_var["cards_left"], ba_var["decksize"]]

    local_data["user info"]["deID"] = deID

    if ba_var["challenger_name"] and ba_var["challenger_ip"]:
        local_data["request options"]["req names"] = ba_var["challenger_name"]
        local_data["request options"]["req Remote IPs"] = ba_var["challenger_ip"]

    if ba_var["badgeview"] is True:
        local_data["user info"]["cards today"] = ba_var["cards_today"]
        local_data["user info"]["time today"] = ba_var["time_today"]
    if ba_var["badgeview"] is False:
        if "cards today" in local_data["user info"].keys():
            del local_data["user info"]["cards today"]
            local_data["c_t"] = ba_var["cards_today"]
        local_data["user info"]["time today"] = " "
    logger_ui.debug("get_local_data completed")
    return


def inbattle_status():
    global ba_var
    if ba_var["inbattle"] == 1:
        ba_var["inbattle_str"] = "Ready"
        # save_ba_var()
        logger_utils.debug(f"inbattle_status completed: {ba_var['inbattle_str']}")
        return "Ready"

    elif ba_var["inbattle"] == 2:
        ba_var["inbattle_str"] = "In Battle"
        # save_ba_var()
        logger_utils.debug(f"inbattle_status completed: {ba_var['inbattle_str']}")
        return "In Battle"
    elif ba_var["inbattle"] == 3:
        ba_var["inbattle_str"] = "Solo"
        # save_ba_var()
        logger_utils.debug(f"inbattle_status completed: {ba_var['inbattle_str']}")
        return "Solo"
    elif ba_var["inbattle"] == 0:
        ba_var["inbattle_str"] = "Away"
        # save_ba_var()
        logger_utils.debug(f"inbattle_status completed: {ba_var['inbattle_str']}")
        return "Away"


def latestart():
    global local_data
    global dyn_id
    if ba_var["matched_box"] is False:
        dyn_id = make_battle_deck(ba_var["terms_of_battle"])
    elif ba_var["matched_box"] is True:
        dyn_id = make_battle_deck(ba_var["matched_terms"])
    mw.battle_window.timer_undo_request.start(15 * 1000)
    logger_ui.info("latestart completed")


def list_mod(inlist: list):
    logger_utils.debug(
        f"[SERVER DATA]:\n" f"[Connected]: {len(sd)}\n" f"{dict_to_str(server_data)}"
    )
    logger_utils.debug("list_mod STARTED")
    for d in inlist:

        if (
            "cards today" in d["user info"].keys()
            and int(d["user info"]["cards today"]) > 0
        ):
            cds = str(d["user info"]["cards today"])
        elif "c_t" in d.keys():
            cds = str(d["c_t"])
        else:
            cds = "NA"

        v = str(d["ver"]) if "ver" in d.keys() else ""

        idx = inlist.index(d)
        q = inlist.pop(idx)
        q["user info"]["name"] = f"{v}${cds}${q['user info']['name']}"
        inlist.insert(idx, q)
        deltacien(d)
    logger_utils.debug("list_mod completed")
    return inlist


def log_bat_info(add_str=""):
    pfcs = [
        ch["user info"]["pfrac"]
        for ch in sd
        if "pfrac" in ch["user info"].keys()
        if ch["user info"]["Remote IP"] in ba_var["challenger_ip"]
    ]
    l1 = f"[{mw.pm.name} vs. {ba_var['challenger_name']}]"
    l2 = f"[{ba_var['myprogress']}% vs. {ba_var['challenger_progress']}%]"
    l3 = f"[{[ba_var['cards_left'], ba_var['decksize']]} v  {pfcs}]"
    sl = fmt_n_log([(l1, "$"), (l2, "-"), (l3, "*")])
    if add_str:
        sl += add_str
    logger_utils.info(sl)


@debugger_logger
def mod_show_list(in_list: list):
    out_list = []

    # if deID in ADMIN_LIST:
    for user in in_list:
        if "deID" in user["user info"].keys():
            out_list.append(user)
        else:
            user["user info"]["deID"] = 0000
            out_list.append(user)
    return out_list
    # elif deID in EN_PAR_EN:
    #     out_list = [p for p in in_list
    #                 if 'deID' in p['user info'].keys()
    #                 and p['user info']['deID'] in EN_PAR_EN]
    #                 #  and not p['user info']['deID'] in ADMIN_LIST
    #     return out_list
    # return


def log_check_prog():
    global ba_var

    if ba_var["inbattle"] == 2:
        ba_var["one_to_ten"] = False
        ba_var["ff_ff"] = False
        ba_var["nty"] = False
        # save_ba_var()
        return
    elif (
        ba_var["inbattle"] == 2
        and (1 < ba_var["myprogress"] < 10)
        and len(ba_var["challenger_name"]) > 0
        and ba_var["one_to_ten"] is False
    ):
        log_bat_info()
        ba_var["one_to_ten"] = True
        # save_ba_var()
        return
    elif (
        ba_var["inbattle"] == 2
        and (45 < ba_var["myprogress"] < 55)
        and len(ba_var["challenger_name"]) > 0
        and ba_var["ff_ff"] is False
    ):
        log_bat_info()
        ba_var["ff_ff"] = True
        # save_ba_var()
        return
    # elif ba_var['inbattle'] is True and ba_var['myprogress'] > 90 and len(ba_var['challenger_name']) > 0 and ba_var['nty'] is False:
    #     log_bat_info()
    #     ba_var['nty'] = True
    else:
        return


def make_battle_deck(searchterms, buildsize=None):
    logger_utils.warning("make_battle_deck() STARTED")
    global ba_var
    global n

    def log_make_info(
        mymsg: str, usrmsg: str, ec: int, mc: object = None, exx: str = "None"
    ):
        logger_utils.warning(
            f"{mymsg}\n"
            f"type ba_var['made_count'] == {type(mc)}\n"
            f"val ba_var['made_count'] == {mc}\n"
            f"searchterms: {searchterms}\n"
            f"buildsize: {buildsize}\n"
            f"Exception: {exx}"
        )
        show_and_log(f"{usrmsg}\n\n" f"Error Code: {ec}")
        return

    def deck_del_n_mo():
        global ba_var
        delete_battle_decks()
        ba_var["tried"] = buildsize
        ba_var["make_deck_problem"] = True
        ba_var["inbattle"] = 1
        return

    # import aqt.dyndeckconf

    if buildsize is None:
        buildsize = ba_var["decksize"]
    created_b_deck = False
    n = 1
    try:
        global did
        deck = mw.col.decks.byName(f"{use_deck}")
        did = mw.col.decks.id_for_name(f"{use_deck}")  # deck['id']  #
        did = int(did)
        mw.col.decks.select(did)
        conf = mw.col.decks.confForDid(did)
        if mw.col.decks.selected() != did:
            mw.col.decks.select(did)
            deck = mw.col.decks.confForDid(did)
            cur = mw.col.decks.current()
            log_make_info(
                f"sel deck != did from use_deck",
                f"There may have been a problem creating the deck...\n"
                f"if something doesn't look right, just delete\n"
                f"the blue deck named 'Battle Deck 1'",
                2767,
            )
        else:
            deck = mw.col.decks.current()
    except Exception as excpe:
        emsg = str(
            f"There seems to be a problem in your Config file...\n"
            f"Please navigate to:\n\n"
            f"Tools -> Add-ons -> (select Anki with Friends) -> click Config\n\n"
            f'and double check that the word for the "use_deck":\n'
            f"matches a deck that actually exists in your collection"
        )
        log_make_info(
            f"exception when trying to select use_deck",
            f"{emsg}\n" f"If the problem persists, please report it!",
            2778,
            exx=f"{excpe}",
        )
    while mw.col.decks.id_for_name("Battle Deck %d" % n):
        n += 1
    name = "Battle Deck %d" % n
    did = mw.col.decks.newDyn(name)
    dyn = mw.col.decks.get(did)
    if ba_var["resched_box"]:
        dyn["resched"] = True
    else:
        dyn["resched"] = False

    dyn["delays"] = None
    dyn["terms"] = [
        [str(searchterms), int(buildsize), ba_var["card_order"]]
    ]  # DYN_DUEPRIORITY]]
    mw.col.decks.save(dyn)
    created_b_deck = True

    ba_var["made_count"] = mw.col.sched.rebuildDyn()

    if (
        type(ba_var["made_count"]) == list and len(ba_var["made_count"]) != buildsize
    ):  # old scheduler
        deck_del_n_mo()
        emsg = str(
            f"We couldn't find enough cards with\n"
            f"the criteria provided\n\n"
            f"Added:     {len(ba_var['made_count'])}\n"
            f"Tried:     {ba_var['tried']}\n"
            f"Found:     {len(mw.col.find_cards(searchterms))}\n\n"
        )
        log_make_info(
            f'could not make full deck, "if"', f"{emsg}\n", 2810, ba_var["made_count"]
        )
        return
    elif (
        type(ba_var["made_count"]) == int and ba_var["made_count"] != buildsize
    ):  # new scheduler
        deck_del_n_mo()
        emsg = str(
            f"There weren't enough cards with\n"
            f"the criteria provided\n\n"
            f"Added:     {ba_var['made_count']}\n"
            f"Tried:     {ba_var['tried']}"
            f"Found:     {len(mw.col.find_cards(searchterms))}\n\n"
        )
        log_make_info(
            f'could not make full deck, "elif"', f"{emsg}\n", 2821, ba_var["made_count"]
        )
        return
    elif ba_var["made_count"] is None:
        deck_del_n_mo()
        emsg = str(
            f"We couldn't find any cards with\n"
            f"the criteria provided\n\n"
            f"Added:     {ba_var['made_count']}\n"
            f"Tried:     {ba_var['tried']}\n"
            f"Found:     {len(mw.col.find_cards(searchterms))}\n\n"
        )
        log_make_info(
            f'could not make ANY of deck, "elif"',
            f"{emsg}\n",
            2832,
            ba_var["made_count"],
        )
        return
    else:
        ba_var["make_deck_problem"] = False
        mw.col.decks.select(did)
        mw.moveToState("review")

        mw.battle_window.showBattle()
        logger_utils.warning("make_battle_deck COMPLETED SUCCESSFULLY")
        return did


@debugger_logger
def make_bw():
    global bw
    # global logger_ui
    # global logger_user
    # global logger_comms
    if not hasattr(mw, "battle_window"):
        mw.battle_window = MainWindow()
        bw = mw.battle_window
    return


def name_str(instr: str, tail: int) -> str:
    # REJOINED = ' REJOINED the game!'  # 0
    # JOINED = ' JOINED the game!'      # 1
    # LEFT = ' LEFT the game...'        # 2
    # NOT_HERE = ' is starting...'      # 3
    # NAME_ONLY = ''                    # 4
    # TAILS = [REJOINED, JOINED, LEFT, NOT_HERE, NAME_ONLY]
    x = next((len(t) for t in TAILS if t in instr), None)
    if x:
        logger_utils.debug("name_str completed")
        return str(instr[:-x] + TAILS[tail])

    else:
        logger_utils.debug("name_str completed")
        return str(instr + TAILS[tail])


def not_dup_request(ip, c_status):
    i = readys["ips"].index(ip)
    ct = int(time.time())
    ts = readys["last battle start"][i]
    ms = readys["my last bat start"]
    if ct - ms <= 30:
        logger_ui.debug("not_dup_request returned False" "if ct - ms <= 30:")
        return False
    elif c_status == 2 and ct - ts >= 15:
        # they are IN battle and started MORE than 15s ago
        logger_ui.debug(
            "not_dup_request returned False" "elif c_status is True and ct - ts >= 15:"
        )
        return False
    else:
        logger_ui.debug("not_dup_request returned True")
        return True


def openfolder(filename=LOG_FOLD):
    logger_utils.info("openfolder clicked")
    try:
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])
        logger_utils.info("openfolder completed")
    except:
        logger_utils.warning("openfolder had a problem")


def opts_open():
    logger_user.info("opts_open clicked")

    mw.opts = QDialog()
    mw.opts = OptDia()
    # mw.opts.set_OptDia_ui()

    logger_user.info("opts_open completed: tried new OptDia")
    return


def recall_boxes(indict: list = None):
    global ba_var

    x = read(X_CONFIG_NAME) if indict is None else indict

    ba_var["new_AND_review_box"] = x[2]["new_AND_review_box"]
    ba_var["decksize"] = x[2]["decksize"]
    ba_var["matched_box"] = x[2]["matched_box"]
    ba_var["new_box"] = x[2]["new_box"]
    ba_var["learn_box"] = x[2]["learn_box"]
    ba_var["mature_box"] = x[2]["mature_box"]
    ba_var["resched_box"] = x[2]["resched_box"]
    ba_var["today_only"] = x[2]["today_only"]

    logger_utils.debug("recall_from_store_data completed")

    return


@debugger_logger
def debug_dicts(inlist: list):
    for i in [d for d in inlist if type(d) == dict]:
        logger_comms.debug(f"{json.dumps(i, indent=4, sort_keys=True)}")
    return


# @debugger_logger
def receive():
    global server_data
    global sd
    try:
        logger_comms.warning("receive STARTING OUTER WHILE LOOP")
        while True:
            if ba_var["shutdown"] is True:
                break
            if threading.main_thread().is_alive() is False:
                logger_comms.debug(
                    f"Main Thread no longer alive\n"
                    f"{threading.main_thread().getName()}"
                )
                break
            list_socks_ready = check_socks(readables=[mw.socket], tmout=10.0)
            if len(list_socks_ready[0]) > 0:
                try:
                    full_msg = ""
                    msg_len = int(mw.socket.recv(HEADER))
                    while len(full_msg) < msg_len:
                        chunk = mw.socket.recv(msg_len - len(full_msg))
                        if chunk == b"":
                            break
                        full_msg += chunk.decode(MSG_FORMAT)
                    if len(full_msg) != msg_len:
                        show_and_log(
                            f"Sorry, there was a problem with Anki with Friends..."
                            f"EC U-421"
                        )
                    if len(full_msg) == msg_len:
                        try:
                            threadlocker.acquire()
                            server_data = str_to_dict(full_msg)
                            sd = server_data["clients connected"]
                        except Exception as e1:
                            show_and_log(
                                f"There was a problem receiving data\n"
                                f"from the Anki with Friends server...\n"
                                f"Please try restarting Anki\n"
                                f"Error code 2701\n"
                                f"{e1}",
                                True,
                            )
                        finally:
                            threadlocker.release()
                            logger_comms.debug("receive completed")

                    debug_dicts(sd)
                except Exception as exc:
                    show_and_log(
                        f"Sorry, there was a problem with Anki with Friends...\n"
                        f"EC 3043\n\n"
                        f"{exc}",
                        True,
                    )
                    pass

    except Exception as excepti:
        show_and_log(
            f"Sorry, there was a problem with Anki with Friends...\n"
            f"EC 1010\n\n"
            f"{excepti}",
            True,
        )
        # finally:
        logger_comms.warning("receive() BROKE OUTER WHILE LOOP")
        return


def record_readys():
    global readys
    # global sd

    readys["cc"] = []

    for rd in sd:
        readys["cc"].append(rd["user info"]["Remote IP"])

        if rd["user info"]["Remote IP"] == ba_var["loc_rem_ip"]:
            if rd["user info"]["in battle?"] != 2 and ba_var["inbattle"] == 2:
                readys["my last bat start"] = int(time.time())
        elif rd["user info"]["Remote IP"] in readys["ips"]:
            i = readys["ips"].index(rd["user info"]["Remote IP"])
            if rd["user info"]["in battle?"] == 2 and readys["last status"][i] != 2:
                readys["last battle start"][i] = int(time.time())
                readys["last status"][i] = rd["user info"]["in battle?"]
            else:
                readys["last status"][i] = rd["user info"]["in battle?"]
        elif rd["user info"]["Remote IP"] not in readys["ips"]:
            readys["ips"].append(rd["user info"]["Remote IP"])
            readys["names"].append(rd["user info"]["name"])
            readys["last status"].append(rd["user info"]["in battle?"])
            readys["last battle start"].append(0)

    for ip in [x for x in readys["ips"] if x not in readys["cc"]]:
        z = readys["ips"].index(ip)
        readys["ips"].pop(z)
        readys["names"].pop(z)
        readys["last status"].pop(z)
        readys["last battle start"].pop(z)

    logger_ui.debug("record_readys completed")


def rejected():
    logger_user.debug("rejected() clicked")
    global ba_var
    mw.ask_deck.timer_ask.stop()
    ba_var["ready_for_request"] = False
    # save_ba_var()
    show_and_log(f"You are unable to receive requests for 30 seconds...")
    mw.battle_window.timer_undo_rejected.start(30 * 1000)
    logger_ui.info("rejected clicked & completed")


def req_was_denied(show: bool = True):
    global ba_var
    global local_data

    mw.battle_window.timer_denied.stop()
    local_data["request options"]["req Remote IP"] = ""
    local_data["request options"]["req name"] = ""

    if ba_var["inbattle"] == 2:
        for rd in [
            x
            for x in sd
            if x["user info"]["Remote IP"] in ba_var["challenger_ip"]
            if x["user info"]["in battle?"] != 2
        ]:
            i = ba_var["challenger_ip"].index(rd["user info"]["Remote IP"])
            ba_var["challenger_ip"].pop(i)
            ba_var["challenger_name"].pop(i)
            ba_var["challenger_progress"].pop(i)
            ba_var["acc_list"].pop(i)
            ba_var["conn"].pop(i)
            # save_ba_var()

    if ba_var["inbattle"] == 0 or ba_var["inbattle"] == 1:
        ba_var["requesters_cards"] = list()
        ba_var["terms_of_battle"] = str()
        # save_ba_var()
        mw.battle_window.undorequest()
        mw.battle_window.showHome()
        mw.battle_window.timer_bar.stop()
        mw.battle_window.reset()
        show_and_log(
            f"Sorry, looks like the people you invited\n"
            f"can't play right now...\n\n"
            f"Maybe you are too strong of an AnKing?"
        )
    logger_ui.info("req_was_denied completed")
    return


def requesters_cards_for_matching():
    global local_data
    the_ids = list(mw.col.find_cards(ba_var["terms_of_battle"]))
    i = 0
    if len(the_ids) > 0:
        while i < len(the_ids) and i <= 2000:
            id_to_add = int(the_ids[i])
            add = {"id": id_to_add}
            local_data["card ids"].append(add)
            i += 1
        logger_comms.info("requesters_cards_for_matching completed")
    else:
        show_and_log(
            f"Sorry, no cards matched the criteria provided."
            f"requesters_cards_for_matching"
            f"EC 1079"
        )


def running():
    logger_ui.debug("running STARTED")
    global ba_var
    # global ba_var['ready_for_request']
    # global ba_var['popped_req']
    try:
        if mw.battle_window.main_win.isVisible():
            ba_var["window_open"] = True
        else:
            ba_var["window_open"] = False
            # ba_var['inbattle'] = 0  # Away
            # save_ba_var()
        if ba_var["socket_open"]:
            get_local_data()
            send_pulse()
            mw.battle_window.refresh_users()
            check_if_req_accepted()
            log_check_prog()
            if ba_var["inbattle"] == 1:
                check_for_requests()

            # start_receiving()

        logger_ui.debug("running completed")

    except Exception as meg:
        show_and_log(f"{meg}")
        mw.battle_window.timer.stop()
        if mw.battle_window.main_win.isVisible():
            mw.battle_window.main_win.setDisabled(True)


def send_pulse():
    global local_data
    global log_helper
    try:
        if time.time() - log_helper["LSt"] > 1.5:
            log_helper["LSt"] = int(time.time())
            send_str = dict_to_str(local_data)
            msg_whead = f"{len(send_str):<{HEADER}}" + send_str
            msg_send = msg_whead.encode(MSG_FORMAT)
            ready_to_send = check_socks(writeables=[mw.socket])
            if len(ready_to_send[1]) > 0:
                mw.socket.send(msg_send)
        logger_comms.debug("send_pulse() completed")
    except Exception as hj:
        show_and_log(f"There was a problem...\n" f"Sorry!\n" f"EC 1865\n" f"{hj}")
        mw.battle_window.timer.stop()


def sendittt():
    logger_user.info("sendittt clicked")
    # try:
    mw.confpopup = QDialog()
    mw.confpopup = ConfDialog()
    mw.confpopup.show()
    # except:
    #     show_and_log("something went wrong...")


def show_and_log(instr, exc=False):
    if exc:
        logger_utils.exception(f"\n{instr}")
    else:
        logger_utils.warning(f"\n{instr}")
    showInfo(instr)


def spinbox_save(val: int):
    d = read(X_CONFIG_NAME)
    d[2]["decksize"] = val
    write(d, X_CONFIG_NAME)
    return


def spinbox_timer_handle(val: int):
    if bw:
        bw.spin_timer = spin_timer = QTimer()
    elif mw.opts:
        mw.opts.spin_timer = spin_timer = QTimer()
    else:
        spin_timer = QTimer()

    spin_timer.timeout.connect(lambda: spinbox_save(val))
    spin_timer.setSingleShot(True)

    if spin_timer.isActive():
        spin_timer.stop()
        spin_timer.start(2000)
    else:
        spin_timer.start(2000)

    return


def spinbox_val_change(val: int, src: str):
    global ba_var

    ba_var = read(X_CONFIG_NAME)[2]

    spinbox_timer_handle(val)

    ba_var["decksize"] = val

    if src == "opt":
        mw.battle_window.ui.spinbox_bdecksize_bw.setValue(ba_var["decksize"])
    elif src == "bw":
        try:
            mw.opts.ui.spinbox_bdecksize_opts.setValue(ba_var["decksize"])
        except:
            pass

    save_ba_var()
    return


#  @debugger_logger
def save_ba_var():
    # global ba_var

    x = read(X_CONFIG_NAME)
    x[2] = ba_var
    write(x, X_CONFIG_NAME)
    return x


@debugger_logger
def make_socket():
    global ba_var

    ba_var["socket_open"] = True
    mw.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mw.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096 * 2)
    # mw.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    if ba_var["startup"]:
        mw.socket.settimeout(3)
        ba_var["startup"] = False
        ba_var["shutdown"] = False

    mw.socket.connect((SERVER, PORT))
    ba_var["loc_rem_ip"] = str(mw.socket.getsockname())

    save_ba_var()

    return


@debugger_logger
def start_client_conn():  # ba_init and battle_anki_clicked
    global ba_var

    logger_comms.info("start_client_conn STARTED")

    def stop_it():
        ba_var["socket_open"] = False
        # save_ba_var()
        bw.timer.stop()
        bw.timer_bar.stop()
        if bw.main_win.isVisible():
            bw.main_win.setDisabled(True)
        return

    try:
        if hasattr(mw, "socket"):
            # sockets_checked = sc = check_socks(writeables=[mw.socket])
            if time.time() - log_helper["LSt"] > 20:  # (mw.socket not in sc[0]) or
                make_socket()
                # # todo: delete this test
                # showInfo(f'The socket will be restarted because ?\n\n'
                #          f'readable:\n\n {sc[0]}\n\n'
                #          f'writeable:\n\n {sc[1]}\n\n'
                #          f'mw.socket:\n\n {mw.socket}')

        else:
            # showInfo(f'The socket does not yet exist, will make now')
            make_socket()

        ms = fmt_n_log(
            [
                ("start_client_conn completed", "", False),
                (f"[Connection initiated with {SERVER}]", ":"),
            ]
        )
        logger_comms.info(ms)
        logger_comms.info(f"ba_var['socket_open'] : {ba_var['socket_open']}")
        return
    except socket.error as e:
        show_and_log(
            f"There was a problem starting Anki with Friends...\n\n"
            f"Please check the config options in\n"
            f"Tools -> Addons -> Anki with Friends -> Config\n\n"
            f"And then restart Anki:\n\n"
            f"Error Code U-496",
            True,
        )
        stop_it()


def init_X_logger(path: str):
    global logger_X, handlr_X, formatter_X

    roll_time = dt(
        dt.now().year, dt.now().month, dt.now().day, hour=4, minute=0, fold=1
    )
    handlr_X = logging.handlers.TimedRotatingFileHandler(
        filename=path, when="midnight", backupCount=50, atTime=roll_time
    )

    handlr_X.suffix = "%Y-%m-%d.jsonl"
    handlr_X.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}(\.\w+)?$", re.ASCII)

    def rotating_namer(default_name):
        s = default_name.split(".")
        if s[1] == "jsonl":
            del s[1]
        return ".".join(s)

    handlr_X.rotation_filename = rotating_namer

    formatter_X = MyFormatter(fmt="%(message)s")
    handlr_X.setFormatter(formatter_X)

    logger_X = logging.getLogger("X_logger")
    logger_X.addHandler(handlr_X)
    logger_X.setLevel(logging.INFO)

    return


def init_X_files():
    global LOG_X_FOLD
    global X_LOG_PATH

    if not os.path.exists(LOG_X_FOLD):
        os.makedirs(LOG_X_FOLD)

    X_LOG_PATH = os.path.join(LOG_X_FOLD, X_LOG_NAME)

    init_X_logger(X_LOG_PATH)

    # read(X_CONFIG_NAME, BA_REL_DIR)

    return


def start_logger(deb: bool = False):
    global logger
    global logger_utils
    global logger_comms
    global logger_ui
    global logger_user
    global handlr
    global formatter
    global LOG_FOLD
    global LOG_NM
    global LOG_PATH
    global LOG_X_FOLD

    LOG_FOLD = os.path.join(mw.pm.addonFolder(), "BA_logfiles")

    if not os.path.exists(LOG_FOLD):
        os.makedirs(LOG_FOLD)

    LOG_PATH = os.path.join(LOG_FOLD, LOG_NM)

    LOG_X_FOLD = os.path.join(LOG_FOLD, X_FOLDER_NAME)

    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    switch_daily_at = dt(
        dt.now().year, dt.now().month, dt.now().day, hour=4, minute=0, fold=1
    )
    handlr = logging.handlers.TimedRotatingFileHandler(
        filename=LOG_PATH, when="midnight", backupCount=50, atTime=switch_daily_at
    )

    formatter = MyFormatter(
        fmt="%(asctime)-31s %(name)-6s %(levelname)-6s %(message)s",
        datefmt="%Y/%m/%d  %I:%M:%S.%f %p",
    )
    handlr.setFormatter(formatter)

    logger.addHandler(handlr)

    logger_ui = logging.getLogger("BA_UI")
    logger_user = logging.getLogger("User")
    logger_utils = logging.getLogger("Utils")
    logger_comms = logging.getLogger("Comms")

    if deb:
        logger_ui.setLevel(logging.DEBUG)
        logger_user.setLevel(logging.DEBUG)
        logger_utils.setLevel(logging.DEBUG)
        logger_comms.setLevel(logging.DEBUG)
    else:
        logger_ui.setLevel(logging.INFO)
        logger_user.setLevel(logging.INFO)
        logger_utils.setLevel(logging.INFO)
        logger_comms.setLevel(logging.INFO)

    s0 = (f"BA_VER: {BA_VER}, schdver: {sv}", "", False)
    s1 = ("[Logger Initiated]", "=")
    s2 = (
        f"Next log file rollover:       "
        f"{str(dt.fromtimestamp(handlr.computeRollover(time.time())))[:-7]}",
        " ",
    )
    so = fmt_n_log([s0, s1, s2])  #
    logger_utils.info(so)
    logger_utils.info(dict_to_str(lg_dct))

    return init_X_files()


# @debugger_logger
def start_receiving():

    # @debugger_logger
    def is_receiving(thread_name: str) -> bool:
        return True if thread_name in [t.name for t in threading.enumerate()] else False

    try:
        if not is_receiving("Anki with Friends Receiver"):
            logger_comms.info(f"Starting receive thread from ba_init")
            r_th = threading.Thread(
                target=receive, daemon=False, name="Anki with Friends Receiver"
            )
            r_th.start()
        return

    except socket.error:
        show_and_log(
            f"There was a problem starting Anki with Friends... Sorry!\n\n"
            f"Error Code M-1694",
            True,
        )
        mw.battle_window.timer.stop()


def store_before_send():
    # global ba_var
    x = read(X_CONFIG_NAME)

    x[2] = ba_var

    write(x, X_CONFIG_NAME)

    logger_utils.debug("store_before_send completed")
    return


def str_to_ip(mystr: str):
    myip = str(mystr.split(",")[0])[2:-1]
    myport = int(mystr.split(",")[1][1:-1])
    ip = str(f"('{myip}', {myport})")
    logger_utils.debug("str_to_ip completed")
    return ip


def str_to_dict(in_str: str):
    try:
        out_dict = json.loads(in_str)
        logger_utils.debug("str_to_dict completed")
        return out_dict
    except json.JSONDecodeError as jsonerro:
        show_and_log(f"there was a problem\n" f"{jsonerro}" f"str_to_dict\n" f"EC 189m")
    except RecursionError as recur:
        show_and_log(f"there was a problem\n" f"{recur}" f"str_to_dict\n" f"EC 195m")


def event_helper(ev: int, backlog_start: dt = None, backlog_end: dt = None):
    def roll_ev():
        """
        - rolls over the event times from event to previous event in the log_helper dict of X_config.json
        - also resets the opponent's dictionaries, rewrites PID
        """

        global log_helper

        X[0]["PEv"] = ev
        X[0]["PEvTi"] = dt2s(t2)
        # lh["PEvTyp"] = lh["EvTyp"]
        X[0]["OPs"] = {}
        X[0]["PID"] = deID
        X[0]["LLt"] = X[0]["EvTi"]
        X[0]["LSt"] = log_helper["LSt"]

        write(X, X_CONFIG_NAME)

        log_helper = X[0]

        return

    def should_count():
        cids = []
        cids = [card[1] for card in stat_diff if card[0] > DATES[1][2]]

        if len(cids) > 0:
            if t1 == DATES[1][1]:
                X[0]["cc"] = len(cids)
            else:
                X[0]["cc"] += len(cids)
            return cids
        else:
            return False

    X = read(X_CONFIG_NAME)

    prevti = str(X[0]["PEvTi"])
    t1 = s2dt(prevti) if prevti != "" else dt.now()
    t1 = t1 if backlog_start is None else backlog_start
    X[0]["PEvTi"] = dt2s(t1)

    t2 = dt.now() if backlog_end is None else backlog_end
    X[0]["EvTi"] = dt2s(t2)

    stat_diff, delta = stats_delta_t(t1, t2)

    should_count()

    log_X(
        slist=stat_diff,
        ev=ev,
        evti=X[0]["EvTi"],
        pevti=X[0]["PEvTi"],
        delta=delta,
        cc=len(stat_diff),
        others=X[0]["OPs"],
    )

    # showInfo(f"t1: {t1}\n"
    #          f"{t1.timestamp()}\n"
    #          f"t2: {t2}\n"
    #          f"{t2.timestamp()}\n"
    #          f"DATES[0][2]: {DATES[0][2]}\n"
    #          f"DATES[0][2]: {dt.fromtimestamp(DATES[0][2])}"
    #          f"delta: {delta}\n"
    #          f"log_x: \n{X[0]}\n"
    #          f"stat_diff: \n{stat_diff}\n")

    roll_ev()

    return True


@debugger_logger
def event_trigger(ev: int, backlog_start: dt = None, backlog_end: dt = None):
    try:
        logger_comms.info(f"Starting event trigger")
        ev_th = threading.Thread(
            target=event_helper, daemon=True, args=(ev, backlog_start, backlog_end)
        )
        ev_th.start()
        return
    except socket.error:
        show_and_log(
            f"There was a problem with Anki with Friends... Sorry!\n\n"
            f"Error Code 3736",
            True,
        )
        mw.battle_window.timer.stop()

    return True


def undo_rejected():
    global ba_var
    ba_var["popped_req"] = False
    ba_var["ready_for_request"] = True
    ba_var["challenger_name"] = []
    ba_var["requesters_cards"] = list()
    ba_var["challenger_ip"] = []
    ba_var["challenger_progress"] = []
    # save_ba_var()
    mw.battle_window.timer_undo_rejected.stop()
    logger_ui.info("undo_rejected completed")


def config_open(raw_open: str):
    """
    takes the Anki add-on config file as a string, from Anki, and formats it
    in a way to display to the user

    :param raw_open: Anki add-on config file
    :type raw_open: str
    :return: text prompt visible to user
    :rtype: str

    """
    try:
        cfg_dict = json.loads(raw_open)
        aver = cfg_dict["Your Anki Version"]
        baver = cfg_dict["Your Anki with Friends version"]
        sver = cfg_dict["Your Scheduler Version"]
        pid = cfg_dict["PARTICIPANT ID"]
        udeck = cfg_dict["use_deck"]
        sc = cfg_dict["Extra Search Criteria"]

        s1 = f"""|------>>>>>>   Anki with Friends Configuration   <<<<<<------|
   NOTE: AFTER MAKING ANY CHANGES HERE YOU MAY HAVE TO
    RESTART ANKI FOR THE CHANGES TO TAKE EFFECT
Your Anki version:                     {aver}
Your Anki with Friends version:        {baver}
Your Scheduler Version:                {sver}


Enter your Participant ID inside of the brackets below.

(Required)     Participant ID:         [{pid}]


Enter the deck that you would like Anki with Friends to use
inside of the brackets below. PLEASE DO NOT name this deck
'Battle Deck n' where 'n' is any number:

(Required)     Name of deck to use:    [{udeck}]


You may add extra search criteria inside of the brackets below.
for example if you want to have cards only due today (without
showing any overdue cards), you would type 'prop:due=0'.
Other Anki search syntax is available here:
https://docs.ankiweb.net/#/searching?id=searching

(Optional)     Extra search criteria:  [{sc}]


Please make sure to click 'OK' below to save changes"""

        logger_ui.info(
            f"{sys._getframe().f_code.co_name}ed\n" f"Text displayed:\n" f"{s1}\n"
        )

        return s1

    except Exception as txt:
        show_and_log(
            f"There was a problem with the Anki with Friends config file:\n"
            f"Error code: C3499\n"
            f"{txt}"
        )
        return raw_open


def config_close(vis_close: str):
    """
    takes the text displayed in the config window, and formats it
    into the Anki add-on config file as a string

    :param vis_close: text from user, coming from add-on config window
    :type vis_close: str
    :return: Anki add-on config file as string
    :rtype: str
    """
    global config

    logger_ui.info(
        f"{sys._getframe().f_code.co_name}ed\n" f"Text from user:\n" f"{vis_close}\n"
    )

    try:
        vals = re.findall("\[([^[\]]*)\]", vis_close)
        config["PARTICIPANT ID"] = vals[0] if vals[0] else config["PARTICIPANT ID"]
        config["use_deck"] = vals[1] if vals[1] else config["use_deck"]
        config["Extra Search Criteria"] = (
            vals[2] if vals[2] else config["Extra Search Criteria"]
        )

        return json.dumps(config, indent=2, sort_keys=True)

    except Exception as txt:
        show_and_log(
            f"There was a problem with the Anki with Friends config file:\n"
            f"Error code: C3527\n"
            f"{txt}"
        )


def read_config_to_solo(indict: dict):
    if "solo" in indict.keys():
        solo = dict(indict["solo"])
        write(solo, SOLO_CONFIG)
    return


def get_user_config():
    """
    reads the Anki config.json file, then writes to it
    """
    global sv
    global config
    global use_deck
    # global PORT
    # global SERVER
    # global password
    global xtra_search
    global lg_dct
    global deID

    config = mw.addonManager.getConfig(__name__)
    use_deck = str(config["use_deck"]).strip()
    #  todo: invoke password usage here
    xtra_search = str(config["Extra Search Criteria"]).strip()
    config["Your Anki Version"] = anki.buildinfo.version
    config["Your Anki with Friends version"] = BA_VER

    deID = int(config["PARTICIPANT ID"])

    try:
        sv = mw.col.schedVer()
    except:
        pass
    config["Your Scheduler Version"] = sv
    mw.addonManager.writeConfig(__name__, config)

    read_config_to_solo(config)

    cfg_keys = [
        "Your Anki Version",
        "Your Anki with Friends version",
        "Your Scheduler Version",
        "use_deck",
        "Extra Search Criteria",
        "server_ip_address",
        "server_port",
        "server_password",
        "PARTICIPANT ID",
    ]
    lg_keys = ["Anki", "BA", "scv", "deck", "xsc", "sip", "spt", "spw", "PID"]
    tmpd = {cfg_keys[i]: lg_keys[i] for i in range(9)}
    lg_dct = {tmpd[k]: v for k, v in config.items() if k in cfg_keys}

    return


def mw_init():
    global ba_var
    ba_var["mw_did_init"] = True
    if ba_var["prof_did_open"]:
        ba_init()
    return


def prof_open():
    global ba_var
    ba_var["prof_did_open"] = True
    if ba_var["mw_did_init"]:
        ba_init()
    return


# todo: compare the last week to revlog  per day
#   should be writing cumulative cards logged, to X_config... can compare with a database query
def compare_revlog_X_log():
    count_revlog, dummy = stats_delta_t(DATES[1][1], dt.now(), "count()")

    X = read(X_CONFIG_NAME)

    try:
        if int(X[0]["cc"]) == int(count_revlog[0][0]):
            return True
        else:
            return False
    except TypeError:
        pass


def sync_finished():

    same = compare_revlog_X_log()

    # f'{sys._getframe().f_code.co_name}\n'

    # showInfo(f'Extra cards found: {not same}')

    if same:
        return
    else:
        # todo: popup telling user BA needs more time to sync?
        #   problem - need to get cards from database
        event_trigger(CARD_DISCREPANCY, DATES[0][1])
        return


def msg():
    new_msg = [d["msg"] for d in sd if "msg" in d.keys()]
    return str(new_msg[0]) if new_msg else False


def reset_if_new_day():
    s = read(SOLO_CONFIG)[0]
    if (s2dt(s["today"]["finish"]).day != dt.now().day) or (
        s2dt(s["today"]["finish"]).month != dt.now().month
    ):
        bw.reset_solo("today")
    return


def state_changed(new: str, old: str):
    """
    triggers event based on change of state, calls event_trigger() and passes the event to it
    """
    # showInfo(f'{sys._getframe().f_code.co_name}\n'
    #          f'New:     {new}\n'
    #          f'Old:     {old}')

    s_msg = msg()
    if s_msg:
        show_and_log(f"{msg}")

    event = None

    if new == RV_STATE and ba_var["inbattle"] == 2:
        event = INTO_BATTLE
    elif new == OV_STATE and old == RV_STATE and ba_var["inbattle"] == 2:
        event = OUT_OF_BATTLE
    elif new == RV_STATE and ba_var["inbattle"] == 3:
        event = INTO_SOLO
    elif new == OV_STATE and old == RV_STATE and ba_var["inbattle"] == 3:
        event = OUT_OF_SOLO
    elif new == RV_STATE:
        event = REVIEWER_STARTED
    elif old == RV_STATE:
        event = REVIEWER_CLOSED
    elif new == DB_STATE:
        event = ANKI_STARTED

    if event:
        event_trigger(event)
        return
    else:
        return


# todo: use these hooks?
def sync_started():
    # showInfo(f'{sys._getframe().f_code.co_name}')
    return


def reviewer_will_close():
    # showInfo(f'{sys._getframe().f_code.co_name}')
    return


# itest = 4
# #  todo: test
# def test():
#     showInfo(f'{mw.socket.getsockname()}\n\n'
#              f'{str(mw.socket.getsockname())}\n\n')

#     now = time.time()*1000
#     before = now - (3600*10*1000)
#     showInfo(f"{get_pct_corr(before, now)}")
# res = mw.col.db.all(f"""
# select count(), sum(time)/1000,
# sum(case when ease = 1 then 1 else 0 end), /* failed */
# sum(case when ease = 2 then 1 else 0 end) /* hard */
# from revlog where id > {int(before)} and id < {int(now)}""")
#     showInfo(f"{res}")

# def test(fxn: callable = None):
#     showInfo(f'list: {[t.name for t in threading.enumerate()]}\n\n'
#              f'Main: {fxn("MainThread")}\n'
#              f'recv: {fxn("Battle Anki Receiver")}')
# global itest
#
# event_trigger(itest)
# # showstr = f"itest completed:\n"
# #
# # show_and_log(
# #         showstr
# # )
# if itest == 4:
#     itest = 5
# elif itest == 5:
#     itest = 4
#
# return


action = QAction("Anki with Friends...", mw)
action.triggered.connect(lambda: battle_anki_clicked())
# action.triggered.connect(lambda: test())
mw.form.menuTools.addAction(action)

#   HOOKS
gui_hooks.main_window_did_init.append(mw_init)
gui_hooks.profile_did_open.append(prof_open)
gui_hooks.profile_will_close.append(close_down)
gui_hooks.reviewer_did_answer_card.append(answered_card)
gui_hooks.addon_config_editor_will_display_json.append(config_open)
gui_hooks.addon_config_editor_will_save_json.append(config_close)
gui_hooks.state_did_change.append(state_changed)
gui_hooks.reviewer_will_end.append(reviewer_will_close)
gui_hooks.sync_will_start.append(sync_started)
gui_hooks.sync_did_finish.append(sync_finished)

# gui_hooks.main_window_did_init.append(ba_init)
# gui_hooks.profile_did_open.append(ba_init)
# gui_hooks.reviewer_will_init_answer_buttons.append(reviewer_will_show)
