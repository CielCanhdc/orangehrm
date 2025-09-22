class ErrorCode:
    BROWSER_NOT_FOUND = "Browser not found"
    ELEMENT_NOT_FOUND = "Element not found"


class AssertionMsg:
    LOGIN_FAIL_MESSAGE = "Login fail message"


class FieldTypes:
    TEXT = 'text'
    SELECT = 'select'
    DATE = 'date'
    SWITCH = 'switch'


fields_type = {
    'Employee Name': FieldTypes.TEXT,
    'Employee Id': FieldTypes.TEXT,
    'Employment Status': FieldTypes.SELECT,
    'Include': FieldTypes.SELECT,
    'Supervisor Name': FieldTypes.TEXT,
    'Job Title': FieldTypes.SELECT,
    'Sub Unit': FieldTypes.SELECT,
    'From Date': FieldTypes.DATE,
    'To Date': FieldTypes.DATE
}
