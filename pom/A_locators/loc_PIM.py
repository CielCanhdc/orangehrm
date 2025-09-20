"""
Naming convention: loc_<type>_<variableName>
frm  Form
mnu  Form menu
btn  Normal button
chk  Check button
opt  Radio button
lbl  Text label
txt  Text edit box
pb   Picture box
pic  Picture
lst  List box
cbo  Combo box
tmr  Timer
tos  Toast
dpd  Dropdown
"""
from config import Config


class Default:
    loc_btn_add = '//button[text()=" Add "]'
    loc_txt_firstName = 'input[name="firstName"]'
    loc_txt_middleName = 'input[name="middleName"]'
    loc_txt_lastName = 'input[name="lastName"]'

    loc_txt_employeeId = '//label[text()="Employee Id"]/../following-sibling::div/input'
    loc_btn_save = 'button[type=submit]'


class Staging(Default):
    """
    Override the locators changed with default locators.
    Example:
        loc_username = '[placeholder="Username"]'

        It will detect automatically to override loc_username of Staging env
    """
    pass


if Config.ENV_LOCATORS.lower() == 'staging':
    locators = Staging()
else:
    locators = Default()