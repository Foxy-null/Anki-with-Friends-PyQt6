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

from .consts import BA_REL_DIR, X_CONFIG_NAME
from .dicts import ba_config, ba_var, log_helper
from .vars import *

from PyQt6 import QtCore, QtWidgets

# import logging.handlers
from datetime import datetime as dt
import json
import os
import tempfile


class myLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.MouseButton.LeftButton:
            self.clicked.emit()


class MyFormatter(logging.Formatter):
    converter = dt.fromtimestamp

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s


def clamp(val, minimum=0, maximum=255):
    if val < minimum:
        return minimum
    if val > maximum:
        return maximum
    return val


def colorscale(hexstr, scalefactor):
    """
    Scales a hex string by ``scalefactor``. Returns scaled hex string.

    To darken the color, use a float value between 0 and 1.
    To brighten the color, use a float value greater than 1.

    >>> colorscale("#DF3C3C", .5)
    #6F1E1E
    >>> colorscale("#52D24F", 1.6)
    #83FF7E
    >>> colorscale("#4F75D2", 1)
    #4F75D2
    """
    hexstr = hexstr.strip("#")
    if scalefactor < 0 or len(hexstr) != 6:
        return hexstr
    r, g, b = int(hexstr[:2], 16), int(hexstr[2:4], 16), int(hexstr[4:], 16)
    r = int(clamp(r * scalefactor))
    g = int(clamp(g * scalefactor))
    b = int(clamp(b * scalefactor))
    return "#%02x%02x%02x" % (r, g, b)


def validate_json(filename: str):
    try:
        if os.path.exists(filename):
            with open(filename) as f:
                return json.load(f)
        else:
            return False
    except:
        return False


# todo: need to save this to memory?
def write(
    indict: object, f_name: str, rel_dir: str = BA_REL_DIR, mode: str = "a+" or "w+"
):
    """
    writes a dict, or list of dicts, to a json or jsonlines file
        - defaults to 'append' for .jsonl and 'write' for .json
        - TO RETURN RESULT WITHOUT WRITING, use only .json or .jsonl as f_name
        - if modification to X_config.json are made, the corresponding dict is also updated in memory
    :param indict: the object you are writing
    :type indict: dict or list
    :param f_name: file name to write to, including file extension;
        should be .json or .jsonl. To return result without writing, only use the .extensions
        (i.e. .json or .jsonl)
    :type f_name: str
    :param mode: append or write to file
    :type mode: str
    :param rel_dir: relative directory between cwd and file
    :type rel_dir: str
    :return: string object identical to the dict or list of dicts that
        were or would have been written
    :rtype: str
    """
    f_dir = os.path.join(os.getcwd(), rel_dir, f_name)

    f_old = os.path.splitext(f_dir)[0] + "_OLD" + os.path.splitext(f_dir)[1]

    (ind, mode) = (2, "w+") if f_name.endswith("json") else (None, mode)

    str_out = ""

    def dump(dump_dict: dict = indict):
        if bool(f_name.split(".")[0]):

            if not f_name == X_CONFIG_NAME:
                with open(f_dir, mode) as f:
                    try:
                        json.dump(dump_dict, f, indent=ind, sort_keys=True)
                        if f_dir.endswith("jsonl"):
                            f.write("\n")
                    except:
                        # x = [log_helper, ba_config, ba_var]
                        json.dump(x, f, indent=ind, sort_keys=True)
                        if f_dir.endswith("jsonl"):
                            f.write("\n")

            else:
                with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f_temp:
                    json.dump(dump_dict, f_temp, indent=4, sort_keys=True)
                    f_temp.flush()
                try:
                    os.remove(f_old)
                except:
                    pass

                try:
                    os.rename(f_dir, f_old)
                except:
                    pass

                try:
                    os.rename(f_temp.name, f_dir)
                except:
                    pass

        chunk = json.dumps(dump_dict, indent=ind, sort_keys=True)

        return "a+", chunk

    if type(indict) == dict:
        mode, str_out = dump()
    elif type(indict) == list and f_name.endswith("json"):
        mode, str_out = dump()
    elif type(indict) == list and f_name.endswith("jsonl"):
        for d in indict:
            if type(d) == dict:
                mode, piece = dump(d)
                str_out += piece

    return f"{str_out}"


def read(f_name: str, rel_dir: str = BA_REL_DIR):
    """
    takes a json or jsonlines file and returns a list of dictionarie(s)
    :param f_name: the filename (including file extension) of the json or jsonlines file you are reading from
    :type f_name: str
    :param rel_dir: relative directory between cwd and file
    :type rel_dir: str
    :return: list of dictionarie(s)
    :rtype: list
    """
    f_dir = os.path.join(os.getcwd(), rel_dir, f_name)

    f_old = os.path.splitext(f_dir)[0] + "_OLD" + os.path.splitext(f_dir)[1]

    result = []

    try:
        if f_name.endswith("json"):
            with open(f_dir, "r") as f:
                result = json.load(f)
            return result if type(result) == list else [result]
        elif f_name.endswith("jsonl"):
            with open(f_dir, "r") as f:
                newlist = list(f)
            for d in newlist:
                result.append(json.loads(d))
            return result
    except:
        if f_name.endswith("json"):
            if validate_json(f_dir):
                read(f_name)
            elif validate_json(f_old):
                try:
                    os.remove(f_dir)
                except:
                    pass
                os.rename(f_old, f_dir)

    # except TypeError as te:
    #     print(f'There was a problem accessing\n'
    #           f'one of the Battle Anki files...\n\n'
    #           f'Please try that again!\n'
    #           f'Error Code 163: {te}')
    #     return [log_helper, ba_config, ba_var]
    #
    # except json.JSONDecodeError as e:
    #     print(f'Problem with decode error\n'
    #           f'maybe problem with file:\n'
    #           f'{e}')


def dt2s(dt_ob: dt = dt.now(), fmt: str = "%m/%d/%y %H:%M:%S"):
    """
    takes a datetime object and returns a formatted string
        if no datetime object is provided, the current time will be used
        if no string format is provided, 'mm/dd/yy hh:mm:ss' will be used
        format codes:
        https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    :param dt_ob: datetime object, or current time
    :type dt_ob: datetime.datetime
    :param fmt: format of string, using dt format codes
    :type fmt: str
    :return: date and time as formatted string
    :rtype: str
    """
    return dt_ob.strftime(fmt)


def s2dt(instr: str, fmt: str = "%m/%d/%y %H:%M:%S"):
    """
    takes date and time as formatted string and returns datetime object
        by default assumes 'mm/dd/yy hh:mm:ss' unless specified by format codes:
        https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    :param instr: date and time as formatted string
    :type instr: str
    :param fmt: format of string, using dt format codes
    :type fmt: str
    :return: datetime object from string
    :rtype: datetime.datetime
    """
    return dt.strptime(instr, fmt)


def parse_qd(data: list):
    res = []
    ks = ["day", "tot_cds", "time", "failed", "learn", "review", "relearn", "filtered"]

    for i in range(0, len(data)):
        vs = []
        for j in range(0, len(data[i])):
            if j == 0:
                val = dt2s(dt.fromtimestamp(data[i][j]))
            else:
                val = data[i][j]
            vs.append(val)
        pairs = zip(ks, vs)
        res.append(dict(pairs))

    return res


def parse_deltaStats(data: list):
    """
    including:
    - tansd = time answered
    - cid = cards.id
    - usn = The update sequence number of the collection: for finding diffs
            value of -1 indicates changes that need to be pushed to server.
            usn < server usn indicates changes that need to be pulled from server
    - ease = Which button you pushed to score your recall.
                1(wrong), 2(hard), 3(ok), 4(easy)
    - ivl = Interval. Used by SRS algorithm
    - lastIvl = Last Interval. Used by SRS algorithm
    - factor = Factor. Used by SRS algorithm
    - time = How many milliseconds your review took, up to 60000 (60s)
    - type = 0=lrn, 1=rev, 2=relrn, 3=cram

    :param data:
    :type data:
    :return:
    :rtype:
    """
    res = []
    # usn = update sequence number
    # type      0=lrn, 1=rev, 2=relrn, 3=cram
    ks = ["tansd", "cid", "usn", "ease", "ivl", "lastIvl", "factor", "tonc", "type"]

    for i in range(0, len(data)):
        vs = []
        for j in range(0, len(data[i])):
            if j == 0:
                val = dt2s(dt.fromtimestamp(data[i][j] / 1000))
            elif j == 7:
                val = data[i][j] / 1000
            else:
                val = data[i][j]
            vs.append(val)
        pairs = zip(ks, vs)
        res.append(dict(pairs))

    return res


# DATES

START_DATETIME = dt.fromtimestamp(dt.now().timestamp() - 2 * 24 * 60 * 60)
HALFWAY_DATETIME = dt.fromtimestamp(dt.now().timestamp())
END_DATETIME = dt.fromtimestamp(dt.now().timestamp() + 2 * 24 * 60 * 60)

START_DATE = dt2s(START_DATETIME)
HALFWAY_DATE = dt2s(HALFWAY_DATETIME)
END_DATE = dt2s(END_DATETIME)

START_POSIX = START_DATETIME.timestamp()
HALFWAY_POSIX = HALFWAY_DATETIME.timestamp()
END_POSIX = END_DATETIME.timestamp()

DATES = [
    [START_DATE, START_DATETIME, START_POSIX],
    [HALFWAY_DATE, HALFWAY_DATETIME, HALFWAY_POSIX],
    [END_DATE, END_DATETIME, END_POSIX],
]

# dt.fromtimestamp() int to dt
# dt.timestamp() dt to int
# dt(year, month, day) etc.
# HALFWAY_DATETIME = dt(2021, 11, 22, 0, 0, 0)
