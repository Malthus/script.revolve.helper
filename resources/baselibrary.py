# *  Library: Basic Functions

import sys
import time


def extract_argument(arguments, index, defaultvalue):
    return arguments[index] if len(arguments) > index else defaultvalue


def get_time_in_milliseconds():
    return int(round(time.time() * 1000))


def escape_path(path):
    return path.replace('\\\\', '\\').replace('\\', '\\\\\\\\')
