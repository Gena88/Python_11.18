import pytest
from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys




def random_string(prefix, maxlen=None):
    symbols = string.ascii_letters + string.digits + string.punctuation*10 + " "*5
    return prefix + "".join([random.choice(symbols) for i  in range(random.randrange(maxlen))])

testdata = [
    # Group(name=str, header=str, footer=str)
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 5)]
    for header in ["", random_string("header", 5)]
    for footer in ["", random_string("footer", 5)]
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default= lambda x: x.__dict__, indent=2))