from fixture.orm import ORMFixture
from model.group import Group
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_addnews_in_groups(Group(id="191"))
    for item in l:
        print(item)
    print(len(l))

finally:
    pass # db.destroy()
