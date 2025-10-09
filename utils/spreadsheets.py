import time
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']  # Or other scopes as needed
SA_INFO = {
    "private_key_id": "88ac6473207ba5fb3401bfab74076ed76c54e687",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDRfiyIDZxiXcdE\n0GSsfDhQbwbmpR2VQ3MIaBmB6JSQbzG1lgGwj3M9OpNpIbazkOoAXs13W0nsuxwF\nDO0s4FA20VsPzCZmsfEAnSl7B7td/1yVrrcfSJ/jr8FHutaMhi2oi0T4ueS8wSax\n5Va0aOziLfiAjSTt9SiW0zTjHWNIiuUfqI02wFMHejKEK44xXZiAMqhw24MUIJw7\nSO3O7ZpRNh5bfuQ7VB4X8VeWAgmXOOgSwEmh5HBHd97na7hi/O5cqvfFmuXmLJAn\nWXE4fAl9B83xvselXCl9WbLX+8EqXQkStmqhhr7Jq6TMpAiPBEn4uffez4p8z2V3\nzNIMdaaPAgMBAAECggEANY1McucPz/FrDAM9iP4kIyOOnw0cV9irIj4CLzw2JgnW\nqjWTbv/slH1Ry3Er1BE6UCfr3BQA/LwD+KKKSot41dqErbAhLOVV1zNVtDaQxgGO\nOFE2TI/zF3AJN33idH+kUk5vrilO+JVjf9xBYtLjoxnfSXVLOG0QGCYbgec0RwmL\nmi7OzOCX+YxVdmgWOjkhfN/GgsonBCQEzUyzdjeMXOpoWNfCDRE2O/1KzhmzcPdk\n0hm/3ML/VpFNaS9MXKYqSMfDibI++3ew0o9vyhuDPXOaeLehNuURlTPZaM7d3nMO\nfKOb1Xh5JxonP6GbUa50FgmMMu+XqbFMIAolS0wrkQKBgQD8l2E1Byv3yOUQFNsk\nqQDgx7T0gXFKIJR9yIhqJHP3xMCIylKUYP2YubkhZugtpgu3hkCF1b0UlVKmZgRa\nUON5Jz9RbJURv3wJKES47+8JL6Fr8xFrH2IuerinKrFblcUYEWoVNMgB0sqmN4MI\nk6xylQqPqjjsv7wQJuxR55VtZwKBgQDUUec2gv3bjji7J9Jpd4B+mc2V0sS734dl\n5Yi2Wo5goqKkuMtywcr8qZty18s3NFK1Flqp26p7Sbyjkifxj+3c1DP6EIDQWb9z\nyNhiv4nBnvDfz/o1t56f00hM5prXEQLknfDPOiko4loe0Ck4xrwSbVU/F7IJQBBD\nvOC5hFAcmQKBgFzHHaVkpPm2iKyHfJbSnMfzkrvcb8hSfzhUWAbkrNPtKOsVpY9q\nsLtQPHfQXKenvdYDMd/2yiStVFZaUm76FxOBHvjBcV+7fcu/Rr7HIn21SQ1lkphO\nRrnbycddHxgMwwA8JUL0yCIjUtwKt86Gr2jG5cIvPAl5w5ILOfI7pd8xAoGAC5Qj\n3c8q9Ow+n8Y+LU49DappkcAaxnwcMCxiVj9+ADseT4lcXve+kCTXu12VUX9i+0kq\nzJSUKYEN7oWr8/p7aE2SQBLiU3pxfGj5k/kKFCsMy8fVx1QqLGEjUj5JN21QEROj\n7EkpsXcWnxOPC++alg6sVXJ/XQ3HVUpZnwReMhECgYB6H4NnARJ5B+/AJg7vgTV+\nWZ6FBX2WfG/pFVA7hdVq+okm7oSurN/mxqoKSJzLcHoF7dLgCJ1zU4K2cIxnVd1x\nwoG0xh9rLCWpfFOqljmPQpvIzh/ZjCJyMs56sXxBvfUctRn4cKw5O2YLqtndo8x6\nDfADF+XvYnMjjyoG8rVT/w==\n-----END PRIVATE KEY-----\n",
    "client_email": "team-code@garena-ai.iam.gserviceaccount.com",
    "client_id": "113380271408391783600",
    "token_uri": "https://oauth2.googleapis.com/token",
}


def main(sheet_link_id: str, specified_sheets: list = None) -> dict:
    if not sheet_link_id:
        return {
            "error": "Error: Invalid Sheet Link",
            "database": []
        }

    try:
        credentials = service_account.Credentials.from_service_account_info(SA_INFO, scopes=SCOPES)
    except Exception as e:
        return {
            "error": "Error: Invalid Service Account Info",
            "database": []
        }

    # Build the Slides API service
    service = build('sheets', 'v4', credentials=credentials)
    spreadsheet_service = service.spreadsheets()

    try:
        spreadsheet = spreadsheet_service.get(spreadsheetId=sheet_link_id).execute()
    except Exception as e:
        return {
            "error": "Error: No Sheets Permission",
            "database": []
        }
    sheets = spreadsheet.get('sheets', [])

    database = []
    spreadsheet_service_value = spreadsheet_service.values()
    for sheet in sheets:
        sheet_name = sheet["properties"]["title"]

        if specified_sheets is None or sheet_name in specified_sheets:  # If you dont pass sheet_name, read all the sheets
            result = spreadsheet_service_value.get(spreadsheetId=sheet_link_id, range=sheet_name).execute()

            rows = result.get("values", [])
            rows_to_dict = []

            for r in rows[1:]:
                if len(r) < len(rows[0]):
                    r += [""] * (len(rows[0]) - len(r))  # Update to row data if it do not enough the elements
                converter = dict(map(lambda k, v: (k, v), rows[0],
                                     r))  # Convert rows to dict, first row is header; data from second row
                rows_to_dict.append(converter)

            database.append({
                sheet_name: rows_to_dict
            })

    return {
        "error": "",
        "database": database
    }