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


from .consts import *
from .vars import *

log_helper = {
    "cc": 0,
    "Ev": "",
    "EvTi": "",
    "EvTyp": "",
    "LLt": "",
    "LSt": 0,
    "OPs": {},
    "PEv": "",
    "PEvTi": "",
    "PEvTyp": "",
    "PID": "",
    "name": "log_helper",
}
# Ev == Event
# EvTi == Event Time (see dt2s method in myclass.py, m/d/yyyy h:m:s AM/PM)
# EvTyp == Event Type
# LSt = Last Send Time
# LLt == Last Log Time
# OPs == Others Participants
# PEv == Previous Event
# PEvTi == Previous Event Time
# PEvTyp == Previous Event Type
# PID == PARTICIPANT ID


# todo: make BA_config.json file and dict for storage
ba_config = {
    "config": {},
    "use_deck": "",
    "PORT": PORT,
    "SERVER": SERVER,
    "PASSWORD": "",
    "xtra_search": "",
    "sv": 0,
    "name": "ba_config",
}

# X_log == dict for logging events to X_datalog.jsonl file
# Ev == Event
# EvTyp == Event Type
# EvTi == Event Time (see dt2s method in myclass.py, m/d/yyyy h:m:s AM/PM)
# OPs == Others Participants
# PID == PARTICIPANT ID
# sdata == Statistics Data
X_log = {
    "Ev": "",
    "EvTyp": "",
    "EvTi": "",
    "OPs": {},
    "PID": "",
    "sdata": {},
}

# sdata
# Ti = time initial
# Tf = time final
# dt = delta T (in tot secs)
# dpct = percent of days
# cpd = cards per day
# tpc = time per card
# tnc = total number of cards
# flips = flip data
# cpct = percent correct
# ib = in battle
# neds = number of edits
us_met = {
    "Ti": "",
    "Tf": "",
    "dT": float,
    "dpct": float,
    "cpd": float,
    "tpc": float,
    "tnc": int,
    "flips": [],
    "cpct": float,
    "ib": bool,
    "neds": int,
}


# def ba_var_update():
#     global ba_var
#     ba_var = {
#             "acc_list"           : acc_list,
#             "accepted_req"       : accepted_req,
#             "badgeview"          : badgeview,
#             "card_type_str"      : card_type_str,
#             "card_order_str"     : card_order_str,
#             "card_order"         : int(DYN_DUEPRIORITY),
#             "can_sendittt"       : can_sendittt,
#             "cards_left"         : cards_left,
#             "cards_today"        : cards_today,
#             "chal_index"         : chal_index,
#             "challenger_name"    : challenger_name,
#             "challenger_ip"      : challenger_ip,
#             "challenger_progress": challenger_progress,
#             "conn"               : conn,
#             "decksize"           : decksize,
#             "ff_ff"              : ff_ff,
#             "inbattle"           : inbattle,
#             "inbattle_str"       : inbattle_str,
#             "invite_timed_out"   : invite_timed_out,
#             "isloading"          : isloading,
#             "joiners_box"        : joiners_box,
#             "learn_box"          : review_box,
#             "loc_rem_ip"         : loc_rem_ip,
#             "made_count"         : made_count,
#             "make_deck_problem"  : make_deck_problem,
#             "matched_box"        : matched_box,
#             "matched_list"       : matched_list,
#             "matched_terms"      : matched_terms,
#             "matched_size"       : matched_size,
#             "mature_box"         : mature_box,
#             "mw_did_init"        : mw_did_init,
#             "mw.is_connected"    : mw.is_connected,
#             "myprogress"         : myprogress,
#             "name"               : "ba_var",
#             "new_AND_review_box" : new_AND_review_box,
#             "new_box"            : new_box,
#             "nty"                : nty,
#             "one_to_ten"         : one_to_ten,
#             "opponent_problem"   : opponent_problem,
#             "popped_req"         : popped_req,
#             "popped_comms"       : popped_comms,
#             "prof_did_open"      : prof_did_open,
#             "ready_for_request"  : ready_for_request,
#             "requester"          : requester,
#             "requesters_cards"   : requesters_cards,
#             "resched_box"        : resched_box,
#             "review_box"         : review_box,
#             "shutdown"           : shutdown,
#             "spinbox_decksize"   : spinbox_decksize,
#             "startup"            : startup,
#             "terms_of_battle"    : terms_of_battle,
#             "time_today"         : time_today,
#             "told_problem"       : told_problem,
#             "today_only"         : today_only,
#             "tried"              : tried,
#             "window_open"        : window_open,
#             "will_sync"          : will_sync,
#     }
#
#
# ba_var = dict()
# ba_var_update()


ba_var = {
    "name": "ba_var",
    "acc_list": list(),
    "accepted_req": False,
    "badgeview": True,
    "can_sendittt": False,
    "card_order": int(DYN_DUEPRIORITY),
    "card_order_str": "Order of relative overdueness",
    "card_type_str": "Reviews only",
    "cards_left": 0,
    "cards_today": 0,
    "chal_index": int(),
    "challenger_ip": list(),
    "challenger_name": list(),
    "challenger_progress": list(),
    "conn": list(),
    "decksize": 100,
    "ff_ff": False,
    "inbattle": 1,
    "inbattle_str": "Ready",
    "invite_timed_out": False,
    "isloading": False,
    "joiners_box": True,
    "learn_box": True,
    "loc_rem_ip": None,
    "made_count": None,
    "make_deck_problem": False,
    "matched_box": False,
    "matched_list": list(),
    "matched_size": int(),
    "matched_terms": str(),
    "mature_box": False,
    "mw_did_init": False,
    "myprogress": 0,
    "new_AND_review_box": False,
    "new_box": False,
    "nty": False,
    "one_to_ten": False,
    "opponent_problem": False,
    "popped_comms": False,
    "popped_req": False,
    "prof_did_open": False,
    "ready_for_request": True,
    "requester": str(),
    "requesters_cards": list(),
    "resched_box": True,
    "shutdown": False,
    "socket_open": False,
    "solo": False,
    "spinbox_decksize": 100,
    "startup": True,
    "terms_of_battle": str(),
    "time_secs": int(),
    "time_today": "0:00",
    "today_only": True,
    "told_problem": False,
    "tried": int(),
    "will_sync": False,
    "window_open": False,
}


local_data = {
    "ver": BA_VER,
    "card ids": [{}],
    "matched terms": str(),
    "matched size": int(),
    "user info": {
        "name": str(mw.pm.name),
        "Connected": ba_var["socket_open"],
        "in battle?": ba_var["inbattle"],
        "Remote IP": ba_var["loc_rem_ip"],
        "accepted req": ba_var["accepted_req"],
        "progress": ba_var["myprogress"],
        "pfrac": [ba_var["cards_left"], ba_var["decksize"]],
        "deck problem": ba_var["make_deck_problem"],
        "cards today": ba_var["cards_today"],
        "time today": ba_var["time_today"],
        "deID": deID,
    },
    "request options": {
        "req name": str(),
        "req names": [],
        "req Remote IP": str(),
        "req Remote IPs": [],
    },
}


# todo: fix these dicts maybe?

# store_data = dict()
#     {
#     'request options':
# }

# {
#         'both box': None,
#         'deck size': None,
#         'matched box': None,
#         'new box': None,
#         'learn box': None,
#         'mature box': None,
#         'resched box': None,
#         'due box': None,
#         'requester': None
#     }

readys = {
    "my last bat start": int(),
    "last battle start": [],
    "ips": [],
    "names": [],
    "last status": [],
    "cc": [],
}
