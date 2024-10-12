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

import logging
import threading
from anki.consts import *
from aqt import mw

# from .consts import *

# from .dicts import *

config = dict()
use_deck = str()
port = int()
server = str()
password = str()
xtra_search = str()
sv = int()

# PID
deID = int()

# ba_var dict:
# acc_list = list()
# accepted_req = False
# badgeview = True
# can_sendittt = False
# card_order = int(DYN_DUEPRIORITY)
# card_order_str = 'Order of relative overdueness'
# card_type_str = 'Reviews only'
# cards_left = 0
# cards_today = 0
# chal_index = int()
# challenger_ip = list()
# challenger_name = list()
# challenger_progress = list()
# conn = list()
# decksize = 100
# ff_ff = False
# inbattle = False
# inbattle_str = 'Ready'
# invite_timed_out = False
# isloading = False
# joiners_box = True
# loc_rem_ip = None
# made_count = None
# make_deck_problem = False
# matched_box = False
# matched_list = list()
# matched_size = int()
# matched_terms = str()
# mature_box = False
# mw.is_connected = False
# mw_did_init = False
# myprogress = 0
# new_AND_review_box = False
# new_box = False
# nty = False
# one_to_ten = False
# opponent_problem = False
# popped_comms = False
# popped_req = False
# prof_did_open = False
# ready_for_request = True
# requester = str()
# requesters_cards = list()
# resched_box = True
# review_box = True
# shutdown = False
# solo = False
# spinbox_decksize = 100
# startup = True
# terms_of_battle = str()
# time_secs = int()
# time_today = '0:00'
# today_only = True
# told_problem = False
# tried = int()
# will_sync = False
# window_open = False

n = int()

cc = "clients connected"
server_data = {cc: []}
sd = server_data[cc]

deltas = list()

bw = object
logger = logging.Logger
logger_ui = logging.Logger
logger_utils = logging.Logger
logger_comms = logging.Logger
logger_user = logging.Logger
handlr = logging.Handler
formatter = logging.Formatter
LOG_FOLD = str()

logger_X = logging.Logger
handlr_X = logging.Handler
formatter_X = logging.Formatter

threadlocker = threading.Lock()

lg_dct = dict()

# chk_socket = (False if socket.gethostname()
#               != 'DESKTOP-F1NF0JO' else True)
