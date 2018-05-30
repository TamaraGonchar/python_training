from pony.orm import *
from model.group import Group
from model.contact import CONTACT
from pymysql.converters import encoders, decoders, convert_mysql_timestamp
from datetime import datetime


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact,
                       table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        deprecated = Optional(str, column='deprecated')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        phone2 = Optional(str, column='phone2')
        groups = Set(lambda: ORMFixture.ORMGroup,
                     table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_addnews_to_model(self, addnews):
        def convert(addnew):
            return CONTACT(id=str(addnew.id), name=addnew.name, lastname=addnew.lastname, address=addnew.address,
                           email=addnew.email, email2=addnew.email2, email3=addnew.email3,
                           home=addnew.home, work=addnew.work,
                           mobile=addnew.mobile, phone2=addnew.phone2)

        return list(map(convert, addnews))

    @db_session
    def get_addnew_list(self):
        return self.convert_addnews_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_addnews_in_groups(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_addnews_to_model(orm_group.contacts)

    @db_session
    def get_addnews_not_in_groups(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_addnews_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None and
                                                    orm_group not in c.groups))
