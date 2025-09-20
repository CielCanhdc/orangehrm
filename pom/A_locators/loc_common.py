"""
Naming convention: loc_<type>_<variableName>
frm  Form
mnu  Menu
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
    loc_mnu_menuItem = '//*[contains(@class, "oxd-main-menu-item--name") and normalize-space(.) = "%s"]'  # Format menu item name
    loc_mnu_topBarItem = '//*[@class = "oxd-topbar-body-nav-tab-item" and normalize-space(.) = "%s"]'
    loc_mnu_topBarSubItem = '//*[@class = "oxd-dropdown-menu" and descendant::text() = "%s"]'

    loc_tos_toastMessage = '#oxd-toaster_1 .oxd-text--toast-message'


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