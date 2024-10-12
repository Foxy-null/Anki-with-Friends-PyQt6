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

import os
from aqt import mw


DEBUG_MODE = False  # True      # todo: debug here with True/False


BA_VER = "2.90"  # #####################################################################################################
BA_FOLDER_NAME = "613520216"
# ba_path = os.path.join(os.getcwd(), '..', '..', 'addons21', '613520216')
BA_REL_DIR = os.path.join(mw.pm.addonFolder(), BA_FOLDER_NAME)

LOG_NM = "B_A.log"

SOLO_CONFIG = "solo.json"
X_FOLDER_NAME = "Version_X_Logfiles"
X_LOG_NAME = "X_datalog.jsonl"
X_CONFIG_NAME = "X_config.json"

REJOINED = " rejoined the game!"  # 0
JOINED = " joined the game!"  # 1
LEFT = " left the game..."  # 2
NOT_HERE = " is starting..."  # 3
NAME_ONLY = ""  # 4
TAILS = [REJOINED, JOINED, LEFT, NOT_HERE, NAME_ONLY]

HEADER = 32
PORT = 8081
SERVER = "140.83.80.253"
PASSWORD = "PASSWORD"

MSG_FORMAT = "utf-8"
DISCONN_MSG = "Disconnected"

# EVENTS
ANKI_STARTED = 0
ANKI_CLOSED = 1
BA_OPENED = 2
BA_CLOSED = 3
INTO_BATTLE = 4
OUT_OF_BATTLE = 5
OPTIONS_OPENED = 6
OPTIONS_CLOSED = 7
ERROR_POPPED = 8
CONFIG_OPENED = 9
CONFIG_CLOSED = 10
SYNC_STARTED = 11
SYNC_FINISHED = 12
BA_SEND = 13
REVIEWER_STARTED = 14
REVIEWER_CLOSED = 15
CARD_DISCREPANCY = 16
INTO_SOLO = 17
OUT_OF_SOLO = 18

# STATES
DB_STATE = "deckBrowser"
PM_STATE = "profileManager"
OV_STATE = "overview"
RV_STATE = "review"

COLOR_ODD_BAR_BOTTOM_HALF = "#13294b"  # blue
COLOR_ODD_BAR_TOP_HALF = "#C22032"  # red
COLOR_ODD_BAR_BACKGROUND_TOP_HALF = "#13294b"  # blue
COLOR_ODD_BAR_BACKGROUND_BOTTOM_HALF = "#535459"  # dark grey

COLOR_EVEN_BAR_BOTTOM_HALF = "#C22032"  # red
COLOR_EVEN_BAR_TOP_HALF = "#FF552E"  # orange
COLOR_EVEN_BAR_BACKGROUND_TOP_HALF = "#C22032"  # red
COLOR_EVEN_BAR_BACKGROUND_BOTTOM_HALF = "#535459"  # dark grey

COLOR_CIMED_BLUE = "#13294b"
COLOR_CIMED_RED = "#C22032"
COLOR_CIMED_ORANGE = "#FF552E"
COLOR_GRAY_DARK = "#535459"
COLOR_GRAY_WARM = "#767676"
COLOR_GRAY_LIGHT = "#B8B8B8"
COLOR_NEAR_WHITE_GRAY = "#EFF1F1"

EN_PAR_DIS = []

EN_PAR_EN = [
    1232,
    2404,
    3248,
    7180,
    7358,
    7736,
    8330,
    1111,
    2222,
    3333,
    4444,
    5555,
    6666,
    7777,
    8888,
    9997,
    9998,
    9999,
]

ADMIN_LIST = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
