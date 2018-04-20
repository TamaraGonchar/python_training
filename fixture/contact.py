

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def createnew(self, addnew):
        wd = self.app.wd
        self.open_add_new_page()
        # init add new creation
        wd.find_element_by_name("firstname").click()
        # fill add new form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(addnew.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(addnew.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(addnew.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(addnew.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(addnew.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(addnew.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(addnew.adrdress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(addnew.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(addnew.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(addnew.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(addnew.fax)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(addnew.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(addnew.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(addnew.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(addnew.homapage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(addnew.byear)
        wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(addnew.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(addnew.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(addnew.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(addnew.notes)
        # enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()


    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()


    def mod_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.return_to_home_page()


    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

