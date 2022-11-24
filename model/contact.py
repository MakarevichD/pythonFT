from sys import maxsize


class Contact:

    def __init__(self, contact_name=None, contact_surname=None, work_num=None, mobile_num=None,home_num=None,fax_num=None,
                 contact_email= None, contact_address=None, id=None):
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.work_num = work_num
        self.mobile_num = mobile_num
        self.home_num = home_num
        self.fax_num = fax_num
        self.contact_email = contact_email
        self.contact_address = contact_address

        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.contact_name, self.contact_surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.contact_name == other.contact_name or self.contact_surname == other.contact_surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else: return maxsize