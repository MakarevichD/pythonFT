from model.contact import Contact
import jsonpickle
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
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
    symbols = string.ascii_letters + string.digits * 10
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)]),


def random_phones(prefix, maxlen):
    numbers = string.digits * 10
    return prefix + "".join([random.choice(numbers) for i in range(maxlen)])


def random_email(self, maxlen):
    email_dom = ['@gmail.com', '@yandex.ru', '@mail.ru', '@list.com']
    index = random.randrange(len(email_dom))
    name = ''.join(random.choice(string.ascii_letters) for _ in range(maxlen))
    email = name + email_dom[index]
    return email


testdata = [Contact(
    contact_name=random_string("contact_name", 6),
    contact_surname=random_string("contact_surname", 8),
    contact_middle=random_string("contact_middle", 8),
    contact_nickname=random_string("contact_nickname", 5),
    home_num=random_phones("+", 10),
    mobile_num=random_phones("+", 10),
    work_num=random_phones("+", 10),
    fax_num=random_phones("+", 10),
    contact_address=random_string("contact_address", 7),
    contact_company=random_string("contact_company", 6),
    contact_title=random_string("contact_title", 7),
    contact_email=random_email("contact_email", 6),
    contact_email_2=random_email("contact_email_2", 4))

    for i in range(3)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
