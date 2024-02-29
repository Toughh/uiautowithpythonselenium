import pyautogui
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

fake = Faker()


class CommonFunctions:

    @staticmethod
    def generate_random_first_name():
        return fake.first_name()

    @staticmethod
    def generate_random_last_name():
        return fake.last_name()

    @staticmethod
    def generate_random_country_code():
        return fake.country_code()

    @staticmethod
    def mob_num_with_country_code(country_code):
        switch_country_code = {
            '+91': str(country_code) + str(fake.random_int(00000000000, 11111111111)),
            '+97155': str(country_code) + str(fake.random_int(2222222, 8888888))
        }
        return switch_country_code.get(country_code, 'Country Code not exist!!!')

    @staticmethod
    def generate_random_number(start, end):
        return str(fake.random_int(start, end))

    @staticmethod
    def generate_random_email():
        return "qa_auto_" + CommonFunctions.generate_random_first_name() + '_' + CommonFunctions.generate_random_last_name() \
               + '@multibankfx.com'

    @staticmethod
    def select_values(element, value):
        select = Select(element)
        select.select_by_visible_text(value)

    @staticmethod
    def select_first_option(element):
        select = Select(element)
        find_text = select.first_selected_option
        text = find_text.text
        return text

    @staticmethod
    def list_all_options(element):
        select = Select(element)
        options = [x.text for x in select.options]
        return options

    @staticmethod
    def select_client_parent_menu(menu_index):
        return '//*[@id="js-nav-menu"]/li[' + str(menu_index) + ']/a/span[1]'

    @staticmethod
    def select_client_child_menu(menu_index, sub_menu_index):
        return '//*[@id="js-nav-menu"]/li[' + str(menu_index) + ']/ul/li[' + str(sub_menu_index) + ']/a/span'

    @staticmethod
    def select_parent_admin_menu(menu_index):
        return '/html/body/div[1]/aside/div[1]/section/ul/li[' + str(menu_index) + ']/a/span[1]'

    @staticmethod
    def select_child_admin_menu(menu_index, sub_menu_index):
        return '/html/body/div[1]/aside/div/section/ul/li[' + str(menu_index) + ']/ul/li[' + str(sub_menu_index) + ']/a'

    @staticmethod
    def select_reject_reason(index):
        return '//*[@id="RejectDocument_predefined_reasons"]/div[' + str(index) + ']/label/div/ins'

    @staticmethod
    def click_dropdown_to_see_options(dropdown_index):
        return '(//span[starts-with(@id, "select2-chosen-")])[' + str(dropdown_index) + ']'

    @staticmethod
    def select_options(options_index):
        return '(//div[starts-with(@id, "select2-result-label-")])[' + str(options_index) + ']'

    @staticmethod
    def upload_files(filepath):
        pyautogui.sleep(2)
        pyautogui.typewrite(filepath)
        pyautogui.press('enter')

    @staticmethod
    def set_element_attribute(ele_id):
        return "let select = document.getElementById('" + ele_id + "'); select.classList.remove('select2-hidden-accessible'); select.style.display = 'block'; select.nextSibling.style.display='none';"

    @staticmethod
    def set_admin_element_attribute(ele_id):
        return "let select = document.getElementById('" + ele_id + "'); select.style.display = 'block';"

    @staticmethod
    def bo_id_por_approve(type_of_account, id_or_por_approval):
        return "//a[starts-with(@href, '/manager/webit/forexcore/" + type_of_account + "/approve_" + id_or_por_approval + "/')]"

    @staticmethod
    def bo_id_reject(type_of_account):
        return "//a[starts-with(@href, '/manager/webit/forexcore/" + type_of_account + "/reject-document/')]"
