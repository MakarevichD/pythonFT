from sys import maxsize


class Contact:

    def __init__(self, contact_name=None, contact_surname=None, contact_middle=None, contact_nickname=None,
                 contact_title=None, contact_company=None, all_phones_from_home_page=None, work_num=None,
                 all_emails_from_home_page=None, mobile_num=None, home_num=None, fax_num=None, contact_email=None,
                 contact_email_2=None, contact_address=None,group_id=None, id=None):
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.contact_middle = contact_middle
        self.contact_nickname = contact_nickname
        self.contact_title = contact_title
        self.contact_company = contact_company
        self.work_num = work_num
        self.mobile_num = mobile_num
        self.home_num = home_num
        self.fax_num = fax_num
        self.contact_email = contact_email
        self.contact_email_2 = contact_email_2
        self.contact_address = contact_address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.group_id = group_id
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
            self.id,self.contact_name, self.contact_surname, self.home_num, self.work_num, self.mobile_num,
            self.contact_address, self.contact_company, self.contact_title, self.contact_email,self.contact_email_2,
            self.contact_middle, self.fax_num, self.contact_nickname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id or self.id == other.id is None) \
               and self.contact_name == other.contact_name and self.contact_surname == other.contact_surname,\
               self.home_num == other.home_num, self.work_num == other.work_num,  self.mobile_num == other.mobile_num,\
               self.contact_address == other.contact_address, self.contact_company == other.contact_company,\
               self.contact_title == other.contact_title, self.contact_email == other.contact_email,\
               self.contact_email_2 == other.contact_email_2, self.contact_middle == other.contact_middle,\
               self.fax_num == other.fax_num, self.contact_nickname == other.contact_nickname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
