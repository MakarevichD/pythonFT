import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title,"
                           "address, home, mobile, work, fax, email, email2 from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title,
                           address, home, mobile, work, fax, email, email2 ) = row
                list.append(Contact(id=str(id), contact_name=firstname, contact_surname=lastname, contact_address=address,
                                    contact_middle=middlename, contact_nickname=nickname, contact_company=company,
                                    contact_title=title, home_num=home, mobile_num=mobile, work_num=work, fax_num=fax,
                                    contact_email=email, contact_email_2=email2))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
