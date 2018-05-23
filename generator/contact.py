# -*- coding: utf-8 -*-
from model.contact import CONTACT
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [CONTACT(name="", middlename="", lastname="", nickname="nickname",
                    address="address", address2="address2")] + [
    CONTACT(name=random_string("name", 10), lastname=random_string("lastname", 20),
            middlename=random_string("middlename", 20), nickname=random_string("nickname", 10),
            address=random_string("address", 30), address2=random_string("address2", 25))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
