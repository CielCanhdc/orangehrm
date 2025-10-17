import time
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']  # Or other scopes as needed
SA_INFO = {
    "private_key_id": "88ac6473207ba5fb3401bfab74076ed76c54e687",
    "private_key": "",
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