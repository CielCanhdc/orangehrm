"""
Naming convention: loc_<type>_<variable-name>
frm  Form
mnu  Form menu
cmd  Command button
chk  Check button
opt  Radio button
lbl  Text label
txt  Text edit box
pb   Picture box
pic  Picture
lst  List box
cbo  Combo box
tmr  Timer
"""

from config import Config


class Default:
    loc_username = 'input[name="username"]'
    loc_username_bak_1 = '[placeholder="Username"]'

    loc_password = 'input[name="password"]'
    loc_login = '.orangehrm-login-button'

    loc_login_error_msg = '.oxd-alert-content--error'
    loc_home_page = '.orangehrm-upgrade-layout'


class Staging(Default):
    """
    Override the locators changed with default locators.
    Example:
        loc_username = '[placeholder="Username"]'

        It will detect automatically to override loc_username of Staging env
    """
    loc_username = '[placeholder="Username"]'


map = {
    'default': Default,
    'staging': Staging
}
locators = map.get(Config.ENV_LOCATORS, Default)
