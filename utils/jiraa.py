import functools
import logging
from utils import current_test_id
from utils.logg import logg
# from jira import JIRA


def jira_decorator(test_id: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f'---------------- {test_id} ----------------')
            token = current_test_id.set(test_id)
            try:
                result = func(*args, **kwargs)
                logging.info(f"[{test_id}] Uploaded test result into Jira")
                return result
            finally:
                if token:
                    current_test_id.reset(token)
        return wrapper
    return decorator


def jiraa(test_id):
    """Combine jira with log. Use this decorator in test file"""
    def decorator(func):
        return jira_decorator(test_id)(logg(func))
    return decorator


def jira_create_issue():
    jira_options = {
        'server': 'https://jira.garena.com/'
    }
    jira = JIRA(options=jira_options, token_auth='Nzk0ODc3NjY3OTEzOv32w0t6XIYWXPFON3xFGZrW/YkH')

    issue = jira.search_issues('project = VNWGO and type = Bug  and status = Open ORDER  BY created DESC')
    required_fields = ['project', 'summary', 'description', 'issuetype', 'fixVersions', 'priority', 'labels', 'assignee', 'components']

    data = dict(filter(lambda k: list(k)[0] in required_fields, list(issue[0].raw['fields'].items()) ))
    print(data)

    jira.create_issue(fields=data)

