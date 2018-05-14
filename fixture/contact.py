
from model.contact import CONTACT
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(
                wd.find_element_by_xpath("//input[@value='Send e-Mail']")) > 0):
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
        self.addnew_cache = None

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
        self.delete_contact_by_index(0)



    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.addnew_cache = None


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def mod_first_contact(self, new_contact_date):
        self.select_contact_by_index(0, new_contact_date)


    def mod_contact_by_index(self, index, new_contact_date):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # fill contact form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_date)
        wd.find_element_by_name("update").click()
        # submit mod
        # edit
        self.return_to_home_page()
        self.addnew_cache = None


    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    addnew_cache = None


#    def get_addnew_list(self):
#        if self.addnew_cache is None:
#            wd = self.app.wd
#            wd.find_element_by_link_text("home").click()
#            self.addnew_cache = []
#            for element in wd.find_elements_by_name("entry"):
#                lastname = element.find_element_by_xpath(".//td[2]").text
#                name = element.find_element_by_xpath(".//td[3]").text
#                id = element.find_element_by_name("selected[]").get_attribute("value")
#                self.addnew_cache.append(CONTACT(name=name, lastname=lastname, id=id))
#        return list(self.addnew_cache)

    def get_addnew_list(self):
        if self.addnew_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.addnew_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                all_names = cells[1+2].text
                name = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.addnew_cache.append(CONTACT(name=name, lastname=lastname, id=id,
                                                 all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.addnew_cache)

    def open_addnew_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        element = wd.find_elements_by_name("entry")[index]
        cell = element.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_addnew_view_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        element = wd.find_elements_by_name("entry")[index]
        cell = element.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_addnew_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_addnew_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return CONTACT(name=name, lastname=lastname, id=id,
                       home=home, mobile=mobile,
                       work=work, phone2=phone2,
                       email=email, email2=email2, email3=email3)


    def get_addnew_from_view_page(self, index):
        wd = self.app.wd
        self.open_addnew_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return CONTACT(home=home, mobile=mobile,
                       work=work, phone2=phone2)














    #DZ 10