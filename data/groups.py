import pytest
from model.group import Group
import random
import string


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


constant = [
    Group(name='name1', header='header1', footer='footer1')
]