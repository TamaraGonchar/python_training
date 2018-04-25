

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
        self.fill_contact_form(addnew)
        # enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, addnew):
        wd = self.app.wd
        self.change_field_value("firstname", addnew.name)
        self.change_field_value("middlename", addnew.middlename)
        self.change_field_value("lastname", addnew.lastname)
        self.change_field_value("nickname", addnew.nickname)
        self.change_field_value("title", addnew.title)
        self.change_field_value("company", addnew.company)
        self.change_field_value("address", addnew.address)
        self.change_field_value("home", addnew.home)
        self.change_field_value("mobile", addnew.mobile)
        self.change_field_value("work", addnew.work)
        self.change_field_value("fax", addnew.fax)
        self.change_field_value("email", addnew.email)
        self.change_field_value("email2", addnew.email2)
        self.change_field_value("email3", addnew.email3)
        self.change_field_value("homepage", addnew.homepage)
        self.change_field_value("ayear", addnew.ayear)
        self.change_field_value("address2", addnew.address2)
        self.change_field_value("phone2", addnew.phone2)
        self.change_field_value("notes", addnew.notes)
        #self.pickyear(addnew)


    def pickyear(self, addnew):
        wd = self.app.wd
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



    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def mod_first_contact(self, new_contact_date):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # open mod form
        wd.find_element_by_name("selected[]").click()
        # fill contact form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_date)
        wd.find_element_by_name("update").click()
        # submit mod
        # edit
        self.return_to_home_page()


    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def count(self):
        wd = self.app.wd
        self.open_add_new_page()
        return len(wd.find_elements_by_name("selected[]"))

